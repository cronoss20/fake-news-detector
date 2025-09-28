import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class FakeNewsDetector:
    """AI-powered fake news detector using OpenAI GPT"""
    
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key or api_key == 'demo_key_for_testing':
            raise ValueError("OpenAI API key not found or is demo key. Please set a valid OPENAI_API_KEY environment variable.")
        
        # Initialize OpenAI client with proper parameters
        self.client = OpenAI(
            api_key=api_key,
            timeout=30.0,
            max_retries=2
        )
        
        # System prompt for fake news detection
        self.system_prompt = """
        You are an expert fact-checker and misinformation analyst. Your task is to analyze text content and determine if it contains fake news or misinformation.

        Consider these factors when analyzing:
        1. Factual accuracy and verifiability
        2. Source credibility indicators
        3. Emotional manipulation techniques
        4. Logical fallacies or inconsistencies
        5. Sensationalized language
        6. Missing context or cherry-picked information
        7. Claims that contradict established facts

        Respond with a JSON object containing:
        - "is_fake": boolean (true if likely fake news, false if likely legitimate)
        - "confidence": number between 0-100 (confidence percentage)
        - "reasoning": string (brief explanation of your analysis)
        - "red_flags": array of strings (specific concerns found)

        Be thorough but concise in your analysis.
        """
    
    def analyze_text(self, text):
        """Analyze text for fake news indicators"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": f"Please analyze this text for fake news indicators:\n\n{text}"}
                ],
                max_tokens=500,
                temperature=0.3,
                timeout=30
            )
            
            result = response.choices[0].message.content
            
            # Try to parse JSON response
            import json
            try:
                analysis = json.loads(result)
                return self._validate_analysis(analysis)
            except json.JSONDecodeError:
                # Fallback if AI doesn't return valid JSON
                return self._create_fallback_analysis(result, text)
                
        except Exception as e:
            raise ValueError(f"Error analyzing text: {str(e)}")
    
    def _validate_analysis(self, analysis):
        """Validate and clean the analysis response"""
        # Ensure required fields exist
        required_fields = ['is_fake', 'confidence', 'reasoning']
        for field in required_fields:
            if field not in analysis:
                raise ValueError(f"Missing required field in analysis: {field}")
        
        # Validate confidence range
        confidence = analysis['confidence']
        if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 100:
            analysis['confidence'] = 50  # Default fallback
        
        # Ensure red_flags is a list
        if 'red_flags' not in analysis or not isinstance(analysis['red_flags'], list):
            analysis['red_flags'] = []
        
        return analysis
    
    def _create_fallback_analysis(self, ai_response, original_text):
        """Create fallback analysis when AI doesn't return proper JSON"""
        # Simple heuristic analysis as fallback
        text_lower = original_text.lower()
        
        # Check for common fake news indicators
        fake_indicators = [
            'shocking', 'unbelievable', 'doctors hate', 'they don\'t want you to know',
            'secret', 'hidden truth', 'mainstream media won\'t tell you',
            'breaking:', 'urgent:', 'you won\'t believe'
        ]
        
        red_flags = []
        for indicator in fake_indicators:
            if indicator in text_lower:
                red_flags.append(f"Contains suspicious phrase: '{indicator}'")
        
        # Basic confidence calculation
        confidence = min(len(red_flags) * 25, 75) if red_flags else 25
        
        return {
            'is_fake': len(red_flags) > 2,
            'confidence': confidence,
            'reasoning': ai_response[:200] + "..." if len(ai_response) > 200 else ai_response,
            'red_flags': red_flags
        }
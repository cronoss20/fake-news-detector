from flask import Flask, request, jsonify
from flask_cors import CORS
from text_processor import TextProcessor
from fake_news_detector import FakeNewsDetector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Initialize components
text_processor = TextProcessor()
detector = None
api_available = False

# Try to initialize the detector
try:
    detector = FakeNewsDetector()
    api_available = True
    print("✅ OpenAI API initialized successfully")
except ValueError as e:
    print(f"⚠️ Warning: {e}")
    print("💡 The system will work in demo mode without AI analysis")
    api_available = False

@app.route('/', methods=['GET'])
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'running',
        'message': 'Fake News Detector API is running',
        'api_available': api_available,
        'endpoints': ['/predict', '/analyze']
    })

@app.route('/predict', methods=['POST'])
def predict():
    """Analyze text directly for fake news"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'Text is required'}), 400
        
        text = data['text']
        
        # Validate text
        text = text_processor.clean_text(text)
        text_processor.validate_text_length(text)
        
        if not api_available:
            # Provide demo analysis
            analysis = _demo_analysis(text)
        else:
            # Use AI analysis
            analysis = detector.analyze_text(text)
        
        return jsonify({
            'success': True,
            'analysis': analysis,
            'text_length': len(text),
            'demo_mode': not api_available
        })
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error occurred'}), 500

@app.route('/analyze', methods=['POST'])
def analyze():
    """Analyze URL content for fake news"""
    try:
        data = request.get_json()
        
        if not data or 'url' not in data:
            return jsonify({'error': 'URL is required'}), 400
        
        url = data['url'].strip()
        
        if not url:
            return jsonify({'error': 'URL cannot be empty'}), 400
        
        # Extract content from URL
        try:
            content = text_processor.extract_content_from_url(url)
        except ValueError as e:
            return jsonify({'error': f'URL processing error: {str(e)}'}), 400
        
        # Validate extracted content
        content = text_processor.clean_text(content)
        try:
            text_processor.validate_text_length(content)
        except ValueError as e:
            return jsonify({'error': f'Extracted content issue: {str(e)}'}), 400
        
        if not api_available:
            # Provide demo analysis
            analysis = _demo_analysis(content)
        else:
            # Use AI analysis
            analysis = detector.analyze_text(content)
        
        return jsonify({
            'success': True,
            'url': url,
            'analysis': analysis,
            'content_length': len(content),
            'content_preview': content[:200] + "..." if len(content) > 200 else content,
            'demo_mode': not api_available
        })
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error occurred'}), 500

def _demo_analysis(text):
    """Provide demo analysis when OpenAI API is not available"""
    text_lower = text.lower()
    
    # Check for common fake news indicators
    fake_indicators = [
        'shocking', 'unbelievable', 'doctors hate', 'they don\'t want you to know',
        'secret', 'hidden truth', 'mainstream media won\'t tell you',
        'breaking:', 'urgent:', 'you won\'t believe', 'miracle', 'amazing discovery'
    ]
    
    red_flags = []
    for indicator in fake_indicators:
        if indicator in text_lower:
            red_flags.append(f"Contains suspicious phrase: '{indicator}'")
    
    # Additional checks
    if len(text.split('!')) > 5:
        red_flags.append("Excessive use of exclamation marks")
    
    if any(word in text_lower for word in ['click here', 'click now', 'act fast']):
        red_flags.append("Contains clickbait language")
    
    if any(word in text_lower for word in ['conspiracy', 'cover-up', 'they hide']):
        red_flags.append("Contains conspiracy theory language")
    
    # Calculate confidence based on red flags
    confidence = min(len(red_flags) * 20, 85) if red_flags else 30
    is_fake = len(red_flags) >= 2
    
    reasoning = f"Analysis based on {len(red_flags)} red flags found in the text. "
    if is_fake:
        reasoning += "The text shows multiple indicators commonly found in misinformation."
    else:
        reasoning += "The text shows few indicators of misinformation, though manual fact-checking is still recommended."
    
    return {
        'is_fake': is_fake,
        'confidence': confidence,
        'reasoning': reasoning + " (Demo analysis - real AI analysis requires OpenAI API key)",
        'red_flags': red_flags
    }

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': 'Method not allowed'}), 405

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"🚀 Starting Fake News Detector API on port {port}")
    print(f"🔧 Debug mode: {debug}")
    print(f"🤖 OpenAI API available: {'Yes' if api_available else 'No (Demo mode)'}")
    if not api_available:
        print("💡 Set a valid OPENAI_API_KEY environment variable to enable AI analysis")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
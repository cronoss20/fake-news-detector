import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

class TextProcessor:
    """Utility class for processing text and extracting content from URLs"""
    
    @staticmethod
    def clean_text(text):
        """Clean and normalize text for analysis"""
        if not text:
            return ""
        
        # Remove extra whitespace and normalize
        text = re.sub(r'\s+', ' ', text.strip())
        
        # Remove HTML tags if any
        text = re.sub(r'<[^>]+>', '', text)
        
        return text
    
    @staticmethod
    def extract_content_from_url(url):
        """Extract main text content from a URL"""
        try:
            # Validate URL
            parsed = urlparse(url)
            if not parsed.scheme or not parsed.netloc:
                raise ValueError("Invalid URL format")
            
            # Add http if no scheme
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            # Set headers to mimic a real browser
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Try to find main content
            content_selectors = [
                'article',
                '[class*="content"]',
                '[class*="article"]',
                '[class*="post"]',
                'main',
                '.entry-content',
                '#content'
            ]
            
            content = ""
            for selector in content_selectors:
                elements = soup.select(selector)
                if elements:
                    content = ' '.join([elem.get_text() for elem in elements])
                    break
            
            # Fallback to body text
            if not content:
                content = soup.get_text()
            
            # Clean and return
            return TextProcessor.clean_text(content)
            
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Error fetching URL: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error processing URL content: {str(e)}")
    
    @staticmethod
    def validate_text_length(text, min_length=10, max_length=5000):
        """Validate text length for analysis"""
        if len(text) < min_length:
            raise ValueError(f"Text too short. Minimum {min_length} characters required.")
        if len(text) > max_length:
            raise ValueError(f"Text too long. Maximum {max_length} characters allowed.")
        return True
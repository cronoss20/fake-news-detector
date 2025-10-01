# 🔒 Security Guide for Live Demo

This document outlines security best practices and considerations for deploying the Fake News Detector live demo.

## 🎯 Security Principles

1. **Data Privacy First**: No user data is stored or logged
2. **API Key Security**: Sensitive credentials are protected via environment variables
3. **Input Validation**: All user inputs are sanitized and validated
4. **Minimal Attack Surface**: Only necessary endpoints are exposed
5. **Regular Updates**: Dependencies are kept up-to-date

## 🛡️ Security Measures Implemented

### 1. Data Privacy

**No Data Storage**
- User-submitted text and URLs are processed in memory only
- No databases or persistent storage for user content
- Analysis results are not saved server-side

**No Content Logging**
- User inputs are never logged to files or monitoring systems
- Only system errors are logged (without user content)
- Logs contain no personally identifiable information

**Session Isolation**
- Each request is stateless and independent
- No session tracking or cookies
- No user accounts or authentication required

### 2. API Key Protection

**Environment Variables**
```bash
# Backend .env file
OPENAI_API_KEY=sk-...your-key-here

# NEVER commit .env files to git
# NEVER expose keys in frontend code
# NEVER send keys in API responses
```

**Key Management Best Practices**
1. Use environment variables on hosting platforms
2. Rotate API keys regularly
3. Set spending limits on OpenAI account
4. Monitor API usage for anomalies
5. Use separate keys for development and production

**Demo Mode Fallback**
- Application works without API key using heuristic analysis
- Prevents service disruption if API key is compromised
- Provides immediate functionality without setup

### 3. Input Validation

**Text Input Validation**
```python
# Backend validates all text inputs
def validate_text(text):
    if not text or not text.strip():
        return False, "No text provided"
    if len(text) > 10000:  # Limit text length
        return False, "Text too long"
    return True, text.strip()
```

**URL Input Validation**
```python
# Backend validates all URL inputs
def validate_url(url):
    if not url.startswith(('http://', 'https://')):
        return False, "Invalid URL protocol"
    # Additional validation...
    return True, url
```

**Content Sanitization**
- All HTML is stripped from scraped content
- Special characters are escaped
- Maximum content length enforced

### 4. CORS Configuration

**Backend CORS Settings**
```python
from flask_cors import CORS

# Configure CORS properly
CORS(app, resources={
    r"/*": {
        "origins": ["https://your-frontend-domain.com"],
        "methods": ["POST", "GET"],
        "allow_headers": ["Content-Type"]
    }
})
```

**Production Configuration**
- Whitelist only your frontend domain
- Disable CORS for development only
- Use HTTPS for all production traffic

### 5. Rate Limiting

**Recommended Implementation**
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)

@app.route("/predict", methods=["POST"])
@limiter.limit("10 per minute")
def predict():
    # Your code here
```

**Rate Limit Recommendations**
- Text analysis: 10 requests per minute per IP
- URL analysis: 5 requests per minute per IP (slower due to scraping)
- Overall: 100 requests per hour per IP

### 6. HTTPS/SSL

**Always Use HTTPS in Production**
- Most hosting platforms (Render, Vercel, Railway) provide free SSL
- Never deploy without HTTPS
- Force HTTPS redirects
- Use HSTS headers

**SSL Configuration**
```python
# Flask configuration for production
if os.environ.get('FLASK_ENV') == 'production':
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Strict'
```

## 🚨 Security Headers

### Recommended Headers

```python
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response
```

### Header Explanations

- **X-Content-Type-Options**: Prevents MIME type sniffing
- **X-Frame-Options**: Prevents clickjacking attacks
- **X-XSS-Protection**: Enables browser XSS filter
- **Strict-Transport-Security**: Forces HTTPS connections
- **Content-Security-Policy**: Restricts resource loading

## 🔍 Monitoring and Alerts

### What to Monitor

1. **API Usage**
   - Track OpenAI API calls
   - Monitor costs
   - Set spending limits

2. **Traffic Patterns**
   - Unusual spikes in requests
   - Geographic anomalies
   - Failed request patterns

3. **Error Rates**
   - Track 4xx and 5xx errors
   - Monitor API failures
   - Log exceptions (without user data)

4. **Performance**
   - Response times
   - Server resource usage
   - Database connections (if any)

### Monitoring Tools

**Free Options**
- [UptimeRobot](https://uptimerobot.com) - Uptime monitoring
- [Sentry](https://sentry.io) - Error tracking (free tier)
- Platform-specific dashboards (Render, Vercel, etc.)

**Paid Options**
- [Datadog](https://www.datadoghq.com)
- [New Relic](https://newrelic.com)
- [Pingdom](https://www.pingdom.com)

## 🔐 Dependency Security

### Keep Dependencies Updated

```bash
# Python backend
pip install --upgrade pip
pip list --outdated
pip install --upgrade package-name

# Node.js frontend
npm outdated
npm update
npm audit fix
```

### Automated Security Scanning

**GitHub Security Features**
- Enable Dependabot alerts
- Enable Dependabot security updates
- Review security advisories regularly

**CI/CD Security Checks**
```yaml
# .github/workflows/security.yml
name: Security Scan
on: [push, pull_request]
jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run security audit
        run: |
          cd backend && pip install safety
          safety check
          cd ../frontend && npm audit
```

## 🚫 What NOT to Do

### Never Do These Things

1. ❌ **Never commit `.env` files**
   ```bash
   # Add to .gitignore
   .env
   .env.local
   .env.production
   ```

2. ❌ **Never log user content**
   ```python
   # BAD
   print(f"User input: {user_text}")
   
   # GOOD
   print("Processing user input...")
   ```

3. ❌ **Never expose API keys in frontend**
   ```javascript
   // BAD
   const apiKey = "sk-...";
   
   // GOOD
   // API keys only in backend environment variables
   ```

4. ❌ **Never disable security features in production**
   ```python
   # BAD
   CORS(app, origins="*")
   
   # GOOD
   CORS(app, origins=["https://your-domain.com"])
   ```

5. ❌ **Never store sensitive data in cookies**
   ```python
   # BAD
   response.set_cookie('api_key', api_key)
   
   # GOOD
   # Keep API keys server-side only
   ```

## ✅ Security Checklist

Before deploying to production, verify:

- [ ] Environment variables are set correctly
- [ ] `.env` files are in `.gitignore`
- [ ] HTTPS is enabled
- [ ] CORS is configured with specific origins
- [ ] Rate limiting is implemented
- [ ] Security headers are set
- [ ] Input validation is in place
- [ ] Dependencies are up-to-date
- [ ] Error messages don't leak sensitive info
- [ ] Monitoring and alerts are configured
- [ ] API spending limits are set
- [ ] Content is not logged
- [ ] No hardcoded credentials in code

## 🆘 Security Incident Response

### If API Key is Compromised

1. **Immediately**:
   - Revoke the compromised API key
   - Generate a new key
   - Update environment variables

2. **Within 24 hours**:
   - Review API usage logs
   - Check for unauthorized charges
   - Assess damage scope

3. **Follow-up**:
   - Implement additional monitoring
   - Review access controls
   - Update security procedures

### If Server is Compromised

1. **Immediately**:
   - Take service offline
   - Preserve logs for investigation
   - Notify users if needed

2. **Investigation**:
   - Analyze access logs
   - Identify vulnerability
   - Patch security hole

3. **Recovery**:
   - Deploy patched version
   - Restore service
   - Implement additional safeguards

## 📚 Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Flask Security Best Practices](https://flask.palletsprojects.com/en/2.3.x/security/)
- [React Security Best Practices](https://react.dev/learn/security)
- [OpenAI API Best Practices](https://platform.openai.com/docs/guides/safety-best-practices)

## 📞 Contact

For security concerns or to report vulnerabilities:
- Open a security advisory on GitHub
- Email: angelsierralopez@icloud.com

---

**Remember**: Security is an ongoing process, not a one-time setup. Regularly review and update security measures.

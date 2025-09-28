FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port
EXPOSE 5000

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1", "--timeout", "120", "app:app"]
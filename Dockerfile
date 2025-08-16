# Dockerfile for Three-Stage Semantic Search Pipeline
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create necessary directories
RUN mkdir -p data indices runs reports cfg app

# Set environment variables
ENV PYTHONPATH=/app
ENV TOKENIZERS_PARALLELISM=false

# Expose port for demo app
EXPOSE 8000

# Default command
CMD ["python", "-m", "streamlit", "run", "app/app.py", "--server.port=8000", "--server.address=0.0.0.0"]

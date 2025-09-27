# Use Python 3.11 slim base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies (needed for gradio, pydub, etc.)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for Docker layer caching)
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Gradio port
EXPOSE 7860

# Run your app
CMD ["python", "main.py"]

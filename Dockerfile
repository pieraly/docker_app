FROM python:3.9-slim

# Set working directory to /app
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose port 8000 for the web application
EXPOSE 8000


# Set working directory and run the command to start the web application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
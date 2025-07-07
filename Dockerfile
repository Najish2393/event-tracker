FROM python:3.11-slim-buster

WORKDIR /app

# Copy the requirements file and install dependencies
COPY eventcode/requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Copy your application code into the container
COPY eventcode/app.py .

# Expose the internal port that the Flask application will run on (8000)
EXPOSE 8000

# Define the command to run the application using Gunicorn for production
# -b 0.0.0.0:8000 binds to all network interfaces on port 8000
# app:app refers to the 'app' Flask instance within the 'app.py' module
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]

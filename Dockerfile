FROM python:3.11-slim-buster

WORKDIR /app

COPY eventcode/requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

COPY eventcode/app.py .

EXPOSE 8000

# run the application using Gunicorn for production
# -b 0.0.0.0:8000 binds to all network interfaces on port 8000
# app:app refers to the 'app' Flask instance within the app.py module
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]

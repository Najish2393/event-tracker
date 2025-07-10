FROM python:3.11-slim-buster

WORKDIR /app

COPY eventcode/requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

COPY eventcode/app.py .

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]

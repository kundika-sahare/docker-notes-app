# Dockerfile for simple Flask notes app
FROM python:3.11-slim

WORKDIR /app

# copy requirements and install (cache friendly)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy all app files (templates folder included)
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

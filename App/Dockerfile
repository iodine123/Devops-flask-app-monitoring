FROM python:3.14.0b1-alpine3.20

WORKDIR /app

COPY main.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]
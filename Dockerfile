FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

VOLUME .

CMD ["python", "news.py"]
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

# serve the app / run the app (keep it running)

CMD ["python","run.py"]
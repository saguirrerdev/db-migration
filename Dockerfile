FROM python:3.9-slim

WORKDIR /api

COPY ./api /api

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "app/main.py"]

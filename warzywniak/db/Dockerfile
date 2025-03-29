FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY init_db.py .
CMD ["python", "init_db.py"]

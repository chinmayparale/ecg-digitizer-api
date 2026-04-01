FROM python:3.10-slim
RUN apt-get update && apt-get install -y libgl1-mesa-glx git
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

FROM python:3.13.1-alpine3.21
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "index.py"]
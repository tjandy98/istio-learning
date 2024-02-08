FROM --platform=linux/amd64 python:3.8-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir Flask
EXPOSE 8008
CMD ["python", "app.py"]
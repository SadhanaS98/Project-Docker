FROM python:3.9-slim
WORKDIR /flask_app
COPY . . 
RUN pip install --no-cache-dir flask
RUN pip install --no-cache-dir flask flask-sqlalchemy
EXPOSE 8080
# Run app.py when the container launches
CMD ["python", "helloworld.py"]
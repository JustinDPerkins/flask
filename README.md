# flask

This is a simple python-flask app to upload a file to AWS S3.

# How to Install

1. Please fork or clone this repository
> https://github.com/JustinDPerkins/flask.git

2. Create a Dockerfile
```bash
FROM python:3.6

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

ENV S3_BUCKET_NAME=<your bucket name>
ENV S3_ACCESS_KEY=<your access key>
ENV S3_SECRET_ACCESS_KEY=<your secret key>

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./wsgi.py"]
```

3. Deploy

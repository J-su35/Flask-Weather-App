FROM python:3-alpine3.15

WORKDIR /app
COPY . /app

RUN pip install Flask
RUN pip install requests
EXPOSE 5000


CMD python ./app.py
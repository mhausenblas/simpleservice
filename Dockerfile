FROM python:3.9.2-slim
MAINTAINER Michael Hausenblas
ENV REFRESHED_AT 2021-02-22T13:50

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./simpleservice.py" ]

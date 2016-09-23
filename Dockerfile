FROM python:2.7-onbuild
MAINTAINER Michael Hausenblas "michael@dcos.io"
ENV REFRESHED_AT 2016-09-23T13:43
EXPOSE 9876
CMD [ "python", "./simpleservice.py" ]
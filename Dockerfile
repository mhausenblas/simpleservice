FROM python:2.7-onbuild
MAINTAINER Michael Hausenblas "michael@dcos.io"
ENV REFRESHED_AT 2016-09-23T14:31
CMD [ "python", "./simpleservice.py" ]
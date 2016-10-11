FROM python:2.7-onbuild
MAINTAINER Michael Hausenblas "michael@dcos.io"
ENV REFRESHED_AT 2016-10-11T18:23
CMD [ "python", "./simpleservice.py" ]
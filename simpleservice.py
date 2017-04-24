#!/usr/bin/env python

"""
A simple service

@author: Michael Hausenblas, http://mhausenblas.info/#i
@since: 2016-09-23
"""

import logging
import os
import json
import tornado.ioloop
import tornado.web
import random
import time

from tornado.escape import json_encode

DEBUG = True

##############################################################################
# The following enviroment variables can be overridden
# to simulate different behaviour of the simple service:

# By default simple service serves on 9876 but you can
# make it listen on a different port by setting the env
# variable `PORT0` (also: it listens on all network interfaces,
# i.e. 0.0.0.0).
PORT = os.getenv('PORT0', 9876)

# By default simple service reports this value in
# the /endpoint0 unless overridden by below env variable.
VERSION = os.getenv('SIMPLE_SERVICE_VERSION', "0.5.0")

# By default the `/health` endpoint returns a HTTP code 200
# immediately but you can define the range with the following
# env variables.
#
# Examples:
# HEALTH_MIN=1000 HEALTH_MAX=2000 ... delays between 1 sec and 3 sec
# HEALTH_MAX=500                  ... delays up to 0.5 sec
HEALTH_MIN = os.getenv('HEALTH_MIN', 0) # in milliseconds
HEALTH_MAX = os.getenv('HEALTH_MAX', 0) # in milliseconds

if DEBUG:
  FORMAT = "%(asctime)-0s %(levelname)s %(message)s [at line %(lineno)d]"
  logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt="%Y-%m-%dT%I:%M:%S")
else:
  FORMAT = "%(asctime)-0s %(message)s"
  logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="%Y-%m-%dT%I:%M:%S")

class Endpoint0(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/endpoint0` resource.
    """
    try:
      logging.info("/endpoint0 serving from %s has been invoked from %s", self.request.host, self.request.remote_ip)
      self.set_header("Content-Type", "application/json")
      self.write(json_encode(
        {
          "version" : VERSION,
          "host" : self.request.host,
          "result" : "all is well"
        }
      ))
      self.finish()
    except Exception, e:
      logging.debug(e)
      self.set_status(404)

class Health(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/health` resource.
    """
    try:
      logging.info("/health serving from %s has been invoked from %s", self.request.host, self.request.remote_ip)
      self.set_header("Content-Type", "application/json")
      self.write(json_encode(
        {
          "healthy" : True
        }
      ))

      if HEALTH_MAX > HEALTH_MIN and HEALTH_MIN >= 0: # make sure no shenanigans take place
        delay_response = random.randrange(float(HEALTH_MIN), float(HEALTH_MAX))
        time.sleep(delay_response/1000.0)
      self.finish()
    except Exception, e:
      logging.debug(e)
      self.set_status(404)

class Info(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/info` resource.
    """
    try:
      logging.info("/info serving from %s has been invoked from %s", self.request.host, self.request.remote_ip)
      self.set_header("Content-Type", "application/json")
      self.write(json_encode(
        {
          "version" : VERSION,
          "host" : self.request.host,
          "from" : self.request.remote_ip
        }
      ))
      self.finish()
    except Exception, e:
      logging.debug(e)
      self.set_status(404)

class Environment(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/env` resource.
    """
    try:
      logging.info("/env serving from %s has been invoked from %s", self.request.host, self.request.remote_ip)
      self.set_header("Content-Type", "application/json")
      self.write(json_encode(
        {
          "version" : VERSION,
          "env" : str(os.environ),
        }
      ))
      self.finish()
    except Exception, e:
      logging.debug(e)
      self.set_status(404)

if __name__ == "__main__":
  app = tornado.web.Application([
      (r"/endpoint0", Endpoint0),
      (r"/health", Health),
      (r"/info", Info),
      (r"/env", Environment)
  ])
  app.listen(PORT, address='0.0.0.0')
  logging.info("This is simple service in version v%s listening on port %s", VERSION, PORT)
  tornado.ioloop.IOLoop.current().start()

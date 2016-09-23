#!/usr/bin/env python

"""
A simple service

@author: Michael Hausenblas, http://mhausenblas.info/#i
@since: 2016-09-23
"""

import logging
import os
import argparse
import json
import tornado.ioloop
import tornado.web

from tornado.escape import json_encode

DEBUG = True
VERSION = os.getenv('SIMPLE_SERVICE_VERSION', "0.2.0")
PORT = os.getenv('SIMPLE_SERVICE_PORT', "9876")

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
      logging.info("/endpoint0 has been invoked from %s", self.request.remote_ip)
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

if __name__ == "__main__":
  app = tornado.web.Application([
      (r"/endpoint0", Endpoint0)
  ])
  app.listen(PORT, address='0.0.0.0')
  print("This is a simple service in version v%s listening on port %s" %(VERSION, PORT))
  tornado.ioloop.IOLoop.current().start()
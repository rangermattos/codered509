from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import tornado.web
import signal
import logging
from tornado.options import options
from codered509  import app

is_closing = False

def signal_handler(signum, frame):
    global is_closing
    print('exiting...')
    is_closing = True

def try_exit(): 
    global is_closing
    if is_closing:
        # clean up here
        tornado.ioloop.IOLoop.instance().stop()
        print('exit success')

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000)

signal.signal(signal.SIGINT, signal_handler)
tornado.ioloop.PeriodicCallback(try_exit, 100).start() 
IOLoop.instance().start()

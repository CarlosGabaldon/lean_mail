#!/usr/bin/env python
# encoding: utf-8
"""
gtd.py

Created by Carlos Gabaldon on 2012-02-14.
Copyright (c) 2012 __yellowshovel__. All rights reserved.

[~/Projects/gtd] ➔ python gtd.py

...
http://0.0.0.0:8888/

"""
import os.path
import tornado.ioloop
import tornado.web
import tornado.httpserver

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class Item(object):
    """Item item"""
    def __init__(self, title, msg):
        self.title = title
        self.msg = msg
        
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]
        
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            ui_modules={"Item": ItemModule},
            autoescape=None,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = [Item(title="Weekly status", 
                      msg="This is the weekly status"),
                 Item(title="Team Meeting", 
                      msg="This is about the meeting"),
                 Item(title="Reboot Servers", 
                      msg="This is spam"),
                 Item(title="Spam", 
                      msg="More spam")]
        
        self.render("home.html", items=items)

class ItemModule(tornado.web.UIModule):
    def render(self, item):
        return self.render_string("modules/item.html", item=item)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



if __name__ == "__main__":
    main()
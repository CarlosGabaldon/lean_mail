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
from datetime import datetime
import tornado.ioloop
import tornado.web
import tornado.httpserver


from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class Item(object):
    """Item"""
    def __init__(self, title, content, 
                 ancillary_content = None, author="anonymous", posted_on = datetime.now()):
        self.title = title
        self.content = content
        self.ancillary_content = ancillary_content
        self.author = author
        self.posted_on = posted_on

    def posted_on_friendly(self):
        return self.posted_on.strftime('%m/%d/%Y')
        
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
        items = [Item(title ="Html 5 Rocks", 
                      content="I love it..", 
                      author="Carlos"),
                 Item(title ="CSS3 and you", 
                      content="How to start..",
                      ancillary_content="CSS is Magic!"),
                 Item(title ="JavaScript Today", 
                      content="Modern JavaScript is ..")]
        
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
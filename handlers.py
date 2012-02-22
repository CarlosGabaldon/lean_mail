#!/usr/bin/env python
#
# Copyright 2012 Carlos Gabaldon
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""
handlers.py

Created by Carlos Gabaldon on 2012-02-14.

[~/Projects/gtd] ➔ python gtd.py

...
http://0.0.0.0:8888/

"""
import os.path
import tornado.ioloop
import tornado.web
import tornado.httpserver
import models


from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
        
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
        items = [models.Item(title ="Html 5 Rocks", 
                      content="I love it..", 
                      author="Carlos"),
                 models.Item(title ="CSS3 and you", 
                      content="How to start..",
                      ancillary_content="CSS is Magic!"),
                 models.Item(title ="JavaScript Today", 
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
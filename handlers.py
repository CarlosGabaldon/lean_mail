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

$ python handlers.py
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
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        inbox_items = models.Item.find_all_new()
        action_items = models.Item.find_all_action()
        hold_items = models.Item.find_all_hold()
        completed_items = models.Item.find_all_completed()
        
        self.render("home.html", 
                    inbox_items=inbox_items,
                    action_items=action_items,
                    hold_items=hold_items,
                    completed_items=completed_items)

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
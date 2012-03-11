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
import tornado.ioloop
import tornado.web
import tornado.httpserver
import config
import urls
import tornado.database


from tornado.options import options
        
class Application(tornado.web.Application):
    def __init__(self):
        
        tornado.web.Application.__init__(self, urls.handlers, **config.settings)
        
        # Global connection to the DB across all handlers
        self.db = tornado.database.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db


class HomeHandler(BaseHandler):
    def get(self):
        sql= """select * from item 
                INNER JOIN  message ON item.id = message.item_id 
                where item.state = %s order by item.updated_at;""" 
        
        inbox_items = self.db.query(sql, "New")
        action_items = self.db.query(sql, "Action")
        hold_items = self.db.query(sql, "Hold")
        completed_items = self.db.query(sql, "Completed")
        
        self.render("home.html", 
                    inbox_items=inbox_items,
                    action_items=action_items,
                    hold_items=hold_items,
                    completed_items=completed_items)

class ItemHandler(BaseHandler):
    def get(self, id):
        sql= """select * from item 
                INNER JOIN  message ON item.id = message.item_id 
                where item.id = %s order by item.updated_at;""" 
        
        item = self.db.get(sql, int(id))
        
        item_states = ["New", "Action", "Hold", "Completed"]
        
        self.render("item.html",
                    item=item,
                    item_states=item_states)
                    
    def post(self, id):
        item_state = self.get_argument("item_state")
        sql= """ update item 
                 SET state = %s WHERE id = %s"""
        self.db.execute(sql, item_state, id)
        self.redirect("/")

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



if __name__ == "__main__":
    main()
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
models.py

Created by Carlos Gabaldon on 2012-02-21.

"""

from datetime import datetime
import MySQLdb

class MySQL(object):
    
    def query(self, sql):
        try:
            db = MySQLdb.connect("localhost","root","","lean_mail" )
            cursor = db.cursor()
            cursor.execute(sql)
            return cursor.fetchall()

        except Exception, e: # in 3.1; except Exception as e:
            print e
            
        finally:
            db.close()



class Item(object):
    """Item"""
    def __init__(self, 
                id, 
                kind,
                created_at,
                updated_at,
                message,
                related_messages = None):
            self.id = id,
            self.kind = kind
            self.message = message
            self.related_messages = related_messages
            self.created_at = created_at
            self.updated_at = updated_at
    
    @classmethod
    def create_from_DB_record(cls, record):
        return Item(id=record[0], 
                    kind=record[1],
                    created_at=record[2],
                    updated_at=record[3],
                    message= Message(id=record[4],
                                     sender=record[5],
                                     to=record[6],
                                     subject=record[7],
                                     body=record[8],
                                     sent_on=record[9],
                                     created_at=record[10],
                                     updated_at=record[11],
                                     cc=record[12],
                                     bc=record[13],
                                     headers=record[14]))

    def created_at_friendly(self):
        return self.created_at.strftime('%m/%d/%Y')
        
    def updated_at_friendly(self):
        return self.updated_at.strftime('%m/%d/%Y')
        
    @classmethod
    def find_all_new(cls):   
        items = []
        
        results = MySQL().query(SQLBuilder.getItem(where="WHERE item.kind = 'New'"))
        
        for record in results:
            item = Item.create_from_DB_record(record=record)
            items.append(item)
        
        return items
        
        
    @classmethod
    def find_all_action(cls):
        items = []
        
        results = MySQL().query(SQLBuilder.getItem(where="WHERE item.kind = 'Action'"))
        
        for record in results:
            item = Item.create_from_DB_record(record=record)
            items.append(item)
        
        return items
 
    
    @classmethod
    def find_all_hold(cls):
        items = []
        
        results = MySQL().query(SQLBuilder.getItem(where="WHERE item.kind = 'Hold'"))
        
        for record in results:
            item = Item.create_from_DB_record(record=record)
            items.append(item)
        
        return items

    
    @classmethod
    def find_all_completed(cls):
        items = []
        
        results = MySQL().query(SQLBuilder.getItem(where="WHERE item.kind = 'Completed'"))
        
        for record in results:
            item = Item.create_from_DB_record(record=record)
            items.append(item)
        
        return items
        
        
class Message(object):
    """Message"""
    def __init__(self, 
                id,
                sender,
                to, 
                subject, 
                body,
                sent_on,
                created_at,
                updated_at,
                cc=None, 
                bc=None,
                headers=None):
        self.id = id
        self.sender = sender
        self.to = to
        self.subject = subject
        self.body = body
        self.sent_on = sent_on
        self.created_at = created_at
        self.updated_at = updated_at
        self.cc = cc
        self.bc = bc
        self.headers = headers
        
    def sent_on_friendly(self):
        return self.sent_on.strftime('%m/%d/%Y')


class SQLBuilder(object):
    @classmethod
    def getItem(cls, where):
        return """select item.id, 
                        item.kind, 
                        item.created_at,
                        item.updated_at,
                        message.id as message_id,
                        message.sender as message_sender, 
                        message.sent_to as message_sent_to,
                        message.subject as message_subject,
                        message.body as message_body,
                        message.sent_on as sent_on,
                        message.created_at as message_created_at,
                        message.updated_at as message_updated_at,
                        message.cc as message_cc,
                        message.bc as message_bc,
                        message.headers as message_headers
                FROM item 
                INNER JOIN  message ON item.id = message.item_id 
                %s
                ORDER BY item.updated_at;""" % (where)


if __name__ == '__main__':
  main()


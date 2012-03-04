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
    
    def execute_query(self, sql):
        try:
            db = MySQLdb.connect("localhost","root","","lean_mail" )
            cursor = db.cursor()
            cursor.execute(sql)
            return cursor.fetchall()

        except Exception, e: # in 3.1; except Exception as e:
            print e

        db.close()



class Item(object):
    """Item"""
    def __init__(self, id, kind,
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

    def created_at_friendly(self):
        return self.created_at.strftime('%m/%d/%Y')
        
    def updated_at_friendly(self):
        return self.updated_at.strftime('%m/%d/%Y')
        
    @classmethod
    def find_all_new(cls):
        sql = """select item.id, 
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
                WHERE item.kind = 'New'
                ORDER BY item.updated_at;"""
                
        items = []
        
        results = MySQL().execute_query(sql=sql)
        for col in results:
            item = Item(id=col[0], 
                        kind=col[1],
                        created_at=col[2],
                        updated_at=col[3],
                        message= Message(id=col[4],
                                         sender=col[5],
                                         to=col[6],
                                         subject=col[7],
                                         body=col[8],
                                         sent_on=col[9],
                                         created_at=col[10],
                                         updated_at=col[11],
                                         cc=col[12],
                                         bc=col[13],
                                         headers=col[14]))
            items.append(item)
        
        return items
        
        
    @classmethod
    def find_all_action(cls):
        m1 = Message(sender="Lisa Gabaldon",
                    subject="AT&T Bill",
                    to="cgabaldon@gmail.com",
                    body="Body..")
        m2 = Message(sender="Carlos Gabaldon",
                    subject="Lean Mail",
                    to="cgabaldon@gmail.com",
                    body="Body..")
        m3 = Message(sender="Hacker Monthly",
                    subject="Hacker Monthly Digital Subscription: Issue #21 - February 2012",
                    to="cgabaldon@gmail.com",
                    body="Body..")
                    
        items = [ Item(kind="Action",message=m1),
                  Item(kind="Action",message=m2),
                  Item(kind="Action",message=m3) ]
        
        return items
 
    
    @classmethod
    def find_all_hold(cls):
        m1 = Message(sender="Zappos.com",
                    subject="Your Shipping Confirmation",
                    to="cgabaldon@gmail.com",
                    body="Body..")
        m2 = Message(sender="GitHub",
                    subject="Wiki Created",
                    to="cgabaldon@gmail.com",
                    body="Body..")
                    
        items = [ Item(kind="Hold",message=m1),
                  Item(kind="Hold",message=m2) ]
        
        return items

    
    @classmethod
    def find_all_completed(cls):
        m1 = Message(sender="service@paypal.com",
                    subject="Receipt for Your Payment to UnifiedRegistrar",
                    to="cgabaldon@gmail.com",
                    body="Body..")
        m2 = Message(sender="Namecheap Support",
                    subject="Welcome to Namecheap.com",
                    to="cgabaldon@gmail.com",
                    body="Body..")
        m3 = Message(sender="Google Offers",
                    subject="Overstock.com | Phoenix",
                    to="cgabaldon@gmail.com",
                    body="Body..")
        m4 = Message(sender="PhotoBotos.com",
                    subject="[New post] Death Valley Racetrack",
                    to="cgabaldon@gmail.com",
                    body="Body..")
        m5 = Message(sender="Dwell",
                    subject="This week from Dwell.",
                    to="cgabaldon@gmail.com",
                    body="Body..")
                    
        items = [ Item(kind="Completed",message=m1),
                  Item(kind="Completed",message=m2),
                  Item(kind="Completed",message=m3),
                  Item(kind="Completed",message=m4), 
                  Item(kind="Completed",message=m5) ]
        
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



if __name__ == '__main__':
  main()


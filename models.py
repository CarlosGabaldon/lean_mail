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

class Item(object):
    """Item"""
    def __init__(self, kind,
                 message,
                 related_messages = None):
        self.kind = kind
        self.message = message
        self.related_messages = related_messages
        #self.created_at = created_at
        #self.updated_at = updated_at

    def created_at_friendly(self):
        return self.created_at.strftime('%m/%d/%Y')
        
    def updated_at_friendly(self):
        return self.updated_at.strftime('%m/%d/%Y')
        
    @classmethod
    def find_all_new(cls):
        m1 = Message(sender="Mint.com",
                    subject="Your tax refund has arrived.",
                    to="cgabaldon@gmail.com",
                    body="Body..")
        m2 = Message(sender="Dwell",
                    subject="This week from Dwell.",
                    to="cgabaldon@gmail.com",
                    body="Body..")
        m3 = Message(sender="Amazon.com",
                    subject="Amazon Instant Video: New Releases and the Weekend Movie Sale",
                    to="cgabaldon@gmail.com",
                    body="Body..")
        m4 = Message(sender="Warby Parker",
                    subject="Your Warby Parker order no. 100194087 has been received and will ship out shortly",
                    to="cgabaldon@gmail.com",
                    body="Body..")
                    
        items = [ Item(kind="New",message=m1),
                  Item(kind="New",message=m2),
                  Item(kind="New",message=m3),
                  Item(kind="New",message=m4) ]
        
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
    def __init__(self, sender,
                subject, to, body,
                cc=None, bc=None,
                headers=None, 
                sent_on=datetime.now()):
        self.sender = sender
        self.subject = subject
        self.to = to
        self.body = body
        self.cc = cc
        self.bc = bc
        self.headers = headers
        self.sent_on = sent_on
        #self.created_at = created_at
        #self.updated_at = updated_at
        
    def sent_on_friendly(self):
        return self.sent_on.strftime('%m/%d/%Y')





if __name__ == '__main__':
  main()


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
    def __init__(self, title, content, 
                 ancillary_content = None, author="anonymous", posted_on = datetime.now()):
        self.title = title
        self.content = content
        self.ancillary_content = ancillary_content
        self.author = author
        self.posted_on = posted_on

    def posted_on_friendly(self):
        return self.posted_on.strftime('%m/%d/%Y')




if __name__ == '__main__':
  main()


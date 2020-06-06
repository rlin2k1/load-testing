""" mixed_node.py
Simulating a more realistic scenario where some users are reading posts while
others are writing. In this test, 10% of users are write intensive
while the remaining 90% are read intensive.

Author(s):
    Roy Lin

Date Created:
    June 5th, 2020
"""

import sys, random
from locust import HttpLocust, TaskSet
USERNAME = "cs144"

def readPost(locust):
    postid = random.randint(1, 500) # generate a random number from 1 to 500 (include 1 and 500)
    url_prefix = "/blog/%s" % (USERNAME)
    url_suffix = "/%s" % (str(postid))
    locust.client.get(url_prefix + url_suffix, name = url_prefix)

def writePost(locust):
    postid = random.randint(1, 500) # generate a random number from 1 to 500 (include 1 and 500)
    url_prefix = "/api/%s" % (USERNAME)
    url_suffix = "/%s" % (str(postid))
    locust.client.put(url_prefix + url_suffix, data={"title":"Loading Test", "body": "***Hello World!***"}, name = url_prefix)

class MyTaskSet(TaskSet):
    tasks = {readPost: 9, writePost: 1}
    def on_start(locust):
        """ on_start is called when a Locust start before any task is scheduled """
        response = locust.client.post("/login", data={"username":"cs144", "password": "password"})
        if response.status_code != 200:
            print("FAIL to start with posting login data to server. Make sure that your server is running.")
            sys.exit();

class MyLocust(HttpLocust):
    """ the class MyLocust inherits from the class HttpLocust, representing an HTTP user """
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000

""" read_node.py
Simulating the scenario where all requests from users are read intensive.

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
    url_prefix = "/blog/"
    url_suffix = "%s/%s" % (USERNAME, str(postid))
    locust.client.get(url_prefix + url_suffix, name = url_prefix)

class MyTaskSet(TaskSet):
    tasks = [readPost]
    def on_start(locust):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

class MyLocust(HttpLocust):
    """ the class MyLocust inherits from the class HttpLocust, representing an HTTP user """
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000

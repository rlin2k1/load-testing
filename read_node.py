""" read_node.py
Simulating the scenario where all requests from users are read intensive.
The user whose name is cs144 would randomly open one of his posts via
/editor/post?action=open&username=cs144&postid={num}, where {num} is a random postid.

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
    locust.client.post(url_prefix + url_suffix, ,data={"title":"Loading Test", "body": "***Hello World!***"}, name = url_prefix)

class MyTaskSet(TaskSet):
    tasks = [readPost]
    def on_start(locust):
        """ on_start is called when a Locust start before any task is scheduled """
        response = locust.client.post("/login", data={"username":"cs144", "password": "password"})
        if response.status_code != 200:
            print("FAIL to start with posting data to server. Make sure that your server is running.")
            sys.exit();

class MyLocust(HttpLocust):
    """ the class MyLocust inherits from the class HttpLocust, representing an HTTP user """
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000

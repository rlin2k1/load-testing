""" write_tomcat.py
Simulating the scenario where the requests from users are write intensive.

Author(s):
    Roy Lin

Date Created:
    June 5th, 2020
"""

import sys, random
from locust import HttpLocust, TaskSet

def writePost(locust):
    postid = random.randint(1, 500) # generate a random number from 1 to 500 (include 1 and 500)
    url_prefix = "/editor/post?action=save"
    url_suffix = "&username=cs144&postid=%s&title=Loading%%20Test&body=***Hello%%20World!***" % (str(postid))
    locust.client.post(url_prefix + url_suffix, name = url_prefix)

class MyTaskSet(TaskSet):
    tasks = [writePost]
    def on_start(locust):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

class MyLocust(HttpLocust):
    """ the class MyLocust inherits from the class HttpLocust, representing an HTTP user """
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000

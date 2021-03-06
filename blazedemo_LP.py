from gevent import sleep
from re import findall, compile
from locust import HttpLocust, TaskSet, task

class UserBehaviour(TaskSet):
    @task(1)
    def generated_task(self):
        self.client.get(timeout=30.0, url="http://blazedemo.com")
        self.client.get(timeout=30.0, url="http://blazedemo.com/reserve.php")
        self.client.get(timeout=30.0, url="http://blazedemo.com/purchase.php")
        self.client.get(timeout=30.0, url="http://blazedemo.com/confirmation.php")
        

class GeneratedSwarm(HttpLocust):
    task_set = UserBehaviour
    host = ""
    min_wait = 0
    max_wait = 0


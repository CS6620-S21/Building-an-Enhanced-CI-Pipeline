import time
from locust import HttpUser, task, between

# def index(l):
#     l.client.get("/")

# class UserBehavior(TaskSet):
#     tasks = {index: 1}

# class WebsiteUser(HttpLocust):
#     task_set = UserBehavior
#     wait_time = between(5.0, 9.0)

class WebsiteUser(HttpUser):
    wait_time = between(1,5)

    @task
    def home_page(self):
        # test go siply visit the website with url
        self.client.get(url="/")

    # @task
    # def test2(self):
    #     # test visit the home page with url
    #     self.client.get(url="/home")

    #  @task(3)
    # def view_items(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
    #         time.sleep(1)

    # def on_start(self):
    #     self.client.post("/login", json={"username":"foo", "password":"bar"})

 
# class UserBehavior(TaskSet):
 
#     @task(1)    
#     def create_post(self):
#         headers = {'content-type': 'application/json','Accept-Encoding':'gzip'}
#         self.client.post("/posts",data= json.dumps({
#       "title": "foo",
#       "body": "bar",
#       "userId": 1
#     }), 
#     headers=headers, 
#     name = "Create a new post")
 
 
# class WebsiteUser(HttpLocust):
#     task_set = UserBehavior
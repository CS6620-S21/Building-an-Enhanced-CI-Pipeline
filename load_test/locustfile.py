import time
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

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
from locust import HttpUser, between, task
import json
 

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
 
    @task  
    def create_post(self):
        headers = {'content-type': 'application/json','Accept-Encoding':'gzip'}
        self.client.post("/predict",data= json.dumps({
                                                        "CHAS":{
                                                            "0":0
                                                        },
                                                        "RM":{
                                                            "0":6.575
                                                        },
                                                        "TAX":{
                                                            "0":296.0
                                                        },
                                                        "PTRATIO":{
                                                            "0":15.3
                                                        },
                                                        "B":{
                                                            "0":396.9
                                                        },
                                                        "LSTAT":{
                                                            "0":4.98
                                                        }
                                                    }), 
    headers=headers, 
    name = "Create a new post")
 

from locust import HttpLocust, TaskSet, task 


class myTaskSet(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        response = self.client.get("/cliente/login")
        csrftoken = response.cookies['csrftoken']
        self.client.post('/cliente/login', 
        {'username': 'luis@gmail.com', 'password': 'holamundo'},
        headers = {'X-CSRFToken': csrftoken})
        
    
    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def categorias(self):
        self.client.get("/categorias/consultar_categoria/")

    @task(3):
    

    



class MyLocust(HttpLocust):
    task_set = myTaskSet
    min_wait = 1000
    max_wait = 2000
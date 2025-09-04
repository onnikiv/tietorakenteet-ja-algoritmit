class User:
    
    def __init__(self, sir_name, last_name, username, email, city):
        self.sir_name = sir_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.city = city
    
    def describe_user(self):
        print(f"Name: {self.sir_name} {self.last_name}\nUsername: {self.username}\nEmail: {self.email}\nLocation: {self.city}")
        
    
    def greet_user(self):
        print("Welcome back " + self.username + "!")
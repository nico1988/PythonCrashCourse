class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print("hello, everybody , my name is " + self.first_name + " " + self.last_name)
    def greet_user(self):
        print("hello " + self.first_name)
user1 = User("lili", 'wang')
user1.describe_user()

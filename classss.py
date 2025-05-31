class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        
    def greet(self):
        print("Hello!, my name is "+ str(self.name))
        
    def is_adult(self):
        if self.age>18:
            return True
        else:
            return False
        

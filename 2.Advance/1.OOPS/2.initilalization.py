"""
__init__ - initialization - means setting starting values for attributes

in other languages __init__ is called constructer

"""

class User:

    def __init__(self,age,name):
        # print("it will be invoked at first")
        self.age = age
        self.name = name

    def print_age(self,additonal_message):
        print(self.name,"age",self.age,additonal_message)

user1 = User(40,'dj')
user2 = User(23,'rohit')

user1.print_age("anything")
user2.print_age("law")


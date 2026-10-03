"""
class variables are shared across all instances of a class. - static variables (also known as)
They are defined within the class construction but outside of any instance methods. 
This means that they are not tied to any specific instance of the class, but rather to the class itself.
"""

class User:
    id = 1 #class variable - static variable

    def __init__(self, name:str=""):
        self.name = name
        self.id = User.id
        User.id += 1 #incrementing the class variable for next user

# user1 = User("dj")
# user2 = User("rohit")
# user3 = User("Seerat")

# print(User.id)

# print(user1.id)
# print(user2.id)
# print(user3.id)

users = [User() for __ in range(10)]
for user in users:
    print(user.id)

print(f"Next ID: {User.id}")


"""
OOP - Object Oriented Programming   

Object   

      Objects - containers that stores variables and functions thematically 
      connected to each other for easier future usage
      Classes - blueprint for creating instances (copies) of objects   
      
      Attributes - fields/features
      Methods - functions (behaviors of objects, for example, the dog can bark)   

Instance of class - instance means 'case', 'example', 'pattern' that can differ from other 'cases' that 
                     came out of blueprint (class)   
                     so it's another name for OBJECT 


                  Start the name of your classes with UpperCase!!

      self -> this (in other lang.)
"""
age =50

class User:
   age = 0
   name = ""
   def print_age(self,additional_info):   # everytime you create a method inside class, 1st parameter must be self
      print(self.name,'age:',self.age,additional_info)

   


john= User()
jessica = User()

john.age =15
john.name = "john"
# jessica.age = 25

name ='dj'
john.print_age("whatever")
  # everytime we invoke, you send automatically an object itself.
# # print(jessica.age)

def print_age(name,age):
    print(f"{name}'s", "age: ",age)

print_age(name, age)
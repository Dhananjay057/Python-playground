"""shallow and deep copy"""
# shallow copy - copy.copy()
# deep copy - copy.deepcopy()

import copy
def evil_function(toBeDestroyed):
    print(id(toBeDestroyed[0][0]))
    toBeDestroyed[0][0]=99
    print(toBeDestroyed)
    print(id(toBeDestroyed[0][0]))

mylist = [[2,4],[40,20],144]
print(id(mylist[0][0]))
evil_function(copy.deepcopy(mylist))
print(id(mylist[0][0]))



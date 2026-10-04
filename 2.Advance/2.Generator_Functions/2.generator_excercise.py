""" Create a generator function that will generate numbers multiplied
by themselves

1
4
9
16
25
36

Generate 20 elements, stop, and then again generate 30 numbers.
Save each results in the same list and then show it.
"""
def sqr_generator(n):
    for i in range(n):
        yield i*i

list1 = [x for x in sqr_generator(20)]
list1.extend([x for x in sqr_generator(30)])
print(list1)




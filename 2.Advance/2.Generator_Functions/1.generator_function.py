"""
Yeild - means - supply , provide  and generate

iterator
iterate on

Go through it

Generator function is a function that has YEILD keyword in it. 
It is used to create an iterator.
 It is a simple way of creating iterators using functions.
"""

# iterator expression - a concise way to create an iterator using a single line of code.
evenNumbersGenerators = (i for i in range(10) if i%2==0)

# print(list(evenNumbersGenerators)) # [0, 2, 4, 6, 8]
# print(list(evenNumbersGenerators)) # [] - because generator function can be iterated only once.

def generate_even_numbers():
    for i in range(10):
        if i%2==0:
            yield i

evenNumGene = generate_even_numbers()
print(next(evenNumGene)) # 0 - because it returns only first even number and then
print(next(evenNumGene))
print(next(evenNumGene))
print(next(evenNumGene))
print(next(evenNumGene))
# print(next(evenNumGene))
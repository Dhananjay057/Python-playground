"""
FILE - name of the location that stores permanent data
RAM - temporary data storage.

Operations that you can do on a file:
1. Opening
2. Reading/Writing
3. Closing

basic modes (ways) of opening files:
r - R read - default
w - W write - if the file existed (will be removed), if not - will be created
a - A append (adding new content at the end)

extension is simply saving TEXT that is there only to
              make sure other programs know what is inside the
              type of file for example txt suggest there is text inside

Exception - An exception is an unusual situtaion in program that makes 
            yout program suddenly stop working. It is an error that occurs during the execution of a program.
"""
try:
    tab = ["a","b"]
    file = open("file.txt","w") # Handling
    file.write("Sampleeeeee")
    print(tab[4]) 
# This will raise an exception since there is no index 4 in the list
finally:
    file.close() # This will close the file even if there is an exception
    a=5
    print(a)
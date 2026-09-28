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
tab = ["a","b"]

"""# here we can with open() as file: - 
this will automatically close the file after the block of code is executed even if it raises an exception/error.
This is a better way to handle files in Python."""

with open("file.txt","w") as file: 
    file.write("Sampleeeeee1")
    # print(tab[4]) 
    file.write("Sampleeeeee2")

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

--------------------------------------------------------------------------------------
additional file opening modes:

r+ - allows to read and write

w+ - allows to write and read
the difference between r+ and w+ is that it's gonna
remove existing file if there was no file then
it's gonna create a new file

a+ - "endless" mode of appending and reading
ATTENTION!
write function will ALWAYS append text
even if you change the pointer using "seek"

if file doesn't exist - it creates it 

extension is simply saving TEXT that is there only to
              make sure other programs know what is inside the
              type of file for example txt suggest there is text inside

"""
tab = ["a","b"]
file = open("file.txt","w") # Handling - this open() should be assigned to a variable so that we can perform operations on it.
file.write("Sampleeeeee")
#tab[4]
file.close()    #we should close the file too 


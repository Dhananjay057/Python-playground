"""

read
readline
readlines
splitlines

"""

with open("names.txt", "r", encoding="utf-8") as file:
#    namesAndSurnames = file.read()  # reads the entire content of the file as a single string
#    'Dhananjay MAurya\nRohit Kumar\nPraveen Pratap\nPrakhar Jadaun\nUzzwal Singh\nVipin pandey\nVishal Singh\nBhushan Deaulkar'

#    namesAndSurnames = file.read().splitlines() # return a list of lines in the file, without the newline characters
#    [ 'Dhananjay MAurya', 'Rohit Kumar', 'Praveen Pratap', 'Prakhar Jadaun', 'Uzzwal Singh', 'Vipin pandey', 'Vishal Singh', 'Bhushan Deaulkar']

    # namesAndSurnames = file.readline() # reads the first line of the file and returns it as a string
    namesAndSurnames = file.readlines() # reads all the lines of the file and returns them as a list of strings, where each string represents a line in the file

print(namesAndSurnames)
# print(namesAndSurnames2)

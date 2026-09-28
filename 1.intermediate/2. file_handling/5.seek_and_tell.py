# tell - returns the current position of the file pointer
# seek - moves the file pointer to a specified position

with open("names.txt", "r", encoding="utf-8") as file:
    print(file.readline())
    print(file.tell()) # returns the current position of the file pointer
    print(file.readlines())
    print(file.tell()) # returns the current position of the file pointer
    print(file.seek(3)) # moves the file pointer to the beginning of the file
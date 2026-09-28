with open("names.txt", "a", encoding="utf-8") as file:
    print(file.tell()) # returns the current position of the file pointer
    file.write("Kayudu Lohar")
    print(file.tell()) # returns the current position of the file pointer
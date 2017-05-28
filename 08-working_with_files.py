file_path = "C:\\Andre\\testing.txt"

#creating a new file with write mode
file = open(file_path, "w")
file.write("Hello file!")
file.close()

#open a file with read mode
file = open(file_path, "r")
content = file.read()
print(content)
file.close()

#replace content
file = open(file_path, "w")
file.write("New line here!")
file.close()

#write new line
file = open(file_path, "a")
file.write("\nThis goes to the next line!")
file.close()

file = open(file_path, "r")
content = file.read()
print(content)
file.close()






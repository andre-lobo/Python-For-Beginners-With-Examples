file_path = "C:\\Andre\\testing.txt"

file = open(file_path, "w")
file.close()

with open(file_path, "w") as file:
	file.write("The with method")
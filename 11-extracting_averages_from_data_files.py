import pandas
import glob2

file1_path = "C:\\Andre\\File1.txt"

df = pandas.read_csv(file1_path)
print(df)
print(df.mean())

file_list = glob2.glob("C:\\Andre\\*.txt")
print(file_list)

for file in file_list:
	df = pandas.read_csv(file)
	m = df.mean()
	print("File1: \n" + str(m) + "\n")

for file in file_list:
	df = pandas.read_csv(file)
	m = df.mean()
	m = float(m)
	print("File1: \n" + str(m) + "\n")


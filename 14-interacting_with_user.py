def milesToKm(miles):
	km = miles * 1.60934
	print(km, "km")

#call function
milesToKm(100)

#input: interacting with user
m = input("Please enter miles: ")
m = float(m)
milesToKm(m)
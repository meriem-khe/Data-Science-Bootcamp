a = 12
s = "hello"
try:
	print("inside try")
	print(a + s) # will raise TypeError
	print("Printed using original data types")
except : #will handle every type error
	print("inside except")
	print(str(a) + s)
	print("Printed using type-casted data types")
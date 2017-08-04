# Output the words "Fizz", "Buzz", or "FizzBuzz" when a number
# is either a multiple of 3, 5, or both (3 & 5), respectively,
# for a range of numbers between 1 to 100

x = 0
for x in range(0,100):
	x += 1
	if (x / 15.0).is_integer():
		print("FizzBuzz")

	elif (x / 3.0).is_integer():
		print("Fizz")
	
	elif (x / 5.0).is_integer():
		print("Buzz")

	else:
		print(x)

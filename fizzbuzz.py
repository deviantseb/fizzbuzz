# Output the words "Fizz", "Buzz", or "FizzBuzz" when a number
# is either a multiple of 3, 5, or both (3 & 5), respectively,
# for a range of numbers between 1 to 100


from_number = int(input("Range from?: "))
to_number = int(input("Range to?: "))
fizz_num = int(input("What is Fizz? "))
buzz_num = int(input("What is Buzz? "))

for x in range((from_number - 1), to_number):
	x += 1
	if x % fizz_num == 0 and x % buzz_num == 0:
		print("FizzBuzz")

	elif x % 3 == 0:
		print("Fizz")
	
	elif x % 5 == 0:
		print("Buzz")

	else:
		print(x)

even = 0
odd = 0
start = 1
end = int(input("Enter limit: "))


while start <= end :
	num = int(input("enter number: "))
	if num % 2 == 0 :
		even += num
	elif num % 2 == 1 :
		odd += num

	start += 1


SumOfEven = "total even number: " + str(even)
SumOfOdd = "total odd number: " + str(odd)
print(SumOfEven)
print(SumOfOdd)


if even > odd :
	print("Even has the bigger sum")
elif even < odd :
	print("Odd has the bigger sum")
else:
	print("Even and Odd are equal")


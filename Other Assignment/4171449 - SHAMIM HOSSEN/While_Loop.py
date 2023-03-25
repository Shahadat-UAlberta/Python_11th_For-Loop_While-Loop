# _____________________________ While Loop problem ______________________________#
even = 0
odd = 0
start = 1
end = int(input("Enter End Limit Number :- "))

while start <= end :
	num = int(input("Enter Random Number :- "))
	if num % 2 == 0 :
		even += num
	elif num % 2 == 1 :
		odd += num

	start += 1
# Total even / odd number
even_sum = "Total Even Number :- " + str(even)
odd_sum = "Total Odd Number :- " + str(odd)
print(even_sum)
print(odd_sum)
# Winner Finding
if even > odd :
	print("Even Winner")
elif even < odd :
	print("Odd Winner")
else:
	print("Even and Odd Equal")







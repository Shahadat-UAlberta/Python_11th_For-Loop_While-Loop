
# While Loop with even//Odd

start= 1
end= int(input("Enter num: "))

even_sum= 0
odd_sum= 0

while start<=end:
    num= int(input("Input a num: "))
    if num % 2==0:
        even_sum += num
    else:
        odd_sum += num

    start= start+1

print("Sum of even numbers", even_sum)
print(odd_sum)

#print(f"Sum of even numbers =  {even_sum}")
#print(f"Sum of odd numbers = {odd_sum}")

if even_sum>odd_sum:
    print("even number is winner")
elif even_sum<odd_sum:
    print("odd number is winner")
else:
    print("Both are equal")
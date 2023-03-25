start = 1
Even_sum = 0
Odd_sum = 0
end = int(input("Enter Number:"))
while start <= end:
    num = int(input("Enter Number:"))
    if num % 2 == 0:
        Even_sum += num
    else:
        Odd_sum += num

    start= start+1

print(f"Sum of even number: {Even_sum}")
print(f"Sum of odd numbers: {Odd_sum}")

if Even_sum > Odd_sum:
    print('Even sum is the winner')
elif Even_sum > Odd_sum:
    print('Odd sum is the winner')
elif Even_sum == Odd_sum:
    print('Both are equal')
else:
    print('No Winner')

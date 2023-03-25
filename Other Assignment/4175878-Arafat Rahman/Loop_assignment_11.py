# >>>> loop assignment <<<<


start = 1
sum_even = 0
sum_odd = 0
end = int(input("Enter the end number: "))
print("Enter the number:")
while start <= end:
    num = int(input())
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

    start += 2

print(f"Sum of even numbers: {sum_even}")
print(f"Sum of odd numbers: {sum_odd}")

if sum_even > sum_odd:
    print('Even sum is the winner')
elif sum_odd > sum_even:
    print('Odd sum is the winner')
else:
    print('No winner...Both are equal')



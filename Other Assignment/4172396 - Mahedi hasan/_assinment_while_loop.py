start = 1
end = 5

sum_even = 0
sum_odd = 0

while start <= end:
    num = int(input())
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
    start = start =1

print(f"sum of even numbers: {sum_even}")
print(f"sum of odd numbers: {sum_odd}")

if sum_even > sum_odd:
    print("even number is winner")
elif sum_even < sum_odd:
    print("odd number is winner")
else:
    print("Both are equal")
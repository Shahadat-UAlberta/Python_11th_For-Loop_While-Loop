
start = 1
end = int(input("Enter the end value: "))
even = 0
odd = 0

print("Enter the numbers:")
while start <= end:
    start += 1

    num = int(input())
    if num % 2 == 0:
        even += num
    else:
        odd += num

print(f"Even sum: {even}")
print(f"Odd sum: {odd}")

if even > odd:
    print("Even  is the winner")
elif odd > even:
    print("Odd  is the winner")
else:
    print("Both are equal")



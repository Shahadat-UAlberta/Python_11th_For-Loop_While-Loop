
start = 1
end = int(input("enter the input: "))

Evensum = 0
Oddsum = 0

while start <= end:
    num1 = int(input("enter value: "))

    Evensum += num1
    Oddsum += num2

    start += 1

print(Evensum)
print(Oddsum)

if Evensum % 2 == 0 and Evensum > Oddsum:
    print("Evensum is win")
elif Oddsum % 2 != 0 and Oddsum > Evensum:
    print("Oddsum is win")
else:
    print("Both are loser")
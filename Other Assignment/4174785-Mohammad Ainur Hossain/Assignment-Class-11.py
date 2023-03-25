#   Assignment-Class-11
start = 1
end = int(input("How Many Number Do You Want To Count:"))

EvenSum = 0
OddSum = 0

while start <= end:
    Num = int(input("Enter Number:"))
    if Num % 2 == 0:
        EvenSum = EvenSum + Num
    else:
        OddSum = OddSum + Num
    start = start+1

if EvenSum > OddSum:
    print("EvenSum is winner\n")
else:
    print("OddSum is Winner\n")
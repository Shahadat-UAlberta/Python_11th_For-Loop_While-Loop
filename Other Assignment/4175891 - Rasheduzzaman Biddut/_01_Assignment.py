'''
Assignment Details:
1.	Start = 1
2.	End –> Input from User
3.	Value -> Even / Odd (User Input)
4.	EvenSum -> Even
5.	OddSum -> Odd
6.	Print (EvenSum>OddSum) –> Even Winner || Odd Winner
'''


start = 1
end = int(input("Enter end Numbers:"))
sum_even = 0
sum_odd = 0

while start <= end:
    num = int(input("Enter Integer Number"))
    if num % 2 ==0:
        sum_even += num
    else:
        sum_odd += num
    start = start + 1

print("Even:",sum_even)
print("odd:",sum_odd)

if sum_even > sum_odd:
    print("Even is winner")
elif sum_even < sum_odd:
    print("Odd is winner")
else:
    print("Even and Odd are Equal")



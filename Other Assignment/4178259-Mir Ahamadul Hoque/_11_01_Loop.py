
s1=1
e1= int(input("put the ending numbers :" ))
sumEven=0
for num1 in range(s1,e1+1):
    if( num1 % 2 ==0):
        sumEven=sumEven+num1
        print(sumEven)
sumOdd=0
for num2 in range(s1,e1+1):
    if(num2 % 2 ==1):
        sumOdd = sumOdd + num2
        print(sumOdd)
if sumEven > sumOdd :
    print(f"Sum of even numbers is '%d' which is greater than sum of odd numbers.>> SUM of EVEN is WINNER <<" %sumEven)
else:
    print(f"Sum of odd numbers is '%d' which is greater than sum of even numbers. >> SUM of ODD is WINNER <<" %sumOdd)


start= 1
end= int(input("Enter the end limit: "))

even_sum= 0
odd_sum= 0
while start<=end:
    value= int(input("Input a number: "))
    if value % 2==0:
        even_sum += value
    else:
        odd_sum += value

    start= start+1
print(f"Sum of even numbers =  {even_sum}")
print(f"Sum of odd numbers = {odd_sum}")
if even_sum>odd_sum:
    print(f"Even numbers sum {even_sum} is greater")
else:
    print(f"Odd numbers sum {odd_sum} is greater")
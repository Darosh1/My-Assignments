#task 1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
sub = num1 - num2
multi = num1 * num2
print("The sum is:", sum)
print("The difference is:", sub)
print("The product is:", multi)
#task 2
check = int(input("Enter a number to check if it's even or odd: "))
if check % 2 == 0: 
    print(check, " is even")
else: 
    print(check, " is odd")
#task 3
floating1 = float(input("Enter first float number: "))
floating2 = float(input("Enter second float number: "))
floating3 = float(input("Enter third float number: "))
floatList = [floating1, floating2, floating3]
floatList.sort()
print(floatList)
#task 4
print(f"Max = {max(floatList)}")
print(f"Min = {min(floatList)}")
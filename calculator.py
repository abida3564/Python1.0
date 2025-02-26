number1 = float(input("enter 1st number: "))
number2 = float(input("enter 2nd number: "))
op =input("Enter operator: ")
if op =='+':
    result = number1 + number2
elif op=='-':
    result = number1 - number2
elif op=='*':
    result = number1 * number2
elif op=='/':
    if number2 !=0:
      result = number1 / number2
    else:
      result = "MATH ERROR"
else:
   result = "Invalid!"
print("Result: ", result)



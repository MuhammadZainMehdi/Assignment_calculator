x = int(input("Enter first number: "))
op = input("Enter arithmetic operator: ")
y = int(input("Enter second number: "))

if op == "+":
    sum = x + y
    print("Sum = " , sum)

elif op == "-":
    diff = x -y 
    print("Difference = " , diff)

elif op == "*":
    prod = x * y
    print("Product = " , prod)
    
elif op == "/":
    if y != 0:
        quot = x / y 
        print("Quotient = " , quot)

    else:
        print("Error!: Division by 0 is not possible")
    
elif op == "%":
    rem = x % y
    print("Remainder = " , rem)

else:
    print("Error!: You entered an Invalid Operator")
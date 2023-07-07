a = int(input("Enter your first value:"))
b = int(input("Enter your second value:"))
c = input("Enter your operation")

if a == 45 and b == 3 and c == "*":
    print("Result = 555")
elif a == 56 and b == 9 and c == "+":
    print("Result = 77")
elif a == 56 and b == 6 and c == "/":
    print("Result = 77")
else:
    if c == "+":
        d = a + b
        print("Result =", d)
    elif c == "-":
        print("Result =", a - b)
    elif c == "/":
        print("Result =", a / b)
    elif c == "*":
        print("Result =", a * b)
    else:
        print("Enter a valid operator")
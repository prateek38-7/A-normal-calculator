while True:
    a = int(input(": "))
    op = input("choose an operator (-,+,/,x): ").lower()
    b = int(input(": "))

    if op == "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print(a / b)

    elif op == "-":
        print(a - b)

    elif op == "+":
        print(a + b)

    elif op == "x":
        print(a * b)

    else:
        print("Invalid operator")

    print("_________________________________")


#imp. (x = *) , .lower() is used for do X = x 
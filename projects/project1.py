def calculator():
    print("Select Operator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
          
    choice = input("Enter choice (1/2/3/4):")

    if choice =="1":
        print("You chose addition")
    if choice =="2":
        print("You chose subtraction")
    if choice =="3":
        print("You chose multiply")
    if choice =="4":
        print("You chose divide")
    
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    
    if choice =="1":
        print(f"Result: {num1+num2}")
    elif choice =="2":
        print(f"Result: {num1-num2}")
    elif choice =="3":
        print(f"Result: {num1 *num2}")
    elif choice =="4":
        if num1 !=0:
            print(f"Result: {num1/num2}")
        else:
            print(f"Cannot divide ")
    else:
        print("invaid choice")

calculator()
# python interest calculator using True and break
principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print("Principal can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("interest rate can't be less than zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("time can't be less than or equal zero")
    else:
        break
    
total = principal *pow((1+rate/100),time)
print(f"Balance after {time} years/s: NRP {total:.2f}")
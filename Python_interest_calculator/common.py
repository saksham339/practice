# Python interesrt calculator 

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal can't be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("interest rate can't be less than or equal to zero")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("time can't be less than or equal to zero")
    
total = principal *pow((1+rate/100),time)
print(f"Balance after {time} years/s: NRP {total:.2f}")


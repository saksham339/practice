# marks >=90 ,grade ="A"
# marks >=80 ,grade ="b"
# marks >=70 ,grade ="c"
# 70> marks ,grade ="d"
# num =int(input("Enter your marks"))
# if(num >=90 ):
#     grade ="A"
   
# elif(num >=80 and num <90):
#      grade ="B"
  
# elif(num >=70 and num <80):
#      grade ="C"
    
# else:
#      grade ="D"

# print("grade of the student: ",grade)
# age=98
# if(age >=18):
#     if(age >=80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")
#wap to check if the number enterd by the user is odd or even
# num =int(input("Enter a number:"))
# if(num % 2==0):
#     print("even")
# else:
#     print("odd")
 #wap to find the greatest of 3 numbers entred by the user
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number :"))
# if(a>b):
#     if(a>c):
#         print("a is the gratest")
#     else:
#         print("c is the greatest")

# elif(b>c):
#     print("b is the greatest")
# else:
#     print("c is the greatest")
#wap to check if a number is a multiple of 7 or not.
# num =int(input("Enter a number:"))
# if(num % 7==0):
#     print("multiple of 7")
# else:
#     print("not")
#name the keyword which helps in writting code involves condition.
# if(condition):
    # statements
# a = int(input("Enter any number:"))
# if(a>=18):
#     vote="he can"
# else:
#     vote="he cannot"
# print("He can vote:",vote)
#Wap to check wheather a number entred by user is even or odd.
# a = int(input("Enter any number:"))
# if(a%2==0):
#     print("the number is even")
# else:
#     print("the number is odd")
# a = int(input("Enter any number:"))
# if(a%5==0):
#     print("Hello")
# else:
#     print("Bye")
# amt=0
# a = int(input("Enter any number:"))
# if(a<=100):
#     amt=0;
# elif(a>100 and a<200):
#     amt=(a-100)*5
# elif(a>200):
#     amt=500+(a-200)*10
# print("The price is :",amt)
# wap a program to display last digit of the number
# a = int(input("Enter any number:"))
# b=a%10
# if(b%3==0):
#     print(f"The number {b} is divisible by three")
# else:
#     print(f"The number {b} is not divisible by three")
# write a program to accept percentage from the user and 
# display the grade according to the following criteria:
# Marks          Grade
# >90            A
# >80 and <=90   B
# >=60 and <=80  C 
# # below 60       D 
# marks = int(input("Enter your marks: "))
# if marks>90:
#     grade="A"
# elif(marks>80 and marks<=90):
#     grade="B"
# elif(marks>=60 and marks<=80):
#     grade="C"
# else:
# #     grade="D"
# # print(f"your marks is {marks} and grade is ",grade)
# Write a program to accept the cost price of a bike and display the road
# tax to be paid according to the following criteria:
# #     costprice                            Tax 
#        >100000                             15%
#        >50000 and <=100000                 10%
#        <50000                               5
# amt=0
# cost =int(input("Enter your cost price:"))
# if(cost<=50000):
#     amt=cost*(5/100)
# elif(cost>50000 and cost<=100000):
#     amt=cost*(0.1)
# elif(cost>100000):
#     amt=cost*(0.15)
# print(f"The tax of {cost} is :",amt)
# wap to check weather the year is leap year or nor
# Program to check if a year is a leap year or not

# Input from the user

# Program to check if a year is a leap year or not using nested if

# Input from the user
# year = int(input("Enter a year: "))

# Check if it's a leap year
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is not a leap year.")
#     else:
#         print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
# dict ={
#     "value":"hello",
#     "name":{
        
#     }
# loops in python
# loops are used to repeat instruction

# while loops
# while condition:
#     some work


# Initialize the starting number
# num = 1

# # Loop until num is greater than 100
# while num <= 10:
#     print(num)
#     num += 1
# list = [45,34,53,35,24,53]
# for var in list:
#     print(var)

# string="Saksham Ghimire"
# for a in string:
#     if( a=="h"):
        
#         print("h found")
#         break
#     print(a)
# else:
#     print("End")

# list=[1,4,9,16,25,49,64,81,100]
# for el in list:
#     print(el)
# list=(1,4,9,16,25,36,49,64,81,100,49)
# idx=0
# x=49
# for el in list:
#     if (el==x):
#         print("number found at index ",idx)
#         break
        
#     idx+=1
# range(5)
# print(range(5))
# seq = range(10)
# for i in range(10):
#     print(i)
# list=[]
# i=1
# for a in range(10):
#     list.append(i**2)
    
#     i+=1
# print(list)
# for i in range(2,10,5):#start,stop,step
#     print(i)
# for i in range(1,101,2):
#     print(i)
# a = int (input("Enter a number:"))
# for i in range(1,11):
#     print(f"{a}*{i}={a*i}")
# pass statement: It is use a a place holder for future purpose
# for i in range(5):
#     pass
# print("some useful work")
# sum of first n natural numbers
# n = int(input("enter a number:"))
# i=1
# sum =0
# while (i<=n):
    
#     sum +=i
#     i+=1
    
# print(sum)
# n = int(input("enter a number:"))#for loop 
# sum=0
# i=1
# for i in range(n+1):
#     sum +=i
   
# print(sum)

# factorial
# n = int(input("enter a number:")) #while loop
# fact = 1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print(f"The factorial of {n} is ",fact)

#for loop
# n = int(input("enter a number:"))

# fact=1
# for i in range(1,n+1):
#     fact *=i
# print(f"The factorial of {n} is ",fact)
#function and recurtion
# Block of statements that perform a specific logics
# def calculate_sum(a,b):
#     sum= a + b
#     print(sum)
#     return sum

# calculate_sum(4,5)
# calculate_sum(5,6)
# calculate_sum(12,17)
# #function defination
# def calc(a,b):#parameters
#     return a+b
# sum =calc(3,4)#function call; argument
# print(sum)

# def print_hello():
#     print("hello")
# output=print_hello()
# print(output)
#average of there numbers 
# def ave(a,b,c):
#     avg=(a+b+c)/3
#     print(avg)
#     return avg
# ave(4,5,6)
# there are two types of function 
# built in function
# user define function
# def a(v=3 , b=7):
#     print(v*b)
#     return v*b
# a(1)
# countries=["nepal","usa","india","china"]
# praa={2,3,32,2.3,2}
# a=(3,)
# def print_len(list):
#     print(len(list))
# print_len(countries)
# print_len(praa)
# print_len(a)



#Function in python
'''
it is a block of statements that performs a specific tasks
'''
#function defination
# def calc_sum(a, b): #parameters
#     return a+b

# sum=calc_sum(12, 17)#function call :argument
# print(sum)
'''
def print_hello():
    print("hello")
output=print_hello()
print(output)
'''

#average of three numbers
"""
def average():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = int(input("Enter Third number:"))
    sum =a+b+c
    avg =sum/3
    print("The average is ",avg)
    return avg
average()

"""
#defualt argument
'''
def calc_product(a,b=8):
    print(a*b)
    return a*b

calc_product(4)

'''

#write a function to print the length of the list
'''
countries =["Nepal","usa","china","india","argentina"]

def print_len(list):
    print(len(list))

print_len(countries)

'''
#  write a function to print the element of a list in a straight line
'''
countries =["Nepal","usa","china","india","argentina"]

def print_list(list):
    for item in list:
        print(item,end=" ")
        
print_list(countries)

# '''
# if(0.1+0.2==0.3):
#     print("True")
# else:
#     print("False")
'''
print("Hello world")
'''
        

# # a python program that checks if someone is eligible to vote yes or no
# age=int(input("ENTER YOUR AGE:"))
# if age >=18:
#     print("You are eligible to vote")
# else:
#     print("You cant vote....underage")
    
# create a program to check if a number is odd or even
number=int(input("ENTER A NUMBER:"))
if number % 2 == 0:
    print("even number")
else:
    print("odd number")

    # create a program that checks between 3 numbers which one is the biggest
num1=int(input("ENTER THE FIRST NUMBER:"))
num2=int(input("ENTER THE SECOND NUMBER:"))
num3=int(input("ENTER THE THIRD NUMBER:"))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number")

elif num2 >= num1 and num2 >= num3:
       print(f"{num2} is the largest number")
else:
     print(f"{num3} is the largest number")

  


#  # a python program that checks if someone is eligible to vote yes or no
age=int(input("ENTER YOUR AGE:"))
if age >=18:
    print("You are eligible to vote")
else:
    print("not eligible")



# # Create a program that checks which of 3 numbers is the biggest

num1 = int(input("ENTER THE FIRST NUMBER: "))
num2 = int(input("ENTER THE SECOND NUMBER: "))
num3 = int(input("ENTER THE THIRD NUMBER: "))

if num1 == num2 and num2 == num3:
    print("NO LARGEST NUMBER")

elif num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number")

elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest number")

else:
    print(f"{num3} is the largest number")


# # create a program that performs addition and subtraction
#  , multiplication and division of two numbers based on user
#  input.when declaring variable make sure u  declare them as
#  float to handle decimal numbers and operator as a variable
#  ie operator= input("Enter the operator (+ - * /):")

x=float(input("ENTER FIRST NUMBER:"))
y=float(input("ENTER SECOND NUMBER:"))
operator= input("Enter the operator (+ - * /):")

if operator == "+":
    print(f"SUM IS:{x+y}")

elif operator == "-":
    print(f"DIFFERENCE IS :{x-y}")

elif operator == "*":
    print(f"MULTIPLICATION IS:{x*y}")

elif operator == "/":
    if y != 0:
        print(f"DIVISION IS:{x/y}")
    else:
        print("ERROR CANNOT BE DIVIDED BY ZERO")
else:
    print("INVALID operator")


#GRADE STUDENTS MARKS
#use the following grading system to grade students marks 70 and above = A,
#  60-69 = B, 50-59 = C, 40-49 = D, below 40 = Fail

marks=int(input("ENTER STUDENT MARKS:"))
if marks <0 or marks >100:
    print("INVALID MARKS")
elif marks >=70:
    print("A")
elif marks >=60:
    print("B")
elif marks >=50:
    print("C")
elif marks >=40:
    print("B")
else:
    print("FAIL")






















  


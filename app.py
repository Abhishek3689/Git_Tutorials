from calci import addition,substraction,Multiplication
from area_file import rectangle_area_calculate
print("""
Enter 1. Addition
      2. Substraction
      3. Rectangle Area """)

user_input=int(input("enter options :"))
print("enter value of first and second number")
a=int(input("Enter Num1 :"))
b=int(input("Enter Num2 :"))
if user_input==1:
    print("Addition of number is ")
    res=addition(a,b)
elif user_input==2:
    print("substraction of number is ")
    res=substraction(a,b)
elif user_input==3:
    print("area of rectangle is ")
    res=rectangle_area_calculate(a,b)
else:
    res=None
print(res)
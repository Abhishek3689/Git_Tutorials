from calci import addition,substraction,Multiplication

print("""
Enter 1. Addition
      2. Substraction
      3. Multiplication """)

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
    print("Multiplication of number is ")
    res=Multiplication(a,b)
else:
    res=None
print(res)
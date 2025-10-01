try:
    num1=float(input("Enter a Number: "))
    num2=float(input("Enter another Number: "))
    Result=num1/num2
    print(Result)
except ZeroDivisionError:
    print("Number Cannot be divided by Zero")
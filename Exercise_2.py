num1 = 60

try:
    num2 = float(input("Enter your second number:"))
    Result = (num1/num2)
    print(Result)
except ZeroDivisionError:
    print("You cannot divide a number by zero")
except ValueError:
    print("wrong input")   
finally:
    print("correct")     
   
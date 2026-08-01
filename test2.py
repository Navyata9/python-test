def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

try:
    num_1= int(input("Enter the first number:"))
    num_2= int(input("Enter the second number:"))
    print("add= 1")
    print("subtract= 2")
    print("multiply= 3")
    print("divide= 4")
    choice= input("Enter the function that you want to use:")

    if choice== '1':
        print(num_1,"+",num_2, "=", add(num_1,num_2))
    elif choice== '2':
        print(num_1,"-",num_2, "=", subtract(num_1,num_2))
    elif choice== '3':
        print(num_1,"*",num_2, "=", multiply(num_1,num_2))
    elif choice== '4':
        print(num_1,"/",num_2, "=", divide(num_1,num_2))
    else:
        print("Input not valid")

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter a valid input")




def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if a == 0:
        return "Error! Division by zero is not allowed."
    return a/b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter seconet number: "))

print("--choose operation--")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice(1-4): ")

if choice == "1":
    print("Result:", add(num1,num2))
elif choice == "2":
    print("Result:", subtract(num1,num2))
elif choice == "3":
    print("Result:", multiply(num1,num2))
elif choice == "4":
    print("Result:", divide(num1,num2))
else:
    print("Invalid Choice!")
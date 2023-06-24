print("Choose an option to calculate")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

operation = input()

if operation == "1":
    num1= int(input("Please enter an integer: "))
    num2= int(input("Please enter an integer: "))
    print(num1+num2)

elif operation == "2":
    num1= int(input("Please enter an integer: "))
    num2= int(input("Please enter an integer: "))
    print(num1-num2)

elif operation == "3":
    num1= int(input("Please enter an integer: "))
    num2= int(input("Please enter an integer: "))
    print(num1*num2)

elif operation == "4":
    num1= int(input("Please enter an integer: "))
    num2= int(input("Please enter an integer: "))
    print(num1/num2)

else: 
    print("Invalid entry")
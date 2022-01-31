from packagecalc.calc import*
while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    num1=int(input("Enter First Number:"))
    num2=int(input("Enter Second Number:"))
    choice=input("Enter Your Choice:")
    if choice=='1':
        print(num1,"+",num2,"=",addition(num1,num2))
    elif choice=='2':
        print(num1,"-",num2,"=",subtraction(num1,num2))
    elif choice=='3':
        print(num1,"*",num2,"=",multiplication(num1,num2))
    elif choice=='4':
        print(num1,"/",num2,"=",division(num1,num2))
    else:
        print("Invalid Choice")
        break;





# write a script that checks if someone is eligible to vote.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    #write a script that checks if a number is odd or even.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    #write a script that checks ("python123") is valid else wrong password
password = input("Enter the password: ")
if password == "python123":
    print("Valid password.")
else:
    print("Wrong password.")
    #write a script that checks the largest of three numbers.
num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
num3= int(input("Enter the third number: "))
if num1 > num2 and num1 > num3:
    print(f"The largest number is: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"The largest number is: {num2}")
else:
    print(f"The largest number is: {num3}")
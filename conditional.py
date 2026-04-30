
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num1 < num2:
#     print(f"{num1} is less than {num2}")
# else:
#     print(f"{num1} is equal to {num2}")


# age = int(input("Enter your age: "))

# if age >= 20 and age <= 35:
#     print("You are eligible.")
# elif age < 20:
#     print("you are underage.")
# elif age > 35:
#     print("You are overage.")

has_license = input("Do you have a driving license? (yes/no): ").lower()

if has_license == "yes" or has_license == "y": 
    print("You can drive.")
elif has_license == "no" or has_license == "n":
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You can apply for a driving license.")
    else:
        print("You are underage to apply for a driving license.")
else:
    print("Invalid input")

print("This is the end of the program.")

# temp = 78

# celsius = (temp - 32) * 5/9


# temp1 = 101
# celsius1 = (temp1 - 32) * 5/9

# print(celsius)
# print(celsius1)

# def convert_temp(temp):
#     return (temp - 32) * 5/9 

# celsius=convert_temp(100)
# print(celsius)
# print(convert_temp(90))

# def print_data(name, email, age):
#     print(name, email, age)

# print_data("ali","a@gmail.com",18)

# def print_data(name = "friend"):
#     print(name)

# print_data("Emil")

# def pet_info(animal,name,number = 1):
#     print(f"i have {number} pet")
#     print(f"i have {animal}")
#     print(f"its name is {name}")

# pet_info(name = "Tom", animal="Cat", number = 2)

# print("hello",end=" ")
# def sum_of_numbers(*args):
#     sum = 0

#     for num in args:
#         sum+=num
    
#     return sum

# print(sum_of_numbers(19,56,19,77))

# def sum_of_two_numbers(a,b):
#     return a+b

# def sum_of_three_numbers(a,b,c):
#     return a+b+c

# print(sum_of_two_numbers(39,20))
# print(sum_of_three_numbers(39,20,10))


# def print_data(**data):
#     print(data["name"])
#     print(data["age"])
#     print(data["email"])

# print_data(name="ali",age=18,email="ali@gmail.com",is_married = False)

def greeting(time = "morning"):
    def morning():
        return "Good Morning"
    def afternoon():
        return "Good afternoon"
    def evening():
        return "Good Evening"
    
    if time == "morning":
        return morning
    elif time == "evening":
        return evening
    elif time == "afternoon":
        return afternoon
    # return "hello "*times

# morning = greeting()
# print(morning())

# print(message)

# fun = greeting

# print(fun(5),greeting(5))

x=0

def number():
    global x
    x = 100
    print(x)

number()

print(x)


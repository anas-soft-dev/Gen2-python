# try:
#     number =  int(input("enter number to devide : "))
#     print(10/number)
# except ValueError:
#     print("please enter a valid number")
# except ZeroDivisionError:
#     print("can not devide by zero")
# except Exception as e:
#     print("error")
# else:
#     print("no error found")
# finally:
#     print("finally block")


# try:
#     with open("test","w") as file:
#         print(file.write("test"))
# except PermissionError:
#     print("you dont have permission to open this file")
# except FileNotFoundError:
#     print("file does not exist")

# class PasswordException(Exception):
#     pass

# try:
#     password = input("enter password (min: 6) ")
#     if len(password) < 6:
#         raise PasswordException("password should be atleast 6 characters")
# except PasswordException as e:
#     print(e)

# try:
#     devisor = int(input("enter number : "))
#     number = 10 / devisor
#     print(number)
# except ValueError:
#     print("invalid Vlaue")
# except TypeError:
#     print("invalid type")
# except ZeroDivisionError:
#     print("you can not divide with 0")
# except Exception as e:
#     print("General Error")
# else:
#     print("No Error Found")
# finally:
#     print("Try block executed")

# print("end of program")

# try:
#     with open("test/story.txt", "a") as file:
#         file.write("new line")
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("you dont have permission to open this file")
# except AttributeError:
#     print("Attribute Error")
# except Exception as e:
#     print("Error")
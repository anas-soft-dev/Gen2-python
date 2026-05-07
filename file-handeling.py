# f = open("students.txt")
# print(f.read())
# f.close()
# list_of_lines = []
# with open("students.txt","r") as file:
#     list_of_lines = file.readlines()

# with open("students.txt","w") as file:
#     # list_of_lines.insert(1,"new line\n")
#     list_of_lines.pop(1)
#     file.writelines(list_of_lines)

# with open("students.txt","r") as file:
#     print(file.read())
    # print(file.readlines()[2])
    # print(file.readline())
    # print(file.readline())
    # print(len(file.read().split()))
    # for line in file:
    #     print(line.strip().title())

# print("file closed")

# import os

# if os.path.exists("admins.py"):
#     os.remove("admins.py")
#     print("file deleted")
# else:
#     print("file does not exist")


# with open("students.txt","r") as file:
#     lines = file.readlines()

# lines[3] = "Sanyia\n"
# with open("students.txt","w") as file:
#     file.writelines(lines)

while True:
    print("="*15+"Menu"+"="*15)
    choice  = int(input(f"press 1: to add data\npress 2: to read data\npress 0: to exit\n{"="*34}\nchoice : "))
    match choice:
        case 1:
            text =  input("enter : ")
            with open("/","r") as file:
                file.write(text+'\n')
        case 2:
            with open("student1.txt","r") as file:
                print(file.read())
        case 0:
            break
        case _:
            print("invalid input")
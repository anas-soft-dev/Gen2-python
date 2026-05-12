# attempt = 0
# while True:
#     print("="*20+"Login"+"="*20)
#     username = input("username : ").strip()
#     password = input("password : ").strip()

#     if username == "admin" and password == "123456":
#         print("Successfully login")
#         break
#     else:
#         attempt+=1
#         print("inavalid username or password")

#         if attempt >= 3: exit()

print("="*20+"Admin Panel"+"="*20)

import os

filename = "students.txt"

def read_file():
    with open(filename,"r") as file:
        return filename.readlines()
while True:
    print("Press 1: view data")
    print("Press 2: add data")
    print("Press 3: remove data")
    print("Press 4: update a record")
    print("Press 0: exit")

    choice = int(input("choice : "))

    match choice:
        case 0:
            break
        case 1:
            print("View all records")
            try:
                with open(filename,"r") as file:
                    count = 0
                    for record in file:
                        count+=1
                        record = record.strip().split("||")
                        print("="*10,count,"="*10)
                        print("Name :"+record[0])
                        print("Email :"+record[1])
                        print("Age :"+record[2])
                        
            except FileNotFoundError:
                with open(filename,"x"):
                    print("file created")
            except Exception as e:
                print(e)
            input()
        case 2:
            print("Add Record")
            with open(filename,"a") as file:
                name = input("Name : ").strip()
                email = input("Email: ").strip()
                age = input("Age: ").strip()
                file.write(f"{name}||{email}||{age}\n")

                print("added")
                input()
        case 3:
            print("remove a record")
            email = input("email : ")

            is_found = False
            new_list = []
            with open(filename,"r") as file:
                student_list = file.readlines()
                for student in student_list:
                    record = student.strip().split("||")
                    record.pop()
                    new_list.append("||".join(record))
                    if record[1] == email.strip():
                        is_found = True
                        student_list.remove(student)
                        break
            
            if is_found:
                with open(filename,"w") as file:
                    file.writelines(student_list)
                    print("record Deleted")
            else: print("Student not found with this email")

            input()
        case 4:
            print("update a record")
            email = input("email : ").strip()
            is_found = False
            with open(filename,"r") as file:
                student_list = file.readlines()

                for index, student in enumerate(student_list):
                    record = student.strip().split("||")

                    if record[1] == email:
                        name = input("name : ")
                        age = input("age : ")
                        student_list[index] = f"{name}||{email}||{age}\n"
                        is_found = True
                        break
            if is_found:
                with open(filename,"w") as file:
                    file.writelines(student_list)
                    print("Updated")
            else:
                print("record not found")
            input("enter ..")
        case _:
            print("invalid choice")
    # For Windows
    os.system("cls")
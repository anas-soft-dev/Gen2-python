# Task 1
# with open("student.txt","w") as file:
#     for i in range(5):
#         student_name=input(f"enter the student {i+1} name :")
#         file.write(student_name+"\n")
#     print("names written succesfully")

# ==================================
# Task 2
# ==================================

# with open("student.txt","r") as file:
#     # data = file.readlines()
#     # print("".join(data).strip())
#     # print("lines",len(data))
#     count = 0
#     for line in file:
#         print(line.strip())
#         count+=1
#     print("lines",count)

# ==================================
# Task 3
# ==================================

# with open("student.txt", "a") as file:
#     for i in range(2):
#         name=input("Enter a name")
#         file.write(name.strip() + "\n")
#         print("2 new names of the students are successfully added")



# with open("numbers.txt","w") as file:
#     numbers = []
#     for i in range(5):
#         num = input("enter a number : ")
#         numbers.append(num)
#     file.write(",".join(numbers))

# print("="*20)
# with open("numbers.txt","r") as file:
#     numbers=file.read().split(",")
#     numbers=[float(num) for num in numbers]
#     sum = sum(numbers)
#     print("sum",sum)
#     print("avg",sum/len(numbers))
    # sum = 0
    # for num in numbers:
    #     print(num)
    #     sum+=num
    # print("sum of numbers : ",sum)
    # print("average of numbers : ",sum/len(numbers))



with open("story.txt") as file:
    content = file.read()
    print("characters : ", len(content))
    print("words : ", len(content.split()))
    print("lines : ", len(content.strip().split("\n")))
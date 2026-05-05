# fruits = ["apple", "banana", "cherry"]

# for x in fruits:
#     if "a" in x:
#         print(x)

# for i in range(1,10,2):
#     print(i)

# message = "Hello, World!"
# for character in message:
#     print(character)


# x=0
# while x < 5:
#     print(x)
#     x += 1

# for i in range(5):
#     print(i)

# for i in range(1, 4): # i = 3
#     for j in range(1, 4): # j = 1
#         # print(f"i={i},j={j}  ", end=" ")

#         if i == j:
#             print(1, end=" ")
#         else:
#             print(0, end=" ")
#     print()
# for i in range(5,0, -1):
#     print("*  " * i)

# for row in range(5):
#     for col in range(5):
#         if row == col:
#             print("*", end="  ")
#     print()


fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# bucket = [y for y in fruits if "a" in y]
# print(bucket)
# bucket = [fruit if "a" in fruit else "no" for fruit in fruits]
# print(bucket)

# numbers = [2,77,44,23,16,18]

# even_or_odd = ["even" if number % 2 == 0 else "odd" for number in numbers]
# print(even_or_odd)

# print(all([True, False, True])) # False
# print(any([True, False, True])) # True

num = int(input("Enter a number: "))
check_prime = True

if int(num**0.5) == num**0.5:
    check_prime = False
    print(f"{num} is not a prime number.")
    exit()
range_of_devisors = range(2, int(num**0.5)+1)
for i in range_of_devisors:
    if num % i == 0:
        check_prime = False
        break
if check_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# print(range(2, int(8**0.5) + 1), int(8**0.5))

# prime_numbers = [num for num in range(2,100) if all(num % divisor != 0 for divisor in range(2, int(num**0.5) + 1))]
# print(prime_numbers)
# upper_fruits = " ".join(fruits).upper().split()
# print(upper_fruits)

# upper_fruits = []

# for fruit in fruits:

#     upper_fruit = fruit.upper()
#     upper_fruits.append(upper_fruit)

# print(upper_fruits)
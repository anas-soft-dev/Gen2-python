# # def fun(a):
# #     a+=5
# #     a-=4
# #     print(a)
# #     b = input()
# #     return 10+5

# # sum = lambda a,b: a+b
# # multiply = lambda a,b:a*b
# # divide = lambda a,b:a/b
# # subtract = lambda a,b:a-b

# # print(sum(111,8))
# # print(sum(22,8))
# # print(multiply(22,8))
# # print(divide(22,8))


# def currency(amount,conversion):
#     converted_amount = conversion(amount)
#     print(converted_amount)

# def usd_to_pkr(amount):
#     return amount*300

# def usd_to_yen(amount):
#     return amount*30

# usd_to_pkr = lambda a: a*300
# currency(100, usd_to_pkr)
# currency(100, lambda a: a*30)
# x = lambda x:x*3*(5)
# print(x(5))


# def myfun(num):
#     return lambda a: a * num

# doubler = myfun(2)
# tripler = myfun(3)
# penta = myfun(5)
# hexa = myfun(6)
# print(doubler(5))
# print(doubler(10))
# print(tripler(10))
# print(hexa(10))

# def power(n):
#     return lambda a:a**n

# square = power(2)
# cube = power(3)
# power_4 = power(4)

# print(square(2))
# print(square(3))
# print(cube(2))
# print(cube(3))
# print(power_4(2))
# print(power_4(3))

# list1 = [1,2,3,4,5]
# new = list(map(lambda x:x*x, list1))
# cube = list(map(lambda x:x**3, list1))

# print(new)
# print(cube)


fruits = ["apple ","orrange","bnana","kiwi"]
fruits1 = ["red ","small","yellow","green"]


upper_case = map(lambda fruit,attribute: True, fruits, fruits1)

print(list(upper_case))
# for items in upper_case:
#     print(items)

numbers = range(11)

even_numbers = filter(lambda x: x%2!=0, numbers)

print(list(even_numbers))

print(list(filter(lambda x: "a" not in x, fruits)))
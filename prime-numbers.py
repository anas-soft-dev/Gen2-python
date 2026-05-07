a = [100 % devisors != 0 for devisors in range(2, int(100**0.5) + 1)]
print(all(a))


pyramid = 5
# for i in range(pyramid):
#     for j in range(pyramid):
#         if j <= i:
#             print("*", end="  ")
#     print()

# n = 5

# for i in range(n):
#     print(" " * i + "*" * (2 * (n - i) - 1))


# n = 5

# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))


for i in range(5):
    print(" "*(5-i-1) + "*" * ((i * 2) + 1))

for i in range(5):
    print(" "*(i) + "*" * ((5 - i) * 2 - 1))
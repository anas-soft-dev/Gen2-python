# fruits = ["apple", "banana", "cherry"]
# fruits2 = ["orange", "kiwi", "melon"]
# fruits = fruits2 = fruits + fruits2
# print(fruits)
# print(fruits2)  
# fruits.extend(fruits2) # fruits = fruits + fruits2
# fruits2.extend(fruits)
# print(fruits2)
# print("before update",fruits)

# fruits[1:3] = ["pineapple","blueberry"]
# print("after update",fruits)
# fruits.append("orange")
# print("after append",fruits)


# if 101 in fruits:
#     print("Yes, 'apple' is in the list.")
# else:
#     print("No, 'banana' is not in the list.")


# lists = list((1, 2, 3, 4, 5)) # [1,2,3,4,5]

# # print(type(lists))

# print(fruits[0:2]) # 1



# fruits = ("apple", "banana", "cherry")
# # fruits.append("1") # TypeError: 'tuple' object does not support item assignment
# fruits = list(fruits) # convert tuple to list
# fruits.append("orange") # now we can append to the list
# fruits = tuple(fruits) # convert back to tuple
# print(fruits, type(fruits))

# fruit = tuple(("orange",))
# print(fruit, type(fruit))
# print(fruits, type(fruits))


# set = {"apple", "banana", "cherry", "apple"}
# set2 = {"orange", "kiwi", "melon", "banana"}
# set.update(set2)
# print(set)


car = {
    "brand":"Ford Mustang",
    "model":"Mustang",
    "year":1964,
    "is_electric": False,
    "features": ["air conditioning", "power steering", "leather seats"]
}

car["model"] = "Mustang GT"
car["engine"] = "V8"

# car["features"].append("sunroof")
# print("brand",car["brand"])
# print("model",car["model"])
# print("year",car["year"])
# print("is_electric",car["is_electric"])
# print("Features",car["features"])

# print(car)

students = {
    "akt_first_1":{
        "name":"John Doe",
        "age": 20,
        "grade": "A",
        "marks": {
            "math": 95,
            "science": 90,
            "english": 92
        }
    },
    "akt_first_1":{
        "name":"John Doe",
        "age": 20,
        "grade": "A",
        "marks": {
            "math": 95,
            "science": 90,
            "english": 92
        }
    },
}

# print(students["akt_first_1"]["marks"].keys().values)


students = [
    {
        "name":"John Doe",
        "age": 20,
        "grade": "A",
        "marks": {
            "math": 95,
            "science": 90,
            "english": 92
        }
    },
    {
        "name":"Jane Smith",
        "age": 22,
        "grade": "B",
        "marks": {
            "math": 85,
            "science": 88,
            "english": 90
        }
    }
]

print(students[1]["marks"]["science"])
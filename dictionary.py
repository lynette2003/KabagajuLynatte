
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# number 1
print("Shoe size:", Shoes["size"])

#number 2
Shoes["brand"] = "Adidas"
print("After updating brand:", Shoes)

# number 3
Shoes["type"] = "sneakers"
print("After adding type:", Shoes)

# number 4
print("All keys:", list(Shoes.keys()))

#number 5
print("All values:", list(Shoes.values()))

#number 6
print("Is 'size' a key in Shoes?", "size" in Shoes)

# number 7
print("Looping through dictionary:")
for key in Shoes:
    print(key, ":", Shoes[key])

#number 8
Shoes.pop("color")
print("After removing color:", Shoes)

# number 9
Shoes.clear()
print("After clearing:", Shoes)

# number 10
my_dict = {
    "name": "Lynette",
    "course": "Software Engineering",
    "year": 2
}
my_dict_copy = my_dict.copy()
print("Original:", my_dict)
print("Copy:", my_dict_copy)

# number 11
students = {
    "student1": {
        "name": "Lynette",
        "age": 22
    },
    "student2": {
        "name": "Desire",
        "age": 21
    },
    "student3": {
        "name": "Mercy",
        "age": 23
    }
}
print("Nested dictionary:", students)
print("Student1 name:", students["student1"]["name"])
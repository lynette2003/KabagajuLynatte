#number 1
x=("samsung","iphone","techno","redmi")
print(x[0])

print(x[-2])

#number 2
phone_list= list(x)
phone_list[1]="itel"
x=tuple(phone_list)
print(x)

#number 3
phone_list.append("Huawei")
x=tuple(phone_list)
print("Add Huawei:",x)

#number 4
for phone in x:
    print(phone)

#number 5
phone_list.remove(phone_list[0])
x = tuple(phone_list)
print("After removing first item:", x)

#number 6
cities = tuple(("Kampala", "Gulu", "Mbarara", "Jinja", "Entebbe"))
print("Cities in Uganda:", cities)

#number 7
city1, city2, city3, city4, city5 = cities
print("Unpacked cities:", city1, city2, city3, city4, city5)

#number 8
print(cities[1:4])

#number 9
first_names = ("Lynette")
second_names = (" Kabagaju")
full_names = first_names + second_names
print("Joined names:", full_names)

#number 10
colors = ("red", "blue", "green")
colors_multiplied = colors * 3
print("Colors multiplied by 3:", colors_multiplied)

#number 11
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_of_8 = thistuple.count(8)
print("Number of times 8 appears:", count_of_8)
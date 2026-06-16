#      lists
#number 1
listnames=["Lynette","Desire","Mercy","Alba","Specy"]
name=listnames[1]
print(name)

#Number 2
listnames[0]="Phillipah"
print(listnames)

#number 3
listnames.append("Lyn")
print(listnames)

#number 4
listnames.insert(2,"Bathel")
print(listnames)

#number 5
name=listnames.remove("Alba")
print(listnames)

#number 6
name=listnames[-1]
print(name)

#number 7
numbers=[1,2,3,4,5,6,7]
print(numbers[2:5])

#number 8
countries=["Uganda","Algeria","Eygpt","Kenya","Tanzania"]
copy=countries.copy()
print(copy)

#number 9
for country in countries:
    print(country)
#number 10
animals = ["Dog", "Cat", "Elephant", "Lion", "Tiger"]

# Ascending order
animals.sort()
print(animals)

# Descending order
animals.sort(reverse=True)
print(animals)

#number 11

for animal in animals:
    if "a" in animal.lower():
        print(animal)

#number 12
firstname=["Lynette"]
lastname=["Kabagaju"]

mynames= firstname + lastname
print(mynames)

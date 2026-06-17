beverages={"berries juice","pespi","cocktail juice","milk","oreo milkshake"}
 #number 1
beverages=set(("berries juice","pespi","cocktail juice","milk","oreo milkshake"))
print(beverages)
 
 #number 2

beverages.update(["coffee","water"])
print(beverages)

mySet={"oven","kettle","microwave","refrigerator"}

#number 3

print("microwave" in mySet)

#number 4
mySet.remove("kettle")
print(mySet)

#number 5
for x in  mySet:
    print(x)

#number 6
mydevices = {"laptop", "phone", "tablet", "charger"}
mylist = ["keyboard", "mouse"]
mydevices.update(mylist)
print( mydevices)

#number 7
ages = {22}
first_names = {"Lynette"}
joined = ages.union(first_names)
print(joined)
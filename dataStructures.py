
#Lists are mutable ie. values can change
#Lists are ordered
myList=["Ridge","Joyce","David","Monah"]
print(myList[0])
myList2=[89,12,3,24,0,1,17,9,-3,-19]
myList2.sort()

#Tuples are immutable ie. values cannot change
#Tuples are ordered
myTuple=("Kenya","Tanzania","Uganda")
print(myTuple)
# myTuple[2]="South Sudan"

#Sets
fruits={"Oranges","Pineapple","Mangoes"}
print(fruits)

#Dictionaries
employees={"Name":"Ridge","Age":30,"Gender":"Male","Salary":200000}
print("Employee name :%s" %employees["Name"])
print("Employees age :%d" %employees["Age"])



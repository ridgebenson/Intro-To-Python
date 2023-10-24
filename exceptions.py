# name="Ridge"
# for i in name:
#     if(i != O):
#         print(i)

fruits=["Mangoes","Apples","Oranges"]
try:
    for i in range(5):
        print(f"The index and element from the list is {i,fruits[i]}")

except:
    print("Index out of range")

numbers=[3,4,5,6,7,]

if len(numbers)>3:
    raise Exception(f"Length must be less or equal to three but its {len(numbers)}")
def ridge():
    print("My name is Ridge Benson")
    print("This file is about functions")

ridge()

def getSum():
    num1=22
    num2=33
    sum=num1+num2

    return sum

print(f"The sum is {getSum()}")

def check_if_odd_or_even():
    theNumber=int(input("Enter the number to check whether odd or even:"))
    if theNumber%2==0:
        print(f"{theNumber} is an even number")
    else:
        print(f"{theNumber} is an odd number")
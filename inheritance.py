class Animal:
    def speaks(self):
        print("Animals Speaks")
class Cat(Animal):
    def meows(self):
        print("Cat Meows")
# Initialize an object
paka=Cat()
paka.meows()
paka.speaks()
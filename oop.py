class Cars:
    #A Constructor
    def __init__(self,type,color,model):
        self.type=type
        self.color=color
        self.model=model
        #A method

    def onyesha(self):
        print(f"I love {self.model} cars which is a {self.type} being {self.color}")

#Creating an object
myobj=Cars("Saloon","White","Toyota")
myobj.onyesha()
myobj2=Cars("G Wagon","Black","Mercedes")
myobj2.onyesha()

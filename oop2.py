class Students:
    def __init__(self,name,course,gender,age):
        self.name=name
        self.course=course
        self.gender=gender
        self.age=age

    def display(self):
        print("Name: %s \nCourse: %s \nGender: %s\n Age: %d"
              %(self.name,self.course,self.gender,self.age))

stud1=Students("Ridge Benson","BBIT","Male",22)
stud1.display()

stud2=Students("Joyce Njeri","BBIT","Female",18)
stud2.display()

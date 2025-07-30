#WAP to create student class that takes name and marks of 3 subjects as arguements in constructor, than create a method to print it
class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def getavg(self):
        sum=0
        for val in self.marks:
            sum += val
        print(self.name,sum/3)
        
s1= Student("Vartul", [87,90,98])
s1.getavg()


                
        
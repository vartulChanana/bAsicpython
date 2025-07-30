#all classes has a fn called init fn , it is always exceuted when the classs is being initiated , whether you write it or not
class Student:
    def __init__(self, name, marks):  
        self.name= name  
        self.marks=marks
        print("ADDING NEW STUDENTS IN THE DATABASE")

s1= Student("Hello",71)
print(s1.name,s1.marks)

#here self.name , is an instance variable , it is also called attribute. 
#self and name are parameter/arguemnets , we have to use self everytime 
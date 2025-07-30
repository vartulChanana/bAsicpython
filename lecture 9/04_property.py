class Marks:
    def __init__(self,chem ,phy,maths):
        self.chem=chem
        self.phy=phy
        self.maths=maths
        

    @property
    def percentage(self):
        return ((self.phy + self.chem + self.maths) / 3)

stu1=Marks(30,40,50)
print(stu1.percentage)

stu1.phy= 86
print(stu1.percentage)
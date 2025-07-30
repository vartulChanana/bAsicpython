class Names:
    name="anonymous"
    
    @classmethod #decorator
    def changename(cls,name):  #here we use cls to talk about that object ,
        cls.name=name 

p1= Names()
p1.changename("Vartul")
print(p1.name)
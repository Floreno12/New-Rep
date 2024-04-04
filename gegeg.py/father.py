class Animall:
    def __init__(self,name,age):
        self.name = name
        self.age = age


class Dog (Animall):
    def __init__(self, name,age):
        super().__init__(name,age)
        self.age = age

class Get (Animall):
    def __init__(self, name, age):
        super().__init__(name, age)


animall = Dog('Rass',12)
get = Get('Vai',13)
print (animall.name,animall.age )
print (get.name,get.age)



        
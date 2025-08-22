class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.life = True
        pass

    def eat(self):
        print(f"The animal {self.name} is eating") 

    def walk(self):  
        if not self.life:
            print(f"The animal {self.name} is dead and cannot walk")
            
        else:

            print(f"The animal {self.name} is walking")

    def sound(self):
        if not self.life:
            print(f"The animal {self.name} is dead and cannot make a sound")
            

class vertebrate(Animal):
    def __init__(self,name,age,vertebrate_type):
        super().__init__(name,age = True)
        self.vertebrate_type = vertebrate_type

class invertebrate(Animal):
    def __init__(self,name,age,invertebrate_type):
        super().__init__(name,age = True)
        self.invertebrate_type = invertebrate_type
           
animals = vertebrate("Lombriz", 10, "reptile")
animals_XL = invertebrate("Elephant", 25, "mamiferous")
animals.life = False
print(animals.life)
print(animals_XL.age)

animals.eat()
animals_XL.eat()

animals.walk()
animals_XL.walk()

animals.sound()
animals_XL.sound()
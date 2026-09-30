#Inheritance

#inheritance


#    class animals:
#     def show(self):
#         print("hello i am mayank")
# class human(animals):
#     def show(self):
#         print("hello mayank") 
# obj=human()
# obj.show()
        
# class intro:
#     def __init__(self, name):
#         self.name = name
       

#     def show(self):
#         print(f"hello your name is {self.name}")


# class name(intro):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
        
        
#     def display(self):
#         print(f"{self.name} ki age {self.age} hai")
            
# hello1=intro("mayank")
# hello1.show()

# hello2=intro("mamtu")
# hello2.show()
       
# intro1=name("mayank",20)
# intro1.display()

# intro2=name("mamtuu","3 mahine 21 din choti hai mayank se")
# intro2.display()







#multiple inheritance

# class Intro:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"your {self.name}")


# class Intro2:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show2(self):
#         print(f"your {self.name} and age is {self.age}")


# class Introduction(Intro, Intro2):
#     def __init__(self, name, age):
#         Intro.__init__(self, name)
#         Intro2.__init__(self, name, age)

#     def display(self):
#         print(f"your {self.name} and age is {self.age}")


# i = Introduction("mayank", 20)
# i.display()
    
                            



#miltilevel inheritace

# class factory1:
#     def __init__(self,material,cargo):
#         self.material = material
#         self.cargo = cargo
    
#     def show1(self):
#         print(f"material are{self.material} and cargo are{self.cargo}")    
        
# class factory2(factory1):
#     def __init__(self,material,cargo,colors): 
#         super().__init__(material,cargo)
#         self.colors = colors
        
#     def show2(self):
#             print(f"material are{self.material},cargo are {self.cargo} and colors of material is {self.colors}")
            
# class factory3(factory2):
#     def __init__(self,material,cargo,colors,worker): 
#         super().__init__(material,cargo,colors)
#         self.worker = worker 
    
#     def show3(self):
#                 print(f"material are{self.material},cargo are {self.cargo} and colors of material is {self.material},{self.worker} work in this factory3")    
                                                        
# f3 = factory3("steel", "containers", "grey", 15)
# f3.show1()
# f3.show2()
# f3.show3()                                                        



#polymorphism

# class Factory1:
#     def __init__(self, material, cargo):
#         self.material = material
#         self.cargo = cargo

#     def show(self):
#         print(f"material are {self.material} and cargo are {self.cargo}")


# class Factory2(Factory1):
#     def __init__(self, material, cargo, colors):
#         super().__init__(material, cargo)
#         self.colors = colors

#     def show(self):
#         super().show()
#         print(f"colors of material is {self.colors}")

# class Factory3(Factory2):
#     def __init__(self, material, cargo, colors, worker):
#         super().__init__(material, cargo, colors)
#         self.worker = worker

#     def show(self):
#         super().show()
#         print(f"{self.worker} work in this factory3")


# f1 = Factory1("wood", "boxes")
# f2 = Factory2("plastic", "bottles", "blue")
# f3 = Factory3("steel", "containers", "grey", 15)

# f1.show()

# f2.show()

# f3.show()



#encapsulation

# class factory:
#     __a ="mayank"
#     def show(self):
#         print(f"{factory.__a} is owner of factory")
       
       
# obj=factory()
# obj.show() 



#abstraction


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        print(f"perimeter of square is {4 * self.side}")

    def area(self):
        print(f"area of square is {self.side ** 2}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        print(f"perimeter of circle is {2 * 3.14 * self.radius}")

    def area(self):
        print(f"area of circle is {3.14 * self.radius ** 2}")



sq = Square(5)
sq.perimeter()
sq.area()


c = Circle(3)
c.perimeter()
c.area()
                  
         
        
class car:
    def __init__(self,brand,colour):
     self.brand = brand
     self.colour = colour
    def start(self):
        print(f"{self.brand} {self.colour} is starting vroom!")

car1=car("honda","red")
car2=car("toyota","blue")
car3=car("tesla","white")
car1.start()
car2.start()
car3.start()
print(car3.brand)

# class car:
#     #attributes
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#     def start(self):
#         print(f"{self.color} {self.brand} car is starting")
# car1=car("Toyota", "Red")
# car2=car("Honda", "Blue")
# car3=car("Ford", "Black")
# car1.start()
# car2.start()
# car3.start()
# print(car3.brand)

        



class rectangle:
   def __init__(self,length,width):
      self.length = length
      self.width = width
      def area(self):
         print(self.length * self.width)
      def perimeter(self):
         print(2*self.length + 2*self.width)

rect = rectangle(12,2)
rect.area()
rect.perimeter()
print(rect.area)



         
     
       


      
   
        
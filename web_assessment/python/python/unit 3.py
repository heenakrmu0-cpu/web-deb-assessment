# class animal:                                              #parent class
#     def __init__(self,name):
#         self.name = name
#         def sound(self):
#             return"..."
# class dog(animal):
#     def sound(self):
#         return "woof!"
# class cat(animal):
#     def sound(self):
#         return "meow!" 
# class bird(animal):
#     def sound(self):
#         return "chirp!"
# animals=[dog("rex"),cat("milo"),bird("tweety")]
# for a in animals:
#     print(f"{a.name} says {a.sound()}")              #polymorphism in action





# class shape:
#     def area(self):
#         return 0
# class square:
#     def __init__(self,side):
#         self.side = side
#         def area(self):
#             return self.side**2
# s1 = square(4)
# print(s1.area())













# class circle:
#     def __init__(self, radius):
#         self.radius =radius
#     def area(self):
#             print(3.14 * self.radius * self.radius)
#     def circumference(self):
#             print(2 * 3.14 * self.radius)
# C = circle(10)
# C.area()
# C.circumference()





# class circle:
#      def __init__(self,radius):
#           self.radius = radius
          
#      def area(self):
#           print(3.14 * self.radius * self.radius)
# c = circle(5)
# c.area()






# class rectangle:
#       def __init__(self,length,breadth):
#           self.length = length
#           self.breadth = breadth
#       def area(self):
#           print(self.length + self.breadth)
# L= rectangle(3,4)
# L.area()



class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        print (self.length * self.breadth)
    def perimeter(self):
        print(2 * (self.length + self.breadth))
L=rectangle(10, 20)
L.area()
L.perimeter()




class student:
     school_name = "Green Valley Public School"              #class variable
     total_student = 0                                       #class variable (counter)

     def __init__(self, name,grade,section="A"):
          self.name = name               #instance variable
          self.grade = grade             #instance variable
          self.section = section         #instance variable,has a default
student.total_student+= 1
def introduce(self):
     print(f"hi i am {self.name} from {self.school_name}"
           f"grade {self.grade} - {self.section}")

     

s1 = student("Heena",15)
s2 = student("Rohan",14,"B")
s1.introduce()
s2.intr900-*oduce()
print( student.total_students)






     
          


          





      







    
        

    

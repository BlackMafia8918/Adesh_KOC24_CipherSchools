#Code 1

"""
class details:
    def __init__(self):
        self.__id="<no id>"
        self.__name="<no name>"
        self.__gender="<no gender>"
    def setdata(self):
        self.__id=id
        self.__name=name
        self.__gender=gender
    def showdata(self):
        print("id:",self.__id)
        print("name:",self.__name)
        print("gender:",self.__gender)
    def _init_(self):
        self.__company="<No Company>"
        self.__dept="<No Dept>"
    def setEmployee(self,id,name,gender,comp,dept):
        self.setData(id,name,gender)
        self.__company=comp
        self.__dept=dept
    def showEmployee(self):
        self.showData()
        print("Company: ", self.__company)
        print("Department: ", self.__dept)
"""       
        
        
#Code 2 is important:
"""
        
class Parent:
    def func1(self):
        print("this is function of parent class")

class Child1(Parent):
    def func2(self):
        print("this is function of child 1 class")

class Child2(Parent):
    def func3(self):
        print("this is function of child2 class")
        
c1 = Child1()
c1.func2()
c1.func1()

c2 = Child2()
c2.func3()
c2.func1()
"""




"""
1. Create a class Student with two instance attributes student_name and student_marks. Create two member functions
a. print - to print the information of student (name and marks)
b. passOrFail - based on the marks, check whether student is pass or fail (pass if marks are greater than 33)


2. Create two derived class A and B inheriting from a base class C, then A class itself is base class for class D.

3. Create a class named Shape with function that prints "This is a shape"
Create another class named Polygon inheriting the Shape class with function that prints "Polygon is a shape"
Create two other classes Rectangle and Triangle inheriting from Polygon class having functions that say
"Rectangle is a polygon" and "Triangle is a polygon"

"""


#Solution 1 :
"""

class Student:
    def __init__(self, name, marks):
        self.student_name = name
        self.student_marks = marks

    def print(self):
        print(self.student_name, self.student_marks)

    def passOrFail(self):
        if self.student_marks > 33:
            print("student is passed")
        else:
            print("student is failed")


s=Student("Ayushi", 25)
s.print()
s.passOrFail()
"""




#Solution 2:
"""

class C:
    def __init__(self):
        print("Base Class C constructor called")

class A(C):
    def __init__(self):
        C.__init__(self)
        print("A derived class constructor called")

class B(C):
    def __init__(self):
        C.__init__(self)
        print("B derived class constructor called")

a=A()
b=B()
"""


#Solution 3:
"""

class Shape:
    def print1(self):
        print("This is a shape")

class Polygon(Shape):
    def print2(self):
        print("Polygon is a shape")

class Rectangle(Polygon):
    def print3(self):
        print("Rectangle is a Polygon")

class Triangle(Polygon):
    def print4(self):
        print("Triangle is a Polygon")

r=Rectangle()
r.print3()
r.print2()
r.print1()

t=Triangle()
t.print4()
t.print2()
t.print1()

"""


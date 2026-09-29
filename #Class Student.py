#Class Student

class Student:
    print("_____<<Student class>>_____")

    def __init__(self, name, age, physics, chemistry, math, collage_name):
        self.names = name
        self.age = age
        self.collage_name = collage_name
        self.physics = physics
        self.chemistry = chemistry
        self.math = math

        print("_____<<", self.collage_name, ">>_____")

        self.percentage = (physics + chemistry + math) / 300 * 100
        self.average = (physics + chemistry + math) / 3

    def display_student_details(self):
        print("____<<Student details>>____")
        print("Student name is", self.names)
        print("Student age is", self.age)
        print("College name is", self.collage_name)

    def display_student_marks(self):
        print("____<<Student marks>>____")
        print("--Physics marks:", self.physics, "out of 100--")
        print("--Chemistry marks:", self.chemistry, "out of 100--")
        print("--Math marks:", self.math, "out of 100--")
        print("--Student percentage:", round(self.percentage, 2),"%--")
        print("--Average marks:", round(self.average, 2),"--")


f = input("--<<Enter college name: ")
a = input("--<<Enter student name: ")
b = int(input("--<<Enter student age: "))
print("__<<Enter student marks out of 100>>__")
c = int(input("--<<Enter physics marks: "))
d = int(input("--<<Enter chemistry marks: "))
e = int(input("--<<Enter math marks: "))
student1 = Student(a, b, c, d, e, f)
print("_____<<Student 1>>_____")
student1.display_student_details()
student1.display_student_marks()

print("_____<<Student 2>>_____")
p = input("--<<Enter student name: ")
q = int(input("--<<Enter student age: "))
print("__<<Enter student marks out of 100>>__")
r = int(input("--<<Enter physics marks: "))
s = int(input("--<<Enter chemistry marks: "))
t = int(input("--<<Enter math marks: "))
student2 = Student(p, q, r, s, t, f)
print("_____<<Student 2>>_____")
student2.display_student_details()
student2.display_student_marks()

print("_____<<End of program>>_____")
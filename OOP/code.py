#  __init__ is equal to constructor
# and self is equal to this

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def grade_summary(self):
        return self

student = Student(name='Felipe', grades=(10, 9, 8, 7, 6))

# print(student.average())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

person = Person('Bob', 25)

print(person)

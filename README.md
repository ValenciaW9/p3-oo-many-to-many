# Many-to-many Object Relationships

## Learning Goals

- Describe many-to-many relationships.
- Explain why many-to-many relationships are important.

***

## Key Vocab

- **Class**: a bundle of data and functionality. Can be copied and modified to
accomplish a wide variety of programming tasks.
- **Object**: the more common name for an instance. The two can usually be used
interchangeably.
- **Object-Oriented Programming**: programming that is oriented around data
(made mobile and changeable in **objects**) rather than functionality. Python
is an object-oriented programming language.
- **Function**: a series of steps that create, transform, and move data.
- **Method**: a function that is defined inside of a class.

***

## Introduction

A many-to-many relationship refers to a relationship where multiple instances of one class (Class A) are associated with multiple instances of another class (Class B), and vice versa. In other words, each object of Class A can be related to multiple objects of Class B, and each object of Class B can be related to multiple objects of Class A.


When working with many-to-many relationships, it is important to consider whether or not to use an intermediary class. An intermediary class is a class that sits between two other classes in a many-to-many relationship and provides additional information about the relationship.


## Many-to-many without intermediary class

An approach to many-to-many relationships without using an intermediary class is to use a list to store references to the related objects.

Lets look at an example where we use a `Parent` and `Child` class to demonstrate a many-to-many relationship.
A child can have multiple parents and a parent can have multiple children.

```py
class Parent:
    def __init__(self):
        self.children = []
    
    def add_child(self, child):
        if isinstance(child, Child):
            self.children.append(child)
        else:
            raise ValueError("Child must be an instance of the Child class.")
    
    def get_children(self):
        return self.children

```

```py
class Child:
    def __init__(self):
        self.parents = []
    
    def add_parent(self, parent):
        if isinstance(parent, Parent):
            self.parents.append(parent)
        else:
            raise ValueError("Parent must be an instance of the Parent class.")
    
    def get_parents(self):
        return self.parents

```

```py
parent1 = Parent()
parent2 = Parent()
child1 = Child()
child2 = Child()

parent1.add_child(child1)
parent2.add_child(child1)
child1.add_parent(parent1)
child1.add_parent(parent2)

```

This approach can be simpler than using an intermediary class, but it can also be less flexible if additional information needs to be stored about the relationship.

***

## Many-to-many with an intermediary class

In this example, we'll create a many-to-many relationship between two classes `Student` and `Course`, using a third intermediary class called `Enrollment`.

```py
class Student:
    def __init__(self, name):
        self.__name = name
        self.__enrollments = []

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self.__enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self.__enrollments.copy()

class Course:
    def __init__(self, title):
        self.__title = title
        self.__enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self.__enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self.__enrollments.copy()

class Enrollment:
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.__student = student
            self.__course = course
            self.__enrollment_date = datetime.now()
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_student(self):
        return self.__student

    def get_course(self):
        return self.__course

    def get_enrollment_date(self):
        return self.__enrollment_date


```

Using an intermediary class you can now store the date when a student enrolls in a course as part of the Enrollment object, which is specific to the relationship between the student and the course.

***

## Conclusion

In conclusion, implementing many-to-many relationships in Object-Oriented Programming can be achieved with or without an intermediary class. We want to use an intermediary class when we need to store some outside information about the relationship. When deciding whether to use an intermediary class for many-to-many relationships, consider the trade offs of each approach.

***

## Resources

- [Python classes](https://docs.python.org/3/tutorial/classes.html)
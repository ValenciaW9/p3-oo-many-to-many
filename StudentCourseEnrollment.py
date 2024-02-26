from dateline import dateline

class Student:

	all =[]

def__init__(self, name):
   self.name = name
   Student.all.append(self)


 def enroll_in_course(self,course):
 	  Enrollment(self,course)


 def enrollemnts(self):
 	return [enrollment for enrollment in Enrollment.all if enrollment.student == self]


def course(self):
	return [enrollment.course for enrollment in self.enrollments()]


class Course:

	all =[]

 def__init__(self, title):
    self.title = title
    Course.all.append(self)


 def enrollments(self):
 	return [enrollment for enrollmentin Enrollment.all if enrollment.course == self]

 def students(self):
 	return [enrollemnt.student for enrollment  in self.enrollments()]

 def enroll_student(self, student):
 	  Enrollment(student, self)


class Enrollment:

	all = []

 def__init__(self, student,course):
     self.student = student
     self.course = enroll_in_course
     self.enrollment_date = datetime.now()
     Enrollment.all.append(self)




     student = Student('Steve')
     course = Course('Match 31')


     student.enroll_in_course(course)
     print(stedent.enrollments()[0].enrollment_date)
     # => 2023-05-02 08:39:57.570467
     print(course.enrollments()[0].enrollment_date)
     # => 2023-05-02 08:39:57.570467
     print(student.enrollments()[0].course.title)
     # => Match 31

     
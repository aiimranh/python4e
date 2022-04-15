# basic class declaration
class student:
    # class attribute

    # @classmethod

    # @staticmethod

	# __init__() method
	def __init__(self,name,age,grade):
        # instance attibutes
		self.name = name
		self.age = age
		self.grade = grade
	
	def get_grade(self):
		return self.grade

class course:
	def __init__(self,name,max_students):
		self.name = name
		self.max_students = max_students
		self.students = [] # list of object instances

	def add_students(self,student):
		if len(self.students) < self.max_students:
			self.students.append(student)
	
	def avg(self):
		value = 0
		for grad in self.students: # grad equal to s1/s2/s3
			value += grad.get_grade()
		
		return value/len(self.students)

s1 = student('rr',19,45)
s2 = student('ii',19,66)
s3 = student('tt',19,77)

cour = course('ece3109',3)

cour.add_students(s1)
cour.add_students(s2)
cour.add_students(s3)

print('{:.3f}'.format(cour.avg()))
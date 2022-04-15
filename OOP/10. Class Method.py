from unicodedata import name


class person:
	# class attribute
	num = 0
	
	def __init__(self,name):
		# method attribute
		self.name = name
		person.add_person()

	@classmethod # to denote the class method
	def number(cls): # 
		return cls.num

	@classmethod
	def add_person(cls):
		cls.num += 1

# access the class attribute
p = person("imran")
print(person.number())

# modifying the class attribute
person.num = 0
print(person.number())
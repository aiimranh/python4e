from unicodedata import name


class person:
	# class attribute
	num = 0
	
	def __init__(self,name):
		# method attribute
		self.name = name
		person.num += 1

# access the class attribute
print(person.num)

# class attribute can be access using object
p = person("imran")
print(p.num)

# modifying the class attribute
person.num = 10
print(person.num)
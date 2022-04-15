# simple inherent class  2
class pet:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	
	def show(self):
		print(f"I am {self.name} and I am {self.age} years old.")

class cat(pet):
	def __init__(self,name,age,color):
		super().__init__(name,age)
		self.color = color

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old. I am {self.color}.")

	def speak(self):
		print("meow")

class dog(pet):
	def speak(self):
		print("geow")

# parent / super class
p = pet("tim",3)
p.show()

print()
# child class 1
c = cat("bill",2,"gray")
c.speak()
c.show()    # if same method is declare in parent and child class both.
# then, child class is called.

print()
# child class 2
d = dog("nil",2)
d.speak()
d.show()
class human:
	def __init__(self):
		super().__init__()
		print("human")

class citizen:
	def __init__(self):
		super().__init__()
		print("citizen")

class student(human,citizen):
	def __init__(self):
		super().__init__()
		print("student")

x = student()
# basic class declaration
class human:
	# class attribute

    # @classmethod

    # @staticmethod

	# __init__() method
    def __init__(self,name,age,height):
		# instance attibutes
        self.name = name
        self.age = age
        self.height = height
    
	# another method
    def display(self):
        print(self.name,self.age,self.height)


# initialization method to data store
h = human('imran',22,5.9)

# print the data - method 1 (invidually)
print(h.name,end=' ')
print(h.age,end=' ')
print(h.height)

# print the data -method 2 (at a once)
h.display()
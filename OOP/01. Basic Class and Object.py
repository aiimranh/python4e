# basic class declaration
class human:
	# class attribute 

    # @classmethod

    # @staticmethod

	# method
    def properties(self,name,age,height):
		# method instances
        self.name = name
        self.age = age
        self.height = height
    
	# another method
    def display(self):
        print(self.name,self.age,self.height)


# initialization object of the class
h1 = human()
h2 = human()

# data storing - method 1
h1.name = "imran"
h1.age = 22
h1.height = 5.8

# data storing - method 2
h2.properties("imran",22,5.9)

# print the data - method 1 (invidually)
print(h1.name,end=' ')
print(h1.age,end=' ')
print(h1.height)

# print the data -method 2 (at a once)
h2.display()
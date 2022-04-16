# base class
class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"

    def show(self):
        # Accessing protected member in child class
        print("Working on project :", self._project)

# initialization of class using an object.
c = Company()

# public method to show the protected data.
c.show()

# Direct access protected data member
print('Project:', c._project)
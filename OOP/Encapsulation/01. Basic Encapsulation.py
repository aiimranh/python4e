class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name # public
        self._salary = salary   # protected
        self.__project = project    # private

    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self._salary)

    # method
    def work(self):
        print(self.name, 'is working on', self.__project)

# creating object of a class
emp = Employee('Jessa', 8000, 'NLP')

# calling public method of the class
emp.show()
emp.work()
class human:
    def __init__(self,name: str,age: int,height: float):

        # run the validation of the argument
        assert age >= 0 , f'age {age} is below zero'
        assert height >= 0, f'height {height} is below zero'

        # assign to seklf object
        self.name = name
        self.age = age
        self.height = height

    def talk(self):
        print("Hi, I'm",self.name,".I'm",self.age,"years old. I'm",self.height,"ft tall. Isn't it enough for a basketball player?")

x = human("imran",34,-5.6)
x.talk()
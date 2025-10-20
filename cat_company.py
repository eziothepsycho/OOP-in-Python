class CatEmployee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
    
    def work(self):
        print(f"{self.name} is working hard... Meow!")

    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, position = {self.position}, salary = {self.salary}"
        return information
    
    @staticmethod
    def bonus(years):
        if years < 1: 
            return 1000
        elif years < 3:
            return 3000
        else:
            return 5000

class FrontEndCat(CatEmployee):
    def __init__(self, name, age, position, salary, tool):
        super().__init__(name, age, position, salary)
        self.tool = tool
    
    def work(self):
        print(f"{self.name} is designing webpage using {self.tool}")

class BackEndCat(CatEmployee):
    def __init__(self, name, age, position, salary, language):
        super().__init__(name, age, position, salary)
        self.language = language

    def work(self):
        print(f"{self.name} is coding in {self.language}")

cats = [FrontEndCat("Bucky", 3, "FrontEnd-Dev", 4000, "Tailwind"),
        BackEndCat("Puti", 1, "BackEnd-Dev", 6000, "Python")]

def catslist(cats):
    for cat in cats:
        print(cat)
        cat.work()
        print("Bonus:", CatEmployee.bonus(cat.age))
        print()

catslist(cats)
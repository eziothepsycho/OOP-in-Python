#Parent Class
class Cats:
    def __init__(self, name, age, color, salary):
        self.name = name
        self.age = age
        self.color = color
        self.salary = salary

    def work(self):
        print(f"{self.name} is working... Meow!")

#Child Class
class FrontEnd(Cats):
    def __init__(self, name, age, color, salary, level):
        #this line of cdde is inhereting the parent class
        super().__init__(name, age, color, salary)
        self.level = level

    def design(self):
        print(f"{self.name} is designing... Meow!")
    def work(self):
        print(f"{self.name} is drawing... Meow!")

class BackEnd(Cats):
    def __init__(self, name, age, color, salary, level):
        #this line of cdde is inhereting the parent class
        super().__init__(name, age, color, salary)
        self.level = level

    def debugging(self):
        print(f"{self.name} is debugging... Meow!")
    def work(self):
        print(f"{self.name} is coding... Meow!")

fEnd = FrontEnd("Kaiden", 19, "Orange", 5000, "Junior")
#fEnd.work()

bEnd = BackEnd("Mickey", 21, "Black", 9000, "Senior")
#bEnd.work()

#Polymorphism
employees = [FrontEnd("Kaiden", 19, "Orange", 5000, "Junior"),
             BackEnd("Mickey", 21, "Black", 9000, "Senior")]

def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)
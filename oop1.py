class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    #instance method
    def meow(self):
        print(f"\n{self.name} says Meow!")

    def information(self):
        information = f"name = {self.name}, age = {self.age}, color = {self.color}"
        return information
    
    #dunder method
    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, color = {self.color}"
        return information
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    @staticmethod
    def salary(age):
        if age < 1:
            return 7000
        elif age > 3:
            return 9000
        else:
            return 8000
#instance
cat1 = Cat("Bucky", 3, "Black")
cat2 = Cat("Puti", 1, "White")

print(f"\nThe name of my cat is {cat1.name} and his age is {cat1.age} and the color of his fur is {cat1.color}")
print(f"The name of my cat is {cat2.name} and his age is {cat2.age} and the color of his fur is {cat2.color}")

cat1.meow()
cat2.meow()

print(cat1)
print(cat2)

print(cat1.salary(3))
print(Cat.salary(3))
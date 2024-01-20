class Dog:
    # An example class which models a dog

    def __init__(self, name, age) -> None:
        self.name = name.title()
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} has rolled over")

bailey = Dog('bailey', 7)

bailey.sit()
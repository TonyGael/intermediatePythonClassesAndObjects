class Person:

    amount = 0  # this would be a global variable

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1 #  Person refers to yhe hole class, instead, self would be avery instance created

    def __del__(self):
        Person.amount -= 1
        # print(f'Object {self.name} deleted!')

    # using string format with placeholders
    def __str__(self):
        return "Name: {}, Age: {}, Height: {}.".format(self.name, self.age, self.height)

    def get_older(years):
        self.age += years


person_1 = Person("Tony", 38, 170)
print(person_1.name)
print(person_1.age)
print(person_1.height)

# We can change the values
person_1.name = "Gael"
person_1.height = 190

print("---------")
print(person_1.name)
print(person_1.height)

print(person_1)  # we get all the values
del person_1

person_2 = Person("Marylin", 50, 170)
print(person_2)

print(Person.amount)

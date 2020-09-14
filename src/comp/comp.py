# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
# a = [person.name for person in humans if person.name[0] == 'D']
for human in humans:
    # can also be written as: if human.name[0] == "D":
    if human.name.startswith("D"):
        a.append(human.name)
print(a)
print("\n\n-------------------------------------------\n\n")

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
# b = [person.name for person in humans if person.name[-1] == 'e']
for human in humans:
    # can also be written as: if human.name.endswith("e"):
    if human.name[-1] == "e":
        b.append(human.name)
print(b)
print("\n\n-------------------------------------------\n\n")

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
# c = [person.name for person in humans if person.name[0] >= 'C' and person.name[0] <= 'G']
letter_range = ("C", "D", "E", "F", "G")
for human in humans:
    if human.name.startswith(letter_range):
        c.append(human.name)
print(c)
print("\n\n-------------------------------------------\n\n")

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
# d = [person.age + 10 for person in humans]
for human in humans:
    newAge = human.age + 10
    d.append([human.name, newAge])
for item in d:
    print(item)
print("\n\n-------------------------------------------\n\n")

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
# e = [f'{person.name}-{person.age}' for person in humans]
for human in humans:
    nameFormat = f"{human.name}-{human.age}"
    e.append(nameFormat)
for item in e:
    print(item)
print("\n\n-------------------------------------------\n\n")

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
# f = [(person.name, person.age) for person in humans if person.age >= 27 and person.age <=32]
for human in humans:
    if human.age >= 27 and human.age <= 32:
        f.append((human.name, human.age))
for item in f:
    print(item)
print("\n\n-------------------------------------------\n\n")

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
# g = [Human(person.name.upper(), person.age + 5) for person in humans]
for human in humans:
    nameUppercase = human.name.upper()
    newAge = human.age + 5
    g.append((nameUppercase, newAge))
print("humans = [")
for item in g:
    print(f"\tHuman{item}")
print("]")
print("\n\n-------------------------------------------\n\n")

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
h = []
# h = [math.sqrt(person.age) for person in humans]
for human in humans:
    squareRoot = math.sqrt(human.age)
    h.append([f"The square root of {human.age} is {squareRoot}"])
for item in h:
    print(item)

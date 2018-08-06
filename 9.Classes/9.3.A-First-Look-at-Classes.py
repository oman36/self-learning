class Dog:

    tricks = []

    def __init__(self, name):
        self.name = name
        self.safe_tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)
        self.safe_tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
# ['roll over', 'play dead']
print(d.safe_tricks)
# ['roll over']

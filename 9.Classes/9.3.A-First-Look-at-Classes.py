class Dog:

    tricks = []
    reinited_tricks = []
    immutable_var = 'default'

    def __init__(self, name):
        self.name = name
        self.safe_tricks = []
        self.reinited_tricks = []
        self.immutable_var += f' [{name}]'

    def add_trick(self, trick):
        self.tricks.append(trick)
        self.reinited_tricks.append(trick)
        self.safe_tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
# ['roll over', 'play dead']

print(d.safe_tricks)
# ['roll over']
print(d.reinited_tricks)
# ['roll over']

print(d.immutable_var)
# default [Fido]
print(e.immutable_var)
# default [Buddy]

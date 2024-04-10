def greeting1():
    return "Booya!"

def greeting2():
    return "Hey there, partner!"

class Greeting:
    def __init__(self, greetings):
        self.greetings = greetings
    
    def greet(self):
        for greet in self.greetings:
            print(greet())

name = 'MyClass'
version = 1.0

'double_value': lambda self: None  # Placeholder method body

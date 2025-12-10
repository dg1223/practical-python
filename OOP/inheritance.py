class Parent:
    def __init__(self, my_string=None):
        if my_string:
            print(my_string)
        else:
            print("Parent constructor.")

    def _print(self):
        print("I am a Parent class")

# Inheritance
class Child(Parent):
    def __init__(self):
        super().__init__("Calling parent constructor from child class.")
        print("Child constructor")

    def _print(self):
        super()._print()  # calls _print() from Parent class
        print("I am a Child class")

child = Child()
child._print()

parent = Parent()
parent._print()
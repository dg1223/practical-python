class DrawingObject:
    def draw(self):
        print("I'm just a generic drawing object.")

class Line:
    def draw(self):
        print("I'm a line.")

class Circle:
    def draw(self):
        print("I'm a circle.")

class Square:
    def draw(self):
        print("I'm a square.")

objects = [DrawingObject(), Line(), Circle(), Square()]

for object in objects:
    object.draw()
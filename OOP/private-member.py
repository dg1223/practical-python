class Rectangle:
    def __init__(self, width, height):
        self.publicwidth = width
        self._height = height
        self.__privateheight = 0

rect = Rectangle(12, 10)
print(rect.publicwidth)
print(rect._height)
print(rect.__privateheight)
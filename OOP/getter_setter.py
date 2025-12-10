class Rectangle:
    # width and height not passed as class arguments
    def __init__(self):
        self._width = 0
        self._height = 0

    ''' Getters '''
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    ''' Setters: We can use the same method names'''
    # # @width.setter
    def width(self, value):
        self._width = value

    # # @height.setter
    def height(self, value):
        self._height = value

rect = Rectangle()
rect.width = 1
rect.height = 3
print(rect.width, rect.height)
class Engine2D:
    def __init__(self):
        self.canvas = []
        self.color = 'black'
        self.drawn_shapes = []

    def add_shape(self, shape):
        self.canvas.append(shape)

    def change_color(self, color):
        self.color = color

    def draw(self):
        for shape in self.canvas:
            shape_str = f"Drawing {shape.name} with color {self.color}: {shape}"
            self.drawn_shapes.append(shape_str)
            print(shape_str)
        self.canvas = []
        return self.drawn_shapes

class Circle:
    def __init__(self, center_x, center_y, radius, color = 'black'):
        self.name = 'Circle'
        self.centerX = center_x
        self.centerY = center_y
        self.radius = radius
        self.color = color

    def __repr__(self):
        return f"({self.centerX}, {self.centerY}) with radius {self.radius}"

    def draw(self):
        print(f"Drawing {self.name} with color {self.color}: {self}")


class Triangle:
    def __init__(self, vertex1, vertex2, vertex3, color='black'):
        self.name = 'Triangle'
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3
        self.color = color

    def __repr__(self):
        return f"({self.vertex1[0]}, {self.vertex1[1]}), ({self.vertex2[0]}, {self.vertex2[1]}), ({self.vertex3[0]}, {self.vertex3[1]})"

    def draw(self):
        print(f"Drawing {self.name} with color {self.color}: {self}")


class Rectangle:
    def __init__(self, topleft, width, height, color='black'):
        self.name = 'Rectangle'
        self.topleft = topleft
        self.width = width
        self.height = height
        self.color = color

    def __repr__(self):
        return f"({self.topleft[0]}, {self.topleft[1]}) with width {self.width} and height {self.height}"

    def draw(self):
        print(f"Drawing {self.name} with color {self.color}: {self}")
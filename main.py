# This is a sample Python script.
import yaml
import os
import sys
from math import pi
import turtle

turtle.tracer(False)

#### classes

class Circle:
    def __init__(self, radius, fill="red", stroke = "black", at=(0,0)):
        self._radius = radius  # private properties
        self._fill = fill
        self._stroke = stroke
        self._at = at

    @property
    def radius(self):
        return self._radius # made the property read only

    def calculate_area(self):
        """ Calculate the area"""
        return pi * self._radius ** 2

    @property
    def area(self):
        return self.calculate_area() # protect area function

    def __len__(self):
        return int(2 * pi * self._radius)

    def __call__(self):
        return "I am a circle"

    def __repr__(self):
        return f"Circle({self._radius}, fill = {self._fill}, stroke = {self._stroke})"

    def __str__(self):
        string = yaml.dump({
            'circle' : {
                'radius' : self._radius,
                'fill' : self._fill,
                'stroke' : self._stroke,
                'at' : self._at
            }
        })
        return string
    def draw(self, pen):
        """Draw a circle"""
        if pen.isdown():
            pen.up()
        pen.pencolor(self._stroke)
        pen.fillcolor(self._fill)
        pen.goto(*self._at)
        pen.down()
        pen.begin_fill()
        pen.pencolor(self._stroke)
        pen.fillcolor(self._fill)
        pen.circle(self._radius)
        pen.end_fill()
        pen.up()

    @classmethod
    def from_yaml(cls, string): # create a circle from YAML string
        circle_dict = yaml.load(string, Loader = yaml.Loader)['circle'] # load the YAML string
        print(circle_dict)
        obj = cls(circle_dict['radius'], fill=circle_dict['fill'], stroke=circle_dict['stroke'], at=circle_dict['at'])
        return obj


class Quadrilater:
    def __init__(self, width, height, fill = "grey", stroke = "red", at=(0,0)):
        self._width = width
        self._height = height
        self._fill = fill
        self._stroke = stroke
        self._at = at

    def calculate_area(self):
        """ Calculate the area"""
        return self._width * self._height

    def __len__(self):
        return int((2*self._width)+(2*self._height))

    def __call__(self):
        return "I am a quadrilater"

    def __repr__(self):
        return f"Quadrilater({self._width}, {self._height}, fill = {self._fill}, stroke = {self._stroke})"

    def __str__(self):
        string = yaml.dump({
            'quadrilater' : {
                'width' : self._width,
                'height' : self._height,
                'fill' : self._fill,
                'stroke' : self._stroke,
                'at' : self._at
            }
        })
        return string

    @property
    def left(self):
        return self._at[0] - (self._width/2)

    @property
    def top(self):
        return self._at[1] + (self._height/2)

    @property
    def right(self):
        return self._at[0] + (self._width/2)

    @property
    def bottom(self):
        return self._at[1] - (self._height/2)

    @property
    def vertices(self):
        """starting from top left and then clockwise"""
        return[
            (self.left, self.top),
            (self.left, self.bottom),
            (self.right, self.bottom),
            (self.right, self.top)
        ]

    def draw(self, pen, *args, **kwargs):
        pen.pencolor(self._stroke)
        pen.fillcolor(self._fill)
        pen.up()
        pen.goto(self.left, self.top)
        pen.down()
        pen.begin_fill()
        pen.goto(self.left, self.bottom)
        pen.goto(self.right, self.bottom)
        pen.goto(self.right, self.top)
        pen.goto(self.left, self.top)
        pen.up()
        pen.end_fill()

class Canvas(turtle.TurtleScreen):
    def __init__(self, width, height, bg="grey"):
        self._cv = turtle.getcanvas()
        super().__init__(self._cv) # super is a special function to refeal to the title class (canvas)
        self.screensize(width, height, bg=bg)
        self._width = width
        self._height = height
        self._pen = turtle.Turtle()
        self._pen.hideturtle()
        self._gb = bg

    def draw_axes(self):
        # self._pen.speed(0)
        self._pen.up()
        self._pen.goto(0, self._height / 2)
        self._pen.down()
        self._pen.goto(0, -self._height / 2)
        self._pen.up()
        self._pen.goto(-self._width / 2, 0)
        self._pen.down()
        self._pen.goto(self._width / 2, 0)
        self._pen.up()
        self._pen.goto(-self._width / 2, -self._height / 2)

    def draw_grid(self, colour='#dddddd', hstep=50, vstep=50):
        # self._pen.speed(0)
        original_pen_colour = self._pen.pencolor()
        self._pen.color(colour)
        # vertical grids
        self._pen.up()
        for hpos in range(-500, 500 + hstep, hstep):
            self._pen.goto(hpos, 350)
            self._pen.down()
            self._pen.goto(hpos, -350)
            self._pen.up()
        # horizontal grids
        for vpos in range(-350, 350 + vstep, vstep):
            self._pen.goto(-500, vpos)
            self._pen.down()
            self._pen.goto(500, vpos)
            self._pen.up()
        # reset
        self._pen.pencolor(original_pen_colour)

    def write(self, text, *args, **kwargs):
        text.write(self._pen, *args, **kwargs)

    def draw(self, shape):
        """Draw the given shape"""
        shape.draw(self._pen)

class Text:
    def __init__(self, text, at=(0,0), color = "black"):
        self._text = text
        self._at = at
        self._color = color

    def write(self, pen, *args, **kwargs):
        pen.up()
        pen.pencolor(self._color)
        pen.goto(self._at)
        pen.down()
        pen.write(self._text, *args, **kwargs)
        pen.up()

#### functions
def main():
    circle = Circle(50, fill = "blue", stroke = "black")
    quadrilater = Quadrilater(20, 30, fill="green", stroke="blue", at=(100,30))
    print(repr(circle))
    print(circle)
    print(f"Circle area = {circle.area}")
    print(f"Circle circumfrerence is {len(circle)}")
    print(repr(quadrilater))
    print(quadrilater)
    print(f"Quadrilater area = {quadrilater.calculate_area()}")
    print(f"Quadrilater perimeter is {len(quadrilater)}")

    yaml_circle = """\
circle:
    at: !!python/tuple
    - 0
    - 0
    fill: orange
    radius: 5.0
    stroke: red"""
    my_circle = Circle.from_yaml(yaml_circle) #use classmethod to load the circle described right above

    pen = turtle.Turtle()
    """
    text = Text("Wrote with turtle", at=(20,-50))
    print(text)
    text.write(pen, font=("Arial", 20, "bold"))
    circle.draw(pen)
    quadrilater.draw(pen)

    # canvas
    canvas = Canvas(1600, 700, bg="grey")
    canvas.draw_grid()
    canvas.draw_axes()
    #user
    canvas.write(text)
    canvas.draw(circle)
    canvas.draw(quadrilater)
    turtle.done()
    """
    #exercise
    canvas = Canvas(1000,700)
    gquad = Quadrilater(
        200, 300, fill="#009a44", stroke="white", at=(-200,0)
    )
    wquad = Quadrilater(
        200, 300, fill="white", stroke="#dddddd", at=(0,0)
    )
    oquad = Quadrilater(
        200, 300, fill="red", stroke="white", at=(200,0)
    )
    text = Text("ITALY", at=(0, -250), color = "black")
    canvas.draw(gquad)
    canvas.draw(wquad)
    canvas.draw(oquad)
    canvas.write(text, align="center", font = ("Arial", 60, "bold"))
    turtle.done()
    return os.EX_OK


#### run functions
if __name__ == "__main__":
    sys.exit(main())
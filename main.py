# This is a sample Python script.
import os
import sys
import turtle
from shapes.canvas import Canvas
from shapes.shapes import Circle, Quadrilater
from shapes.text import Text

turtle.tracer(False)

def main():
   circle = Circle(50, fill ="blue", stroke ="black")
    quadrilater = Quadrilater(20, 30, fill="green", stroke="blue", at=(100, 30))
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
    text = Text("ITALY", at=(0, -250), color ="black")
    canvas.draw(gquad)
    canvas.draw(wquad)
    canvas.draw(oquad)
    canvas.write(text, align="center", font = ("Arial", 60, "bold"))
    turtle.done()

    return os.EX_OK


#### run functions
if __name__ == "__main__":
    sys.exit(main())
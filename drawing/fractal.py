import turtle


def sierpinskiTriangle(someTurtle, l, n):
  if n == 0:
    return drawTriangle(someTurtle, l)
  l = l/2
  n = n-1
  sierpinskiTriangle(someTurtle, l, n)
  someTurtle.forward(l)
  sierpinskiTriangle(someTurtle, l, n)
  someTurtle.left(120)
  someTurtle.forward(l)
  someTurtle.right(120)
  sierpinskiTriangle(someTurtle, l, n)
  someTurtle.right(120)
  someTurtle.forward(l)
  someTurtle.left(120)

def drawTriangle(someTurtle, l):
  someTurtle.fillcolor('green')
  someTurtle.begin_fill()
  for x in range(0, 3):
    someTurtle.forward(l)
    someTurtle.left(120)
  someTurtle.end_fill()


def mainScreen():
  window = turtle.Screen()
  window.bgcolor('red')
  # Create a new turtle to draw a square
  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.color("green")
  brad.speed(0)
  sierpinskiTriangle(brad, 200, 3)

  window.exitonclick()


mainScreen()

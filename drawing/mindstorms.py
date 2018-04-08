import turtle


def drawSquare(someTurtle):
  for x in range(0,4):
    someTurtle.forward(100)
    someTurtle.right(90)


def drawCircle(someTurtle):
  someTurtle.circle(100)


def drawTriangle(someTurtle):
  for x in range(0, 3):
    someTurtle.forward(100)
    someTurtle.right(120)
    

def mainScreen():
  window = turtle.Screen()
  window.bgcolor('red')
  # Create a new turtle to draw a square
  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.color("green")
  for i in range(0,36):
    drawSquare(brad)
    brad.right(10)
  # Create a new turtle to draw a circle
  #angie = turtle.Turtle()
  #angie.color("blue")
  #drawCircle(angie)
  # Create a new turtle to draw a triangle
  #vera = turtle.Turtle()
  #vera.color("yellow")
  #drawTriangle(vera)

  window.exitonclick()

mainScreen()

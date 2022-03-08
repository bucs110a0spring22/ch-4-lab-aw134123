import turtle
import math

# y = math.sin(math.radians(180))
# print(y)

# wn = turtle.Screen()
# fred = turtle.Turtle()
# fred.goto(50,60)
# wn.exitonclick()
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def drawSineCurve(dart):
  '''for drawing sine curve
  dart:(turtle object)
  return:(none)'''
  for angle in range(-360, 360+1):
    x = math.radians(angle)
    y = math.sin(x)
    print('sin', angle, x, y)
    dart.goto(x,y)

def drawCosineCurve(dart):
  '''for drawing cosine curve
  dart:(turtle object)
  return:(none)'''
  for angle in range(-360, 360+1):
    x = math.radians(angle)
    y = math.cos(x)
    print('cos', angle, x, y)
    dart.goto(x,y)

def drawTangentCurve(dart):
  '''for drawing tangents to the curve
  dart:(turtle object)
  return:(none)'''
  for angle in range(-360, 360+1):
    x = math.radians(angle)
    y = math.tan(x)
    print('tan', angle, x, y)
    dart.goto(x,y)


def setupWindow(screen):
  '''sets up window coordinates
  screen:(Screen object)
  return:(none)'''
  screen.setworldcoordinates(-10*2, -1*2, 10*2, 1*2)

def setupAxis(dart):
  '''sets up turtle to starting point
  dart:(turtle object)
  return:(none)'''
  dart.hideturtle()
  dart.goto(0, 0)
  dart.showturtle()

##########  Do Not Alter Any Code Past Here ########
def main():
  #Part A
  wn = turtle.Screen()
  wn.tracer(5)
  dart = turtle.Turtle()
  dart.speed(10)
  drawSineCurve(dart)

  # #Part B
  setupWindow(wn)
  setupAxis(dart)
  dart.speed(10)
  dart.color("red")
  drawSineCurve(dart)
  dart.color("blue")
  drawCosineCurve(dart)
  dart.color("green")
  drawTangentCurve(dart)
  wn.exitonclick()
main()






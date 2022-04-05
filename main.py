import turtle
import math
from urllib.request import urlopen
from bs4 import BeautifulSoup

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

def randomGraphColor(screen):
  '''for creating different RGB values
  screen:(Screen object)
  return rbg values'''
  red = int(screen.numinput("Red", "Choose a number between 0 and 255", minval=0, maxval=255))
 
  green = int(screen.numinput("Blue","Choose another number between 0 and 255", minval=0, maxval=255))
 
  blue = int(screen.numinput("Green", "Choose a third number between 0 and 255", minval=0, maxval=255))
 
  return red, blue, green

def scrapeBing():
  '''for scraping binghamton announcement page
  no input parameter
  return announcements'''
  url_to_scrape = "https://www.binghamton.edu/apps/messaging/announcement/"
  request_page = urlopen(url_to_scrape) 
  page_html = request_page.read()
  request_page.close()
  html_soup = BeautifulSoup(page_html, 'html.parser')
  announcements = html_soup.find_all('li', class_="accordion-item")
  return announcements

##########  Do Not Alter Any Code Past Here ########
def main():
  #Part A
  wn = turtle.Screen()
  wn.tracer(5)
  wn.colormode(255)
  dart = turtle.Turtle()
  dart.speed(10)
  drawSineCurve(dart)

  # #Part B
  
  setupWindow(wn)
  setupAxis(dart)
  dart.speed(10)
  dart.color(randomGraphColor(wn))
  drawSineCurve(dart)
  dart.color(randomGraphColor(wn))
  drawCosineCurve(dart)
  dart.color(randomGraphColor(wn))
  drawTangentCurve(dart)
  announcements = scrapeBing()
  print(announcements)
  wn.exitonclick()
main()






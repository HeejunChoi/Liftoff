from turtle import *

speed(0) # Instant printing speed

bgcolor("black") # Setting background color

color("orange") # Creating Orange planet
begin_fill()
circle(60)
end_fill()

penup() # Moving forward
forward(100)
pendown()

color("grey") # Creating Grey planet
begin_fill()
circle(20)
end_fill()

penup() # Moving forward
forward(80)
pendown()

color("red") # Creating Red planet
begin_fill()
circle(40)
end_fill()

penup() # Moving forward
forward(90)
pendown()

color("green") # Creating Green planet
begin_fill()
circle(30)
end_fill()

done() # KEEP WINDOW OPEN
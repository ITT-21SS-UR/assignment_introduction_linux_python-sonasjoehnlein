import turtle   # import turtle module

itt = turtle.Turtle()
itt.shape("turtle")     # looks like a turtle
itt.speed(300)          # speed for drawing the circle

radius = int(input("Radius: "))  # radius as commandline parameter

while (radius > 0):              # while for drawing
    itt.forward(radius)          # stays at about radius pxiel
    itt.backward(radius)         # stays at about radius pxiel
    itt.left(0.5)                # move to a circle

if (radius < 0 or radius == 0):  # radius must be over 0
    print("Enter a radius over 0 and restart")  # error print

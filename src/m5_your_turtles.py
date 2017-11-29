"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Hyang Seo.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
import matplotlib

window = rg.TurtleWindow()

right_turtle = rg.SimpleTurtle('turtle')
left_turtle = rg.SimpleTurtle('turtle')

left_turtle.pen = rg.Pen ('orange', 4)
right_turtle.pen = rg.Pen('red', 4)

size = 60

right_turtle.draw_circle(size)
left_turtle.draw_circle(size)


for k in range(13):
    right_turtle.pen_up()
    right_turtle.right(45)
    right_turtle.forward(10)
    right_turtle.left(45)

    left_turtle.pen_up()
    left_turtle.right(45)
    left_turtle.forward(10)
    left_turtle.left(45)
size = -12



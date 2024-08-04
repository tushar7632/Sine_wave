from turtle import *
from math import *


A = 25       # Amplitude
B = 50       # WaveLength
C = 10       # Horizontal Shift
D = 20       # Vertical Shift

penup()
# As x increases y increases and decreases as it is evaluated.
for x in range(-200, 200):
    # Sine Wave Equation
    y = A * sin((2 * pi / B) * (x + C)) + D
    goto(x, y)
    pendown()

hideturtle()
mainloop()

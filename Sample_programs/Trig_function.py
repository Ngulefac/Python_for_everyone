from math import pi, sin, cos, tan
x = {x: sin(x*pi/180) for x in range(0, 90)}
y = {y: cos(y*pi/180) for y in range(0, 90)}

print("sin()=", x)
print("cos()=", y)

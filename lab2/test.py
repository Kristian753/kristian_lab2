from circle import Circle
try:
 c1 = Circle(x=0, y=0, radius=5)
except TypeError as e:
    print(f"valueerror:{e}")

c1.translate(5, -3)
print(c1)

c2 = Circle(1, 1, 3)
print(c1 == c2)
import math
x1, y1 = [float(A) for A in input().split()]
x2, y2 = [float(B) for B in input().split()]

dist = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

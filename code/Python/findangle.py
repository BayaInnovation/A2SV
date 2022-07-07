import math
A = int(input())
B = int(input())
c = math.sqrt(A**2 + B**2)
d = c/2.0
adj = B/2.0
Output = int(round(math.degrees(math.acos(adj/d))))
Output = str(Output)
print(Output+chr(176))
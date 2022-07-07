
import re;

a = int(input())
for _ in range(a):
    try:
        re.compile(input())
        Output = True
    except re.error:
        Output = False
    
    print(Output)


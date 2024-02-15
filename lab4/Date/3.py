#Write a Python program to drop microseconds from datetime.
from datetime import *
x = datetime.now()
m = x.replace(microsecond=0)
print(m)
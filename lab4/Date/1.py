#Write a Python program to subtract five days from current date.
from datetime import *
x = datetime.now()

f = x - timedelta(days=6555)
print(f)
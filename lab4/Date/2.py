#Write a Python program to print yesterday, today, tomorrow.
from datetime import *
today = datetime.now()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print(yesterday)
print(today)
print(tomorrow)
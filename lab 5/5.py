#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
import re

text = "John6See%3nadsfbbb"
x = re.findall('^.*a.*b$', text)   #. -- Any character (except newline character)
print(x)
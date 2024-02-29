#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

text = "aaaabbbbbbbbb12b"
x = re.search('ab*', text)
print(x)


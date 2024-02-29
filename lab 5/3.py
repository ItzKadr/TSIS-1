#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

text = 'dio_Sama_ZA_warudo_dksdkals_smam'
x = re.findall('[a-z]*_', text)
print(x)
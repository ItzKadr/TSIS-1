# The Syntax

'newlist = [expression for item in iterable if condition == True]'
# ex1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]

# ex2
newlist = [x for x in fruits]

# ex3
newlist = [x for x in range(10)]


#Boolean operators also exist in their usual form

#Negation w/ not

bool("") # False
not "" # True

not 1 > 2 # True

if not 1 > 2: #True
    print("nope") 

# or

'' or 'not empty' # Will give you the  truthy value, 'not empty'

'not empty' or 0 #Both are truthy, but only the first value will return

if '' or 'string': #True because 'string' is truthy
    print("This conditional evaluates to true")

#and - Evaulates returns true if and only if both values are true

if 'a' and '': #False
    print("this will not execute")


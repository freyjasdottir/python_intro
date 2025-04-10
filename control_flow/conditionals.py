#Comparisons work like most languages you're familiar with

print (1 < 2) #True
print (1 > 2) #False
print (1 == 2) #False
print (1 == 1) #True
print (1 == 1.0) #True

print ( 'a' == 'a') #True
print ('a' == 'A') #False

print ('a' > 'b') #False

print ('a' != 'b') #True

#Strings are compared one character at a time

print ('abc' < 'b') #True
print ('bac' < 'b') #False

#Use 'in' or 'not in' keyword to check for something in a sequence

print (2 in [1, 2, 3]) #True
print (4 not in [1, 2, 3]) #True

##Conditionals (if/then, you know the drill)

if True: #True
    print("Was true, so this line gets evaluated!")

if 1 > 2: #False
    print("This will not execute!")

if 1 > 2: #False
    print("No joy here")
else:
    print("Else condition hit!")

name = "bob"
if len(name) >= 4:
    print ("Name long")
elif len(name) == 3:
    print("only this line will execute")
elif len(name) >=2:
    print("this is true, but will not eval because the previous condition was hit")
else:
    print("name is way short")

#Tuples and ranges are collections that are *immutable*, unlike lists.

#Tuples are fixed width, you cannot change their length. Use parens instead of square brackets.
point = (2.0, 3.0)

#Tuples can be added to and assigned to a *new* tuple.
point_3d = point + (4.0,)
print(point_3d)

#You can unpack tuples with vars, but number of vars must match. This would not work with x, y
x, y, z = point_3d

print(x, y, z)


#Ranges are made with the range function
print(range(10))

#Ranges can save memory over lists, if you know they're a sequence and the same type.
print (list(range(10)))


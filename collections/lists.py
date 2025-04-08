#Syntax for creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)

#Can grab individual elements by index
print(my_list[0])
print(my_list[3])

#len() function works like you'd expect
print(len(my_list))

#Slicing is also available. Gives you index:up to but not including index
print(my_list[0:2])

#Can also use steps in slicing, defaults to 1. This grabs every other element.
print(my_list[::2])

#Quick way to reverse a list, negative step goes backwards.
print(my_list[::-1])

#Lists are mutable and not bound to types.
my_list[0] = "a"
print(my_list)

#Using readable methods is probably better than slicing to manipulate lists
my_list.remove(4)
print (my_list)

#One way to use a list as a stack
my_list.pop()
print(my_list)

my_list.pop()
print(my_list)

#Adding an element at a specific index
my_list.insert(0, 1)
print (my_list)

#Append bulitin method
my_list.append(5)
print (my_list)
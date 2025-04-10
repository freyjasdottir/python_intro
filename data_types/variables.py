#Variable assignment works like you'd expect
my_name = "Hannah"
print (my_name)

#Same result, but does not modify original variable
print (my_name + "Other")

#Actual modification of variable
my_name = my_name + "R"
print (my_name)

my_str = "Hannah"
my_int = 1

#Vars are not strong typed
my_str = my_int
print (my_str)

#Assignment is not a pointer!
my_int = 4
print (my_str)

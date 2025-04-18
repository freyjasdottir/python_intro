#Functions/methods also work like most languages you've seen

def hello_world():
    print("hello world")

hello_world() #Functions called also like you've seen a bazillion times

#Arguments to functions also work like you're used to

def print_name(name):
    print(f"Name is {name}")

print_name("Anne")
print_name("Ted")

#Can assign return value of a function to a variable.

output = print_name("Timmy")
print(output) #This will be None, because by default functions do not return values.

#Function that actually returns something

def add_two(num):
    return num + 2 #return keyword makes a return value happen

result = add_two(2)

print (result)# Will be 4

def add (num1, num2): #Defining multiple args
    return num1 + num2

#Can use keyword args instead of positional ones

def contact_card(name, age, car_model):
    return f"{name} is {age} and drives a {car_model}"

contact_card(age=35, car_model="Civic", name="Paul") #With keyword args they do not have to be in the same order as the function sig.
#These can be mixed with positional arguments, but the positional arguments *have* to be passed first.

#Can also set default arguments

def can_drive(age, driving_age=16):
    return age >= driving_age

can_drive(15) #False

can_drive(15, 14) # True, because you can override defaults if you pass them.
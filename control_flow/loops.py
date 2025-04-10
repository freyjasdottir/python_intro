#while loops, also as expected

#while True: #oops this is an infinite loop don't do this
    #print('looping')

#better version is have an incrementor/decrementor

count = 1
while count <= 4:
    print(count)
    count += 1

#for loops, for when you want to iterate over a collection of things. Still like other for loops you've seen

colors = ['blue', 'green', 'red', 'yellow']

for color in colors:
    print(color)
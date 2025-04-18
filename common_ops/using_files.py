#Open a text file and write some lines to it

my_file = open('marios.txt', 'w+')
my_file.write('Mario\n')
my_file.write('Wario\n')

my_file.writelines([
    'Shyguy\n',
    'Donkey Kong\n',
    'Birdo\n',
])

my_file.close()


#Read from a text file
my_file = open('marios.txt', 'r')
print(my_file.read())
my_file.close()
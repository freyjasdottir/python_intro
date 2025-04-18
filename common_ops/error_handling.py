#Small demo of exception handling by opening an already existing file.
import sys


file_name = 'recipes.txt'

try:
    my_file = open('recipes.txt', 'x')
    my_file.write('Kebab\n')
    my_file.close()
except FileExistsError as err: #File already exists
    print(f"The {file_name} file already exists.")
    print(err)
except:
    #If there is some other error, eg the file is not a text file.
    print(f"Unable to write to the file")
else:
    #If no error cases hit
    print(f"Wrote to {file_name}")
finally:
    #End of block in any case
    print(f"Execution completed")
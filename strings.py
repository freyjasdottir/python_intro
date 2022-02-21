#!/usr/bin/env python3.9

# This will evaluate to an empty string with single quotes.
print("")
print("It doesn't matter if we use double quotes here, because python internally represent them with single quotes.")
print('single quoted')
print("double quoted")

print('''
multi-line
single quote''')

print('concatenating strings with  +')
print('single' + 'quote')
print('contatenating with multiplication')
print("Ha" * 4)


print("strings are collections of characters")
print('single'.find('d'))
print('single'.find('g'))
print('single'.find('le'))


print('the easiest way to compare strings is to lowercase them')
print("TeStIng".lower())

print('special characters')
print("Tab\tDelimited")
print("New\nLine")

print('escaping')
print("Slash\\Character")
print("Slash\Character")

print('quotes inside quotes')
print('"Double" quotes')
print('\'Double\' quotes')

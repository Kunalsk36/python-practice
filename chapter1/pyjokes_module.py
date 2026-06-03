# pip install pyjokes
# multiline comment - """text""" or '''text'''
''' This module is used to get random jokes in Python. 
 It provides a simple interface to retrieve jokes in various categories and languages. 
 You can use it to add some humor to your Python applications or just for fun.'''

import pyjokes
joke = pyjokes.get_joke()
print(joke)
print("\n")
joke = pyjokes.get_joke(language="en", category="all")
print(joke)
print("\n")
joke = pyjokes.get_joke(language="en", category="neutral")
print(joke)
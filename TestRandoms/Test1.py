import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)

def greetings(who_needs_greet):
    greeting = 'Hello, {}'.format(who_needs_greet)
    return greeting

print (greetings("world"))
#print(greetings("Atique"))
r= requests.get('https://varian.com')
print (r.history)

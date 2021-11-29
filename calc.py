#calculator
#
from colorama import init
from colorama import Fore, Back, Style
init()

print(Back.GREEN)
print(Fore.BLACK)
x=input('+ or -: ')
print(Back.RED)
a=float(input('a: '))
b=float(input('b: '))
print(Back.BLUE)

if x=='+':
    c = a + b
    print('result: ' + str(c))
elif x=='-':
    c = a - b
    print('result: ' + str(c))
else:
    print('wrong operation')

input()
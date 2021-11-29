#+,-,*,/,**,%,унарный минус,округление,Пи
import math
a=8
b=4
q=3
w=3.63
r=1.09
c=a+b
d=a-b
e=a*b
f=a/b
g=a**b
h=a%q
q=-q

print('c='+str(c), 'd='+str(d), 'e='+str(e), 'f='+str(f), 'g='+str(g), 'h='+str(h), 'q='+str(q))
print('w='+str(round(w)))
print('w='+str(math.floor(w)))
print('w='+str(math.ceil(w)))
print('r='+str(math.floor(r)))
print('r='+str(math.ceil(r)))
print('Pi='+str(math.pi))
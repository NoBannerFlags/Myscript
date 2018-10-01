#!/usr/bin/python
import time
x = ''
y = ''.join(sorted(x))
y = y.replace(' ', '')
y = y.replace('A', 'a')
y = y.replace('B', 'b')
y = y.replace('C', 'c')
y = y.replace('D', 'd')
y = y.replace('E', 'e')
y = y.replace('F', 'f')
y = y.replace('G', 'g')
y = y.replace('H', 'h')
y = y.replace('I', 'i')
y = y.replace('J', 'j')
y = y.replace('K', 'k')
y = y.replace('L', 'l')
y = y.replace('M', 'm')
y = y.replace('N', 'n')
y = y.replace('O', 'o')
y = y.replace('P', 'p')
y = y.replace('Q', 'q')
y = y.replace('R', 'r')
y = y.replace('S', 's')
y = y.replace('T', 't')
y = y.replace('U', 'u')
y = y.replace('V', 'v')
y = y.replace('W', 'w')
y = y.replace('X', 'x')
y = y.replace('Y', 'y')
y = y.replace('Z', 'z')
f1 = open ('test.txt','w');
f1.write('');
f1.close();
f = open('test.txt','a')
z = 0;
print('Script by NoBannerFlags');

for i in y:
	z = z+1
	
	if z>=10:
		f.write('\n');
		z=0;
	f.write(i)
f.close();

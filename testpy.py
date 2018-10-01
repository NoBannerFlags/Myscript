#!/usr/bin/python
import time
x = input("What string would you like to sort? please use \' before and after your input."
y = ''.join(sorted(x))
y = y.replace(' ', '')
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

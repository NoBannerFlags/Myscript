#!/usr/bin/python
import time

#x = input();
x = ''
y = ''.join(sorted(x))
f1 = open ('test.txt','w');
f1.write('');
f1.close();
f = open('test.txt','a')
z = 0;
print('Script by Kai.');
print('sorting \"'+x+'\" to test.txt');
print('sorted text is '+y);
for i in y:
	z = z+1
	#time.sleep(0.1);
	if z>=10:
		f.write('\n');
		z=0;
	f.write(i)
	#print(i);
f.close();

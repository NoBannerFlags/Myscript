#!/usr/bin/python
import time
def sortMe ( stringtoSort, fileName ):
	"This sorts the string that is given, filename meaning the file it is stored in."
	y = ''.join(sorted(x)).lower()
	storeMe = open(fileName,'w')
	storeMe.write('');
	storeMe.close();
	storeMe2 = open(fileName,'a')
	count = 0;
	for i in y:
		count = count+1
	
		if count>=10:
			storeMe2.write('\n');
			count=0;
		storeMe2.write(i)
	storeMe2.close();

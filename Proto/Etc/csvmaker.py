#!/usr/bin/env python
# -*- coding: utf-8 -*-
# csvmaker

import csv
import random
import numpy

pages = 100
samplelist = []
f = open('test.csv','w') 

writer = csv.writer(f, lineterminator='\n')
for i in range(60*pages):
	for j in range(60):
		samplelist.append(random.randint(0,49))
		
	writer.writerow(samplelist)
	samplelist = []
	# writer.writerow('\n')

f.close()
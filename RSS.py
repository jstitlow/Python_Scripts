# !/usr/bin/python

import csv

with open('RSS.csv', 'r') as csvinput:
	with open('RSSoutput.csv', 'w') as csvoutput:
		writer = csv.writer(csvoutput, lineterminator='\n')
		reader = csv.reader(csvinput)
		
		all = []
		row = next(reader)
		row.append('RSS')
		all.append(row)
		
		for row in reader:
			row.append(row[0])
			all.append(row)
			
		writer.writerows(all)
        
quit()
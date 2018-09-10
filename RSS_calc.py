# !/usr/bin/python

import pandas as pd
import numpy as np


RSS = pd.read_csv('Fit_1B_2species_2D_rawFitData_FixedAmp.csv')

df=pd.DataFrame(RSS)

#df['RSS']=((df[df.columns[1]]-df[df.columns[2]])**2)

#Create empty data frame
pd.DataFrame()
results=pd.DataFrame()

#Calculate RSS for each fit in the raw data file
for i in range (1,210,2):			#Adjust to number of files
	df['%s%s' % ('RSS', i)]=((df[df.columns[i]]-df[df.columns[i+1]])**2)
	#sum_row=df['%s%s' % ('RSS', i)].sum()
	#results.append(df['%s%s' % ('RSS', i)].sum())
	
#df.to_csv('RSS_results.csv')
df.to_csv('RSS_output.csv')

quit()

	

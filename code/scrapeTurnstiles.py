#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pandas as pd
import csv
import sys
import time


def getTurnstileData():
	'''scrapes all turnstile data from the website'''

	# allDFs = []

	csvPath = '/Users/casy/Dropbox/CUSP/1_2_CAUI/CA_project1/transport/turnstile_data_links.csv'
	with open(csvPath, 'r') as csvfile:
	  csvReader = csv.reader(csvfile, delimiter=',', quotechar='"', )
	  next(csvReader, None) # skip headers

	  for line in csvReader:
	  	name = line[1].split('/')[-1].replace('txt','csv')
	  	print name
	  	try:
		  	df = pd.read_csv(line[1])
		  	# allDFs.append(df)
		  	# print sys.argv[1] + name
		  	df.to_csv(sys.argv[1] + name, encoding='utf8')
		except Exception,e:
			print str(e)
	  	# time.sleep(1) # just to be sure
	
	return pd.concat(allDFs)

def main():
	'''saving turnstiles as one file to 
	selected location'''
	# print sys.argv[1]
	getTurnstileData()
	

if __name__ == '__main__':
	main()


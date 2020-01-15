from pymongo import MongoClient
import pandas as pd
import os
import csv
import sys, getopt, pprint
import json


host="mongodb://localhost:27017"
client= MongoClient(host)
db = client["gw_data"]
col_name =  input("Please enter the new collection name: ")
col = db[col_name]

def main():
        
	#print the files in the current directory
	cwd = os.getcwd()
	for subdir, dirs, files in os.walk(cwd, topdown=True):
		del dirs[:] #remove sub directories.
		for file in files:
			print (file)

	file_to_load = input("File to load: ")

	loadAndInsertData(file_to_load)


def loadAndInsertData(file):
	#str() to make sure the file path is in string
	csvfile = open(str(file))
	reader = csv.DictReader(csvfile)
	header = reader.fieldnames
	count = 0

	for each in reader:
		row={}
		for field in header:
			row[field]=each[field]
		col.insert_one(row)
		count = count + 1

	if(count!=0):
		print("COMPLETED! " + str(count) + " rows inserted")
	else:
		print(str(count) + " rows have been inserted")



if __name__=="__main__":
	main()


from pymongo import MongoClient
import pandas as pd
import os
import csv
import sys, getopt, pprint
import json


try:
	host = "mongodb://localhost:27017"
	client = MongoClient(host)
	print("Establishing connection to " + str(host))

	#list files in current directory
	for subdir, dirs, files in os.walk('./'):
		del dirs[:]
		for file in files:
			print(file)



	file_to_load = input("Type in the file to load: "

	db = client["gw_data"]
	col = db["carbon_emissions"]


	def main():
		#Don't shorten the data table
		pd.set_option('display.max_colwidth', -1)

		loadAndInsertData(FILE_TO_LOAD)

	def loadAndInsertData(file):
		#remove the data first to avoid duplicates
		col.drop()

		#open the file
		csvfile = open(str(file))
		reader = csv.DictReader(csvfile)
		#header = ["TIME", "GEO", "UNIT", "AIRPOL", "SRC_CRF", "Value" ]
		header = reader.fieldnames
		count = 0
		for each in reader:
			row={}
			for field in header:
				row[field]=each[field]
			col.insert_one(row)
			count = count + 1
		if(count != 0):
			print("COMPLETED! " + str(count) + " rows inserted!")
		else:
			print(str(count) + "rows have been inserted. Maybe check if filename is correct?")


	if __name__=="__main__":
		main()

except:
	print("Cannot connect to the database, please try again later")



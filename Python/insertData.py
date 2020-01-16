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
run = True

def main():
    while(run):
        #print the files in the current directory and store them in array
        list_files=[]
        cwd = os.getcwd()
    
        for subdir, dirs, files in os.walk(cwd, topdown=True):
            del dirs[:] #remove sub directories.
            for file in files:
                list_files.append(file)
                print(file)

        file_to_load = input("File to load: ")
    
        file_exists = doesFileExist(file_to_load, list_files)

        if(file_exists):
            loadAndInsertData(file_to_load)    
        else:
            print('\n File does not exist, please try again')

def doesFileExist(file_name, file_list):
     exists = False
     if(file_name in file_list):
        exists = True
     return exists


def loadAndInsertData(file):
    #str() to make sure the file path is in string
    csvfile = open(str(file))
    reader = csv.DictReader(csvfile)
    header = reader.fieldnames
    count = 0
    try: 
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
    except:
        print('\n Something went wrong')


if __name__=="__main__":
    main()


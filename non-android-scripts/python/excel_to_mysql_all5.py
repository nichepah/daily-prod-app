#!/usr/bin/python
# inserts ALL-5 Integrated Steel Plant's production data into mysql db, from excel
# Author: Aneesh PA
# mail: mypa4me@gmail.com
# date: 23 Feb 2018

import MySQLdb
import xlrd
import datetime
import sys

file=sys.argv[1]
print file


excel_list = xlrd.open_workbook(file)
sheet = excel_list.sheet_by_index(0)

database = MySQLdb.connect (host='localhost', \
user ='test_updater', passwd='updater123', db='test')
cursor = database.cursor()

query = """INSERT INTO T_ALL5_ACT_PRO (
Production_Date,
Oven_Pushing,
HM,
PI,
CS,
CC,
SS_Prod,
SS_Desp 
) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)""" 

col = 9

prod_d = sheet.cell(0, col).value
Production_Date = datetime.datetime(*xlrd.xldate_as_tuple(prod_d, excel_list.datemode)).strftime("%Y-%m-%d")

Oven_Pushing = sheet.cell(93,col).value
HM = sheet.cell(94, col).value
PI = sheet.cell(95, col).value
CS = sheet.cell(96, col).value
CC = sheet.cell(97, col).value
SS_Prod = sheet.cell(98, col).value
SS_Desp  = sheet.cell(99, col).value

values = (
Production_Date,
Oven_Pushing,
HM,
PI,
CS,
CC,
SS_Prod,
SS_Desp)

#print values

cursor.execute(query,values)
cursor.close();
database.commit()

database.close()

print""
print values
print "Done !"

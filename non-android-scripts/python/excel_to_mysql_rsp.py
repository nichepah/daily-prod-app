#!/usr/bin/python
# inserts RSP's production data into mysql db, from excel
# Author: Aneesh PA
# mail: mypa4me@gmail.com
# date: 23 Jan 2018

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

#caster3 removed
query = """INSERT INTO T_RSP_ACT_PRO (
Production_Date,
Oven_Pushing,
Sinter,
HM,
PI,
CS,
SMS_1_CC,
SMS2_CC,

Plate_Mill,
New_PM,
HSM,
CR_Saleable,
CRNO,
Semis,
Fin_Steel,
SS_Prod,
SS_Desp 
) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" 

col = 9

prod_d = sheet.cell(0, col).value
Production_Date = datetime.datetime(*xlrd.xldate_as_tuple(prod_d, excel_list.datemode)).strftime("%Y-%m-%d")

Oven_Pushing = sheet.cell(40,col).value
Sinter = sheet.cell(41, col).value
HM = sheet.cell(42, col).value
PI = sheet.cell(43, col).value
CS = sheet.cell(44, col).value
SMS1_CC = sheet.cell(45, col).value
SMS2_CC = sheet.cell(46, col).value
#Caster_3 = sheet.cell(47, col).value
Plate_Mill = sheet.cell(48, col).value
New_PM = sheet.cell(49, col).value
HSM = sheet.cell(50, col).value
CR_Saleable = sheet.cell(51, col).value
CRNO = sheet.cell(52, col).value
Semis = sheet.cell(53, col).value
Fin_Steel = sheet.cell(54, col).value
SS_Prod = sheet.cell(55, col).value
SS_Desp  = sheet.cell(56, col).value

values = (
Production_Date,
Oven_Pushing,
Sinter,
HM,
PI,
CS,
SMS1_CC,
SMS2_CC,
#Caster_3,
Plate_Mill,
New_PM,
HSM,
CR_Saleable,
CRNO,
Semis,
Fin_Steel,
SS_Prod,
SS_Desp 
)

#print values

cursor.execute(query,values)
cursor.close();
database.commit()

database.close()

print""
print values
print "Done !"

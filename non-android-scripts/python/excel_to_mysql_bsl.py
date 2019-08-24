#!/usr/bin/python
# inserts BSL's production data into mysql db, from excel
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

query = """INSERT INTO T_BSL_ACT_PRO (
Production_Date,
Oven_Pushing,
Sinter,
HM,
PI,
CS,
SMS_1,
SMS2_CC,
SM,
HSM,
CRM_1_2,
CRM_3,
CR_Saleable,
Semis,
Fin_Steel,
SS_Prod,
SS_Desp 
) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" 

col = 9

prod_d = sheet.cell(0, col).value
Production_Date = datetime.datetime(*xlrd.xldate_as_tuple(prod_d, excel_list.datemode)).strftime("%Y-%m-%d")

Oven_Pushing = sheet.cell(60,col).value
Sinter = sheet.cell(61, col).value
HM = sheet.cell(62, col).value
PI = sheet.cell(63, col).value
CS = sheet.cell(64, col).value
SMS_1 = sheet.cell(65, col).value
SMS2_CC = sheet.cell(66, col).value
SM = sheet.cell(67, col).value
HSM = sheet.cell(68, col).value
CRM_1_2 = sheet.cell(69, col).value
CRM_3 = sheet.cell(70, col).value
CR_Saleable = sheet.cell(71, col).value
Semis = sheet.cell(72, col).value
Fin_Steel = sheet.cell(73, col).value
SS_Prod = sheet.cell(74, col).value
SS_Desp  = sheet.cell(75, col).value

values = (
Production_Date,
Oven_Pushing,
Sinter,
HM,
PI,
CS,
SMS_1,
SMS2_CC,
SM,
HSM,
CRM_1_2,
CRM_3,
CR_Saleable,
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

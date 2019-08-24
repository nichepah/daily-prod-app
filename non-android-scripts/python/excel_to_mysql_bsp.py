#!/usr/bin/python
# inserts production data into mysql db, from excel
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

#BRM Removed; As it is not entered in the spreadsheet
query = """INSERT INTO T_BSP_ACT_PRO (
Production_Date,
Oven_Pushing,
Sinter,
HM,
PI,
CS,
SMS_1,
SMS_2_CC,
BBM_ingot_rolling,
Rails,
URM,
MM,
WRM,

Plate_Mill,
Semis,
Fin_Steel,
SS_Prod,
SS_Desp) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" 

col = 9

prod_d = sheet.cell(0, col).value
Production_Date = datetime.datetime(*xlrd.xldate_as_tuple(prod_d, excel_list.datemode)).strftime("%Y-%m-%d")

Oven_Pushing = sheet.cell(3,col).value
Sinter = sheet.cell(4, col).value
HM = sheet.cell(5, col).value
PI = sheet.cell(6, col).value
CS = sheet.cell(7, col).value
SMS_1 = sheet.cell(8, col).value
SMS_2_CC = sheet.cell(9, col).value
BBM_ingot_rolling = sheet.cell(10, col).value
Rails = sheet.cell(11, col).value
URM = sheet.cell(12, col).value
MM = sheet.cell(13, col).value
WRM = sheet.cell(14, col).value
#BRM = sheet.cell(15, col).value
Plate_Mill = sheet.cell(16, col).value
Semis = sheet.cell(17, col).value
Fin_Steel = sheet.cell(18, col).value
SS_Prod = sheet.cell(19, col).value
SS_Desp  = sheet.cell(20, col).value

values = (
Production_Date,
Oven_Pushing,
Sinter,
HM,
PI,
CS,
SMS_1,
SMS_2_CC,
BBM_ingot_rolling,
Rails,
URM,
MM,
WRM,

Plate_Mill,
Semis,
Fin_Steel,
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

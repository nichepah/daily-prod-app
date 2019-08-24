#!/usr/bin/python
# inserts DSP's production data into mysql db, from excel
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

query = """INSERT INTO T_DSP_ACT_PRO (
Production_Date,
Oven_Pushing,
Sinter,
HM,
PI,
CS,
CC_Billet,
CC_Bloom,
BRC,
BRM,
MM,
SM,
MSM,
W_n_A,
Semis,
Fin_Steel,
SS_Prod,
SS_Desp ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" 

col = 9

prod_d = sheet.cell(0, col).value
Production_Date = datetime.datetime(*xlrd.xldate_as_tuple(prod_d, excel_list.datemode)).strftime("%Y-%m-%d")

Oven_Pushing = sheet.cell(22,col).value
Sinter = sheet.cell(23, col).value
HM = sheet.cell(24, col).value
PI = sheet.cell(25, col).value
CS = sheet.cell(26, col).value
CC_Billet = sheet.cell(27, col).value
CC_Bloom = sheet.cell(28, col).value
BRC = sheet.cell(29, col).value
BRM = sheet.cell(30, col).value
MM = sheet.cell(31, col).value
SM = sheet.cell(32, col).value
MSM = sheet.cell(33, col).value
W_n_A = sheet.cell(34, col).value
Semis = sheet.cell(35, col).value
Fin_Steel = sheet.cell(36, col).value
SS_Prod = sheet.cell(37, col).value
SS_Desp  = sheet.cell(38, col).value

values = (
Production_Date,
Oven_Pushing,
Sinter,
HM,
PI,
CS,
CC_Billet,
CC_Bloom,
BRC,
BRM,
MM,
SM,
MSM,
W_n_A,
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

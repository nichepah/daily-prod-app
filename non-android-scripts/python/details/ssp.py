#!/usr/bin/python
# inserts production data into mysql db, from excel
# Author: Aneesh PA
# mail: mypa4me@gmail.com
# date: 02 April 2018
# modified to include all fields : 03042018

import MySQLdb
import xlrd
import datetime
import sys


file=sys.argv[1]
print file

excel_list = xlrd.open_workbook(file)
sheet = excel_list.sheet_by_index(0)

#Pay Attention: BRM
#field[] = {'Oven_Push', 'Sinter', 'HM', 'PI', 'CS', 'HRM', 'SMS_2_HRM', 'BBM_Ingot', 'Rails', 'URM', 'MM', 'WRM', 'BRM', 'Plate_Mill', 'Semis', 'Fin_Steel', 'SS_Prod', 'SS_Desp'}
#Pay Attention: column 10 not used
#suf[] = {'_Mon_CPLY','_Mon_Tar_APP','_Mon_Tar_Rev','_Daily_Tar_APP','_Daily_Tar_Rev', '_Act', 'NotUsed', '_Cum','_MRate','_APP_Fulfill'}
#data = {}

col = 9
prod_d = sheet.cell(0, col).value
Production_Date = datetime.datetime(*xlrd.xldate_as_tuple(prod_d, excel_list.datemode)).strftime("%Y-%m-%d")

row = 108
CS_Mon_CPLY = sheet.cell(row, 4).value
CS_Mon_Tar_APP = sheet.cell(row, 5).value
CS_Mon_Tar_Rev = sheet.cell(row, 6).value
CS_Daily_Tar_APP = sheet.cell(row, 7).value
CS_Daily_Tar_Rev = sheet.cell(row, 8).value
CS_Act = sheet.cell(row, 9).value
CS_Cum = sheet.cell(row, 11).value
CS_MRate = sheet.cell(row, 12).value
CS_APP_Fulfill = sheet.cell(row, 13).value

row = 109
HRM_Mon_CPLY = sheet.cell(row, 4).value
HRM_Mon_Tar_APP = sheet.cell(row, 5).value
HRM_Mon_Tar_Rev = sheet.cell(row, 6).value
HRM_Daily_Tar_APP = sheet.cell(row, 7).value
HRM_Daily_Tar_Rev = sheet.cell(row, 8).value
HRM_Act = sheet.cell(row, 9).value
HRM_Cum = sheet.cell(row, 11).value
HRM_MRate = sheet.cell(row, 12).value
HRM_APP_Fulfill = sheet.cell(row, 13).value


row = 110
SS_Prod_Mon_CPLY = sheet.cell(row, 4).value
SS_Prod_Mon_Tar_APP = sheet.cell(row, 5).value
SS_Prod_Mon_Tar_Rev = sheet.cell(row, 6).value
SS_Prod_Daily_Tar_APP = sheet.cell(row, 7).value
SS_Prod_Daily_Tar_Rev = sheet.cell(row, 8).value
SS_Prod_Act = sheet.cell(row, 9).value
SS_Prod_Cum = sheet.cell(row, 11).value
SS_Prod_MRate = sheet.cell(row, 12).value
SS_Prod_APP_Fulfill = sheet.cell(row, 13).value

row = 111
SS_Desp_Mon_CPLY = sheet.cell(row, 4).value
SS_Desp_Mon_Tar_APP = sheet.cell(row, 5).value
SS_Desp_Mon_Tar_Rev = sheet.cell(row, 6).value
SS_Desp_Daily_Tar_APP = sheet.cell(row, 7).value
SS_Desp_Daily_Tar_Rev = sheet.cell(row, 8).value
SS_Desp_Act = sheet.cell(row, 9).value
SS_Desp_Cum = sheet.cell(row, 11).value
SS_Desp_MRate = sheet.cell(row, 12).value
SS_Desp_APP_Fulfill = sheet.cell(row, 13).value

database = MySQLdb.connect (host='localhost', \
user ='test_updater', passwd='updater123', db='SAILPRO')
cursor = database.cursor()

#BRM Removed; As it is not entered in the spreadsheet
#17*9 fields, BRM excluded
query = """INSERT INTO T_SSP (
Production_Date,

CS_Mon_CPLY,
CS_Mon_Tar_APP,
CS_Mon_Tar_Rev,
CS_Daily_Tar_APP,
CS_Daily_Tar_Rev,
CS_Act,
CS_Cum,
CS_MRate,
CS_APP_Fulfill,

HRM_Mon_CPLY,
HRM_Mon_Tar_APP,
HRM_Mon_Tar_Rev,
HRM_Daily_Tar_APP,
HRM_Daily_Tar_Rev,
HRM_Act,
HRM_Cum,
HRM_MRate,
HRM_APP_Fulfill,

SS_Prod_Mon_CPLY,
SS_Prod_Mon_Tar_APP,
SS_Prod_Mon_Tar_Rev,
SS_Prod_Daily_Tar_APP,
SS_Prod_Daily_Tar_Rev,
SS_Prod_Act,
SS_Prod_Cum,
SS_Prod_MRate,
SS_Prod_APP_Fulfill,

SS_Desp_Mon_CPLY,
SS_Desp_Mon_Tar_APP,
SS_Desp_Mon_Tar_Rev,
SS_Desp_Daily_Tar_APP,
SS_Desp_Daily_Tar_Rev,
SS_Desp_Act,
SS_Desp_Cum,
SS_Desp_MRate,
SS_Desp_APP_Fulfill
) 
VALUES (%s,
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)""" 

values = (
Production_Date,

CS_Mon_CPLY,
CS_Mon_Tar_APP,
CS_Mon_Tar_Rev,
CS_Daily_Tar_APP,
CS_Daily_Tar_Rev,
CS_Act,
CS_Cum,
CS_MRate,
CS_APP_Fulfill,

HRM_Mon_CPLY,
HRM_Mon_Tar_APP,
HRM_Mon_Tar_Rev,
HRM_Daily_Tar_APP,
HRM_Daily_Tar_Rev,
HRM_Act,
HRM_Cum,
HRM_MRate,
HRM_APP_Fulfill,

SS_Prod_Mon_CPLY,
SS_Prod_Mon_Tar_APP,
SS_Prod_Mon_Tar_Rev,
SS_Prod_Daily_Tar_APP,
SS_Prod_Daily_Tar_Rev,
SS_Prod_Act,
SS_Prod_Cum,
SS_Prod_MRate,
SS_Prod_APP_Fulfill,

SS_Desp_Mon_CPLY,
SS_Desp_Mon_Tar_APP,
SS_Desp_Mon_Tar_Rev,
SS_Desp_Daily_Tar_APP,
SS_Desp_Daily_Tar_Rev,
SS_Desp_Act,
SS_Desp_Cum,
SS_Desp_MRate,
SS_Desp_APP_Fulfill
) 
 
print values

cursor.execute(query,values)
cursor.close();
database.commit()

database.close()

#print""
#print values
#print "Done !"

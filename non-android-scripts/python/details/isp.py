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
#field[] = {'Oven_Push', 'Sinter', 'HM', 'PI', 'CS', 'SMS_1', 'WRM', 'Bar_Mill', 'USM', 'URM', 'MM', 'WRM', 'BRM', 'Plate_Mill', 'Semis', 'Fin_Steel', 'SS_Prod', 'SS_Desp'}
#Pay Attention: column 10 not used
#suf[] = {'_Mon_CPLY','_Mon_Tar_APP','_Mon_Tar_Rev','_Daily_Tar_APP','_Daily_Tar_Rev', '_Act', 'NotUsed', '_Cum','_MRate','_APP_Fulfill'}
#data = {}

col = 9
prod_d = sheet.cell(0, col).value
Production_Date = datetime.datetime(*xlrd.xldate_as_tuple(prod_d, excel_list.datemode)).strftime("%Y-%m-%d")

row = 78
Oven_Push_Mon_CPLY = sheet.cell(row, 4).value
oven_Push_Mon_Tar_APP = sheet.cell(row, 5).value
oven_Push_Mon_Tar_Rev = sheet.cell(row, 6).value
oven_Push_Daily_Tar_APP = sheet.cell(row, 7).value
oven_Push_Daily_Tar_Rev = sheet.cell(row, 8).value
Oven_Push_Act = sheet.cell(row, 9).value
Oven_Push_Cum = sheet.cell(row, 11).value
Oven_Push_MRate = sheet.cell(row, 12).value
Oven_Push_APP_Fulfill = sheet.cell(row, 13).value

row=83
Sinter_Mon_CPLY = sheet.cell(row, 4).value
Sinter_Mon_Tar_APP = sheet.cell(row, 5).value
Sinter_Mon_Tar_Rev = sheet.cell(row, 6).value
Sinter_Daily_Tar_APP = sheet.cell(row, 7).value
Sinter_Daily_Tar_Rev = sheet.cell(row, 8).value
Sinter_Act = sheet.cell(row, 9).value
Sinter_Cum = sheet.cell(row, 11).value
Sinter_MRate = sheet.cell(row, 12).value
Sinter_APP_Fulfill = sheet.cell(row, 13).value

row = 79
HM_Mon_CPLY = sheet.cell(row, 4).value
HM_Mon_Tar_APP = sheet.cell(row, 5).value
HM_Mon_Tar_Rev = sheet.cell(row, 6).value
HM_Daily_Tar_APP = sheet.cell(row, 7).value
HM_Daily_Tar_Rev = sheet.cell(row, 8).value
HM_Act = sheet.cell(row, 9).value
HM_Cum = sheet.cell(row, 11).value
HM_MRate = sheet.cell(row, 12).value
HM_APP_Fulfill = sheet.cell(row, 13).value

row = 80
PI_Mon_CPLY = sheet.cell(row, 4).value
PI_Mon_Tar_APP = sheet.cell(row, 5).value
PI_Mon_Tar_Rev = sheet.cell(row, 6).value
PI_Daily_Tar_APP = sheet.cell(row, 7).value
PI_Daily_Tar_Rev = sheet.cell(row, 8).value
PI_Act = sheet.cell(row, 9).value
PI_Cum = sheet.cell(row, 11).value
PI_MRate = sheet.cell(row, 12).value
PI_APP_Fulfill = sheet.cell(row, 13).value

row = 81
CS_Mon_CPLY = sheet.cell(row, 4).value
CS_Mon_Tar_APP = sheet.cell(row, 5).value
CS_Mon_Tar_Rev = sheet.cell(row, 6).value
CS_Daily_Tar_APP = sheet.cell(row, 7).value
CS_Daily_Tar_Rev = sheet.cell(row, 8).value
CS_Act = sheet.cell(row, 9).value
CS_Cum = sheet.cell(row, 11).value
CS_MRate = sheet.cell(row, 12).value
CS_APP_Fulfill = sheet.cell(row, 13).value

row = 82
CC_Mon_CPLY = sheet.cell(row, 4).value
CC_Mon_Tar_APP = sheet.cell(row, 5).value
CC_Mon_Tar_Rev = sheet.cell(row, 6).value
CC_Daily_Tar_APP = sheet.cell(row, 7).value
CC_Daily_Tar_Rev = sheet.cell(row, 8).value
CC_Act = sheet.cell(row, 9).value
CC_Cum = sheet.cell(row, 11).value
CC_MRate = sheet.cell(row, 12).value
CC_APP_Fulfill = sheet.cell(row, 13).value

row = 84
WRM_Mon_CPLY = sheet.cell(row, 4).value
WRM_Mon_Tar_APP = sheet.cell(row, 5).value
WRM_Mon_Tar_Rev = sheet.cell(row, 6).value
WRM_Daily_Tar_APP = sheet.cell(row, 7).value
WRM_Daily_Tar_Rev = sheet.cell(row, 8).value
WRM_Act = sheet.cell(row, 9).value
WRM_Cum = sheet.cell(row, 11).value
WRM_MRate = sheet.cell(row, 12).value
WRM_APP_Fulfill = sheet.cell(row, 13).value

row = 85
Bar_Mill_Mon_CPLY = sheet.cell(row, 4).value
Bar_Mill_Mon_Tar_APP = sheet.cell(row, 5).value
Bar_Mill_Mon_Tar_Rev = sheet.cell(row, 6).value
Bar_Mill_Daily_Tar_APP = sheet.cell(row, 7).value
Bar_Mill_Daily_Tar_Rev = sheet.cell(row, 8).value
Bar_Mill_Act = sheet.cell(row, 9).value
Bar_Mill_Cum = sheet.cell(row, 11).value
Bar_Mill_MRate = sheet.cell(row, 12).value
Bar_Mill_APP_Fulfill = sheet.cell(row, 13).value

row = 86
USM_Mon_CPLY = sheet.cell(row, 4).value
USM_Mon_Tar_APP = sheet.cell(row, 5).value
USM_Mon_Tar_Rev = sheet.cell(row, 6).value
USM_Daily_Tar_APP = sheet.cell(row, 7).value
USM_Daily_Tar_Rev = sheet.cell(row, 8).value
USM_Act = sheet.cell(row, 9).value
USM_Cum = sheet.cell(row, 11).value
USM_MRate = sheet.cell(row, 12).value
USM_APP_Fulfill = sheet.cell(row, 13).value


row = 87
Semis_Mon_CPLY = sheet.cell(row, 4).value
Semis_Mon_Tar_APP = sheet.cell(row, 5).value
Semis_Mon_Tar_Rev = sheet.cell(row, 6).value
Semis_Daily_Tar_APP = sheet.cell(row, 7).value
Semis_Daily_Tar_Rev = sheet.cell(row, 8).value
Semis_Act = sheet.cell(row, 9).value
Semis_Cum = sheet.cell(row, 11).value
Semis_MRate = sheet.cell(row, 12).value
Semis_APP_Fulfill = sheet.cell(row, 13).value

row = 88
Fin_Steel_Mon_CPLY = sheet.cell(row, 4).value
Fin_Steel_Mon_Tar_APP = sheet.cell(row, 5).value
Fin_Steel_Mon_Tar_Rev = sheet.cell(row, 6).value
Fin_Steel_Daily_Tar_APP = sheet.cell(row, 7).value
Fin_Steel_Daily_Tar_Rev = sheet.cell(row, 8).value
Fin_Steel_Act = sheet.cell(row, 9).value
Fin_Steel_Cum = sheet.cell(row, 11).value
Fin_Steel_MRate = sheet.cell(row, 12).value
Fin_Steel_APP_Fulfill = sheet.cell(row, 13).value

row = 89
SS_Prod_Mon_CPLY = sheet.cell(row, 4).value
SS_Prod_Mon_Tar_APP = sheet.cell(row, 5).value
SS_Prod_Mon_Tar_Rev = sheet.cell(row, 6).value
SS_Prod_Daily_Tar_APP = sheet.cell(row, 7).value
SS_Prod_Daily_Tar_Rev = sheet.cell(row, 8).value
SS_Prod_Act = sheet.cell(row, 9).value
SS_Prod_Cum = sheet.cell(row, 11).value
SS_Prod_MRate = sheet.cell(row, 12).value
SS_Prod_APP_Fulfill = sheet.cell(row, 13).value

row = 90
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
query = """INSERT INTO T_ISP (
Production_Date,

Oven_Push_Mon_CPLY,
oven_Push_Mon_Tar_APP,
oven_Push_Mon_Tar_Rev,
Oven_Push_Act,
oven_Push_Daily_Tar_APP,
oven_Push_Daily_Tar_Rev,
Oven_Push_Cum,
Oven_Push_MRate,
Oven_Push_APP_Fulfill,

Sinter_Mon_CPLY,
Sinter_Mon_Tar_APP,
Sinter_Mon_Tar_Rev,
Sinter_Daily_Tar_APP,
Sinter_Daily_Tar_Rev,
Sinter_Act,
Sinter_Cum,
Sinter_MRate,
Sinter_APP_Fulfill,

HM_Mon_CPLY,
HM_Mon_Tar_APP,
HM_Mon_Tar_Rev,
HM_Daily_Tar_APP,
HM_Daily_Tar_Rev,
HM_Act,
HM_Cum,
HM_MRate,
HM_APP_Fulfill,

PI_Mon_CPLY,
PI_Mon_Tar_APP,
PI_Mon_Tar_Rev,
PI_Daily_Tar_APP,
PI_Daily_Tar_Rev,
PI_Act,
PI_Cum,
PI_MRate,
PI_APP_Fulfill,

CS_Mon_CPLY,
CS_Mon_Tar_APP,
CS_Mon_Tar_Rev,
CS_Daily_Tar_APP,
CS_Daily_Tar_Rev,
CS_Act,
CS_Cum,
CS_MRate,
CS_APP_Fulfill,

CC_Mon_CPLY,
CC_Mon_Tar_APP,
CC_Mon_Tar_Rev,
CC_Daily_Tar_APP,
CC_Daily_Tar_Rev,
CC_Act,
CC_Cum,
CC_MRate,
CC_APP_Fulfill,

WRM_Mon_CPLY,
WRM_Mon_Tar_APP,
WRM_Mon_Tar_Rev,
WRM_Daily_Tar_APP,
WRM_Daily_Tar_Rev,
WRM_Act,
WRM_Cum,
WRM_MRate,
WRM_APP_Fulfill,

Bar_Mill_Mon_CPLY,
Bar_Mill_Mon_Tar_APP,
Bar_Mill_Mon_Tar_Rev,
Bar_Mill_Daily_Tar_APP,
Bar_Mill_Daily_Tar_Rev,
Bar_Mill_Act,
Bar_Mill_Cum,
Bar_Mill_MRate,
Bar_Mill_APP_Fulfill,

USM_Mon_CPLY,
USM_Mon_Tar_APP,
USM_Mon_Tar_Rev,
USM_Daily_Tar_APP,
USM_Daily_Tar_Rev,
USM_Act,
USM_Cum,
USM_MRate,
USM_APP_Fulfill,

Semis_Mon_CPLY,
Semis_Mon_Tar_APP,
Semis_Mon_Tar_Rev,
Semis_Daily_Tar_APP,
Semis_Daily_Tar_Rev,
Semis_Act,
Semis_Cum,
Semis_MRate,
Semis_APP_Fulfill,

Fin_Steel_Mon_CPLY,
Fin_Steel_Mon_Tar_APP,
Fin_Steel_Mon_Tar_Rev,
Fin_Steel_Daily_Tar_APP,
Fin_Steel_Daily_Tar_Rev,
Fin_Steel_Act,
Fin_Steel_Cum,
Fin_Steel_MRate,
Fin_Steel_APP_Fulfill,

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
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s
)""" 

values = (
Production_Date,

Oven_Push_Mon_CPLY,
oven_Push_Mon_Tar_APP,
oven_Push_Mon_Tar_Rev,
Oven_Push_Act,
oven_Push_Daily_Tar_APP,
oven_Push_Daily_Tar_Rev,
Oven_Push_Cum,
Oven_Push_MRate,
Oven_Push_APP_Fulfill,

Sinter_Mon_CPLY,
Sinter_Mon_Tar_APP,
Sinter_Mon_Tar_Rev,
Sinter_Daily_Tar_APP,
Sinter_Daily_Tar_Rev,
Sinter_Act,
Sinter_Cum,
Sinter_MRate,
Sinter_APP_Fulfill,

HM_Mon_CPLY,
HM_Mon_Tar_APP,
HM_Mon_Tar_Rev,
HM_Daily_Tar_APP,
HM_Daily_Tar_Rev,
HM_Act,
HM_Cum,
HM_MRate,
HM_APP_Fulfill,

PI_Mon_CPLY,
PI_Mon_Tar_APP,
PI_Mon_Tar_Rev,
PI_Daily_Tar_APP,
PI_Daily_Tar_Rev,
PI_Act,
PI_Cum,
PI_MRate,
PI_APP_Fulfill,

CS_Mon_CPLY,
CS_Mon_Tar_APP,
CS_Mon_Tar_Rev,
CS_Daily_Tar_APP,
CS_Daily_Tar_Rev,
CS_Act,
CS_Cum,
CS_MRate,
CS_APP_Fulfill,

CC_Mon_CPLY,
CC_Mon_Tar_APP,
CC_Mon_Tar_Rev,
CC_Daily_Tar_APP,
CC_Daily_Tar_Rev,
CC_Act,
CC_Cum,
CC_MRate,
CC_APP_Fulfill,

WRM_Mon_CPLY,
WRM_Mon_Tar_APP,
WRM_Mon_Tar_Rev,
WRM_Daily_Tar_APP,
WRM_Daily_Tar_Rev,
WRM_Act,
WRM_Cum,
WRM_MRate,
WRM_APP_Fulfill,

Bar_Mill_Mon_CPLY,
Bar_Mill_Mon_Tar_APP,
Bar_Mill_Mon_Tar_Rev,
Bar_Mill_Daily_Tar_APP,
Bar_Mill_Daily_Tar_Rev,
Bar_Mill_Act,
Bar_Mill_Cum,
Bar_Mill_MRate,
Bar_Mill_APP_Fulfill,

USM_Mon_CPLY,
USM_Mon_Tar_APP,
USM_Mon_Tar_Rev,
USM_Daily_Tar_APP,
USM_Daily_Tar_Rev,
USM_Act,
USM_Cum,
USM_MRate,
USM_APP_Fulfill,


Semis_Mon_CPLY,
Semis_Mon_Tar_APP,
Semis_Mon_Tar_Rev,
Semis_Daily_Tar_APP,
Semis_Daily_Tar_Rev,
Semis_Act,
Semis_Cum,
Semis_MRate,
Semis_APP_Fulfill,

Fin_Steel_Mon_CPLY,
Fin_Steel_Mon_Tar_APP,
Fin_Steel_Mon_Tar_Rev,
Fin_Steel_Daily_Tar_APP,
Fin_Steel_Daily_Tar_Rev,
Fin_Steel_Act,
Fin_Steel_Cum,
Fin_Steel_MRate,
Fin_Steel_APP_Fulfill,

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

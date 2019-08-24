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

col = 9
prod_d = sheet.cell(0, col).value
Production_Date = datetime.datetime(*xlrd.xldate_as_tuple(prod_d, excel_list.datemode)).strftime("%Y-%m-%d")

row = 40
Oven_Push_Mon_CPLY = sheet.cell(row, 4).value
oven_Push_Mon_Tar_APP = sheet.cell(row, 5).value
oven_Push_Mon_Tar_Rev = sheet.cell(row, 6).value
oven_Push_Daily_Tar_APP = sheet.cell(row, 7).value
oven_Push_Daily_Tar_Rev = sheet.cell(row, 8).value
Oven_Push_Act = sheet.cell(row, 9).value
Oven_Push_Cum = sheet.cell(row, 11).value
Oven_Push_MRate = sheet.cell(row, 12).value
Oven_Push_APP_Fulfill = sheet.cell(row, 13).value

row=41
Sinter_Mon_CPLY = sheet.cell(row, 4).value
Sinter_Mon_Tar_APP = sheet.cell(row, 5).value
Sinter_Mon_Tar_Rev = sheet.cell(row, 6).value
Sinter_Daily_Tar_APP = sheet.cell(row, 7).value
Sinter_Daily_Tar_Rev = sheet.cell(row, 8).value
Sinter_Act = sheet.cell(row, 9).value
Sinter_Cum = sheet.cell(row, 11).value
Sinter_MRate = sheet.cell(row, 12).value
Sinter_APP_Fulfill = sheet.cell(row, 13).value

row = 42
HM_Mon_CPLY = sheet.cell(row, 4).value
HM_Mon_Tar_APP = sheet.cell(row, 5).value
HM_Mon_Tar_Rev = sheet.cell(row, 6).value
HM_Daily_Tar_APP = sheet.cell(row, 7).value
HM_Daily_Tar_Rev = sheet.cell(row, 8).value
HM_Act = sheet.cell(row, 9).value
HM_Cum = sheet.cell(row, 11).value
HM_MRate = sheet.cell(row, 12).value
HM_APP_Fulfill = sheet.cell(row, 13).value

row = 43
PI_Mon_CPLY = sheet.cell(row, 4).value
PI_Mon_Tar_APP = sheet.cell(row, 5).value
PI_Mon_Tar_Rev = sheet.cell(row, 6).value
PI_Daily_Tar_APP = sheet.cell(row, 7).value
PI_Daily_Tar_Rev = sheet.cell(row, 8).value
PI_Act = sheet.cell(row, 9).value
PI_Cum = sheet.cell(row, 11).value
PI_MRate = sheet.cell(row, 12).value
PI_APP_Fulfill = sheet.cell(row, 13).value

row = 44
CS_Mon_CPLY = sheet.cell(row, 4).value
CS_Mon_Tar_APP = sheet.cell(row, 5).value
CS_Mon_Tar_Rev = sheet.cell(row, 6).value
CS_Daily_Tar_APP = sheet.cell(row, 7).value
CS_Daily_Tar_Rev = sheet.cell(row, 8).value
CS_Act = sheet.cell(row, 9).value
CS_Cum = sheet.cell(row, 11).value
CS_MRate = sheet.cell(row, 12).value
CS_APP_Fulfill = sheet.cell(row, 13).value

row = 45
SMS1_CC_Mon_CPLY = sheet.cell(row, 4).value
SMS1_CC_Mon_Tar_APP = sheet.cell(row, 5).value
SMS1_CC_Mon_Tar_Rev = sheet.cell(row, 6).value
SMS1_CC_Daily_Tar_APP = sheet.cell(row, 7).value
SMS1_CC_Daily_Tar_Rev = sheet.cell(row, 8).value
SMS1_CC_Act = sheet.cell(row, 9).value
SMS1_CC_Cum = sheet.cell(row, 11).value
SMS1_CC_MRate = sheet.cell(row, 12).value
SMS1_CC_APP_Fulfill = sheet.cell(row, 13).value

row = 46
SMS2_CC_Mon_CPLY = sheet.cell(row, 4).value
SMS2_CC_Mon_Tar_APP = sheet.cell(row, 5).value
SMS2_CC_Mon_Tar_Rev = sheet.cell(row, 6).value
SMS2_CC_Daily_Tar_APP = sheet.cell(row, 7).value
SMS2_CC_Daily_Tar_Rev = sheet.cell(row, 8).value
SMS2_CC_Act = sheet.cell(row, 9).value
SMS2_CC_Cum = sheet.cell(row, 11).value
SMS2_CC_MRate = sheet.cell(row, 12).value
SMS2_CC_APP_Fulfill = sheet.cell(row, 13).value

row = 48
Plate_Mill_Mon_CPLY = sheet.cell(row, 4).value
Plate_Mill_Mon_Tar_APP = sheet.cell(row, 5).value
Plate_Mill_Mon_Tar_Rev = sheet.cell(row, 6).value
Plate_Mill_Daily_Tar_APP = sheet.cell(row, 7).value
Plate_Mill_Daily_Tar_Rev = sheet.cell(row, 8).value
Plate_Mill_Act = sheet.cell(row, 9).value
Plate_Mill_Cum = sheet.cell(row, 11).value
Plate_Mill_MRate = sheet.cell(row, 12).value
Plate_Mill_APP_Fulfill = sheet.cell(row, 13).value

row = 49
New_PM_Mon_CPLY = sheet.cell(row, 4).value
New_PM_Mon_Tar_APP = sheet.cell(row, 5).value
New_PM_Mon_Tar_Rev = sheet.cell(row, 6).value
New_PM_Daily_Tar_APP = sheet.cell(row, 7).value
New_PM_Daily_Tar_Rev = sheet.cell(row, 8).value
New_PM_Act = sheet.cell(row, 9).value
New_PM_Cum = sheet.cell(row, 11).value
New_PM_MRate = sheet.cell(row, 12).value
New_PM_APP_Fulfill = sheet.cell(row, 13).value

row = 50
HSM_Mon_CPLY = sheet.cell(row, 4).value
HSM_Mon_Tar_APP = sheet.cell(row, 5).value
HSM_Mon_Tar_Rev = sheet.cell(row, 6).value
HSM_Daily_Tar_APP = sheet.cell(row, 7).value
HSM_Daily_Tar_Rev = sheet.cell(row, 8).value
HSM_Act = sheet.cell(row, 9).value
HSM_Cum = sheet.cell(row, 11).value
HSM_MRate = sheet.cell(row, 12).value
HSM_APP_Fulfill = sheet.cell(row, 13).value

row = 51
CR_Saleable_Mon_CPLY = sheet.cell(row, 4).value
CR_Saleable_Mon_Tar_APP = sheet.cell(row, 5).value
CR_Saleable_Mon_Tar_Rev = sheet.cell(row, 6).value
CR_Saleable_Daily_Tar_APP = sheet.cell(row, 7).value
CR_Saleable_Daily_Tar_Rev = sheet.cell(row, 8).value
CR_Saleable_Act = sheet.cell(row, 9).value
CR_Saleable_Cum = sheet.cell(row, 11).value
CR_Saleable_MRate = sheet.cell(row, 12).value
CR_Saleable_APP_Fulfill = sheet.cell(row, 13).value

row = 52
CRNO_Mon_CPLY = sheet.cell(row, 4).value
CRNO_Mon_Tar_APP = sheet.cell(row, 5).value
CRNO_Mon_Tar_Rev = sheet.cell(row, 6).value
CRNO_Daily_Tar_APP = sheet.cell(row, 7).value
CRNO_Daily_Tar_Rev = sheet.cell(row, 8).value
CRNO_Act = sheet.cell(row, 9).value
CRNO_Cum = sheet.cell(row, 11).value
CRNO_MRate = sheet.cell(row, 12).value
CRNO_APP_Fulfill = sheet.cell(row, 13).value

row = 53
Semis_Mon_CPLY = sheet.cell(row, 4).value
Semis_Mon_Tar_APP = sheet.cell(row, 5).value
Semis_Mon_Tar_Rev = sheet.cell(row, 6).value
Semis_Daily_Tar_APP = sheet.cell(row, 7).value
Semis_Daily_Tar_Rev = sheet.cell(row, 8).value
Semis_Act = sheet.cell(row, 9).value
Semis_Cum = sheet.cell(row, 11).value
Semis_MRate = sheet.cell(row, 12).value
Semis_APP_Fulfill = sheet.cell(row, 13).value

row = 54
Fin_Steel_Mon_CPLY = sheet.cell(row, 4).value
Fin_Steel_Mon_Tar_APP = sheet.cell(row, 5).value
Fin_Steel_Mon_Tar_Rev = sheet.cell(row, 6).value
Fin_Steel_Daily_Tar_APP = sheet.cell(row, 7).value
Fin_Steel_Daily_Tar_Rev = sheet.cell(row, 8).value
Fin_Steel_Act = sheet.cell(row, 9).value
Fin_Steel_Cum = sheet.cell(row, 11).value
Fin_Steel_MRate = sheet.cell(row, 12).value
Fin_Steel_APP_Fulfill = sheet.cell(row, 13).value

row = 55
SS_Prod_Mon_CPLY = sheet.cell(row, 4).value
SS_Prod_Mon_Tar_APP = sheet.cell(row, 5).value
SS_Prod_Mon_Tar_Rev = sheet.cell(row, 6).value
SS_Prod_Daily_Tar_APP = sheet.cell(row, 7).value
SS_Prod_Daily_Tar_Rev = sheet.cell(row, 8).value
SS_Prod_Act = sheet.cell(row, 9).value
SS_Prod_Cum = sheet.cell(row, 11).value
SS_Prod_MRate = sheet.cell(row, 12).value
SS_Prod_APP_Fulfill = sheet.cell(row, 13).value

row = 56
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
query = """INSERT INTO T_RSP (
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

SMS1_CC_Mon_CPLY,
SMS1_CC_Mon_Tar_APP,
SMS1_CC_Mon_Tar_Rev,
SMS1_CC_Daily_Tar_APP,
SMS1_CC_Daily_Tar_Rev,
SMS1_CC_Act,
SMS1_CC_Cum,
SMS1_CC_MRate,
SMS1_CC_APP_Fulfill,

SMS2_CC_Mon_CPLY,
SMS2_CC_Mon_Tar_APP,
SMS2_CC_Mon_Tar_Rev,
SMS2_CC_Daily_Tar_APP,
SMS2_CC_Daily_Tar_Rev,
SMS2_CC_Act,
SMS2_CC_Cum,
SMS2_CC_MRate,
SMS2_CC_APP_Fulfill,

Plate_Mill_Mon_CPLY,
Plate_Mill_Mon_Tar_APP,
Plate_Mill_Mon_Tar_Rev,
Plate_Mill_Daily_Tar_APP,
Plate_Mill_Daily_Tar_Rev,
Plate_Mill_Act,
Plate_Mill_Cum,
Plate_Mill_MRate,
Plate_Mill_APP_Fulfill,

New_PM_Mon_CPLY,
New_PM_Mon_Tar_APP,
New_PM_Mon_Tar_Rev,
New_PM_Daily_Tar_APP,
New_PM_Daily_Tar_Rev,
New_PM_Act,
New_PM_Cum,
New_PM_MRate,
New_PM_APP_Fulfill,

HSM_Mon_CPLY,
HSM_Mon_Tar_APP,
HSM_Mon_Tar_Rev,
HSM_Daily_Tar_APP,
HSM_Daily_Tar_Rev,
HSM_Act,
HSM_Cum,
HSM_MRate,
HSM_APP_Fulfill,

CR_Saleable_Mon_CPLY,
CR_Saleable_Mon_Tar_APP,
CR_Saleable_Mon_Tar_Rev,
CR_Saleable_Daily_Tar_APP,
CR_Saleable_Daily_Tar_Rev,
CR_Saleable_Act,
CR_Saleable_Cum,
CR_Saleable_MRate,
CR_Saleable_APP_Fulfill,

CRNO_Mon_CPLY,
CRNO_Mon_Tar_APP,
CRNO_Mon_Tar_Rev,
CRNO_Daily_Tar_APP,
CRNO_Daily_Tar_Rev,
CRNO_Act,
CRNO_Cum,
CRNO_MRate,
CRNO_APP_Fulfill,

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
%s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s
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

SMS1_CC_Mon_CPLY,
SMS1_CC_Mon_Tar_APP,
SMS1_CC_Mon_Tar_Rev,
SMS1_CC_Daily_Tar_APP,
SMS1_CC_Daily_Tar_Rev,
SMS1_CC_Act,
SMS1_CC_Cum,
SMS1_CC_MRate,
SMS1_CC_APP_Fulfill,

SMS2_CC_Mon_CPLY,
SMS2_CC_Mon_Tar_APP,
SMS2_CC_Mon_Tar_Rev,
SMS2_CC_Daily_Tar_APP,
SMS2_CC_Daily_Tar_Rev,
SMS2_CC_Act,
SMS2_CC_Cum,
SMS2_CC_MRate,
SMS2_CC_APP_Fulfill,

Plate_Mill_Mon_CPLY,
Plate_Mill_Mon_Tar_APP,
Plate_Mill_Mon_Tar_Rev,
Plate_Mill_Daily_Tar_APP,
Plate_Mill_Daily_Tar_Rev,
Plate_Mill_Act,
Plate_Mill_Cum,
Plate_Mill_MRate,
Plate_Mill_APP_Fulfill,

New_PM_Mon_CPLY,
New_PM_Mon_Tar_APP,
New_PM_Mon_Tar_Rev,
New_PM_Daily_Tar_APP,
New_PM_Daily_Tar_Rev,
New_PM_Act,
New_PM_Cum,
New_PM_MRate,
New_PM_APP_Fulfill,

HSM_Mon_CPLY,
HSM_Mon_Tar_APP,
HSM_Mon_Tar_Rev,
HSM_Daily_Tar_APP,
HSM_Daily_Tar_Rev,
HSM_Act,
HSM_Cum,
HSM_MRate,
HSM_APP_Fulfill,

CR_Saleable_Mon_CPLY,
CR_Saleable_Mon_Tar_APP,
CR_Saleable_Mon_Tar_Rev,
CR_Saleable_Daily_Tar_APP,
CR_Saleable_Daily_Tar_Rev,
CR_Saleable_Act,
CR_Saleable_Cum,
CR_Saleable_MRate,
CR_Saleable_APP_Fulfill,

CRNO_Mon_CPLY,
CRNO_Mon_Tar_APP,
CRNO_Mon_Tar_Rev,
CRNO_Daily_Tar_APP,
CRNO_Daily_Tar_Rev,
CRNO_Act,
CRNO_Cum,
CRNO_MRate,
CRNO_APP_Fulfill,

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

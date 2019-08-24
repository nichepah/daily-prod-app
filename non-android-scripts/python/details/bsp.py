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

database = MySQLdb.connect (host='localhost', \
user ='test_updater', passwd='updater123', db='SAILPRO')
cursor = database.cursor()

col = 9
prod_d = sheet.cell(0, col).value
Production_Date = datetime.datetime(*xlrd.xldate_as_tuple(prod_d, excel_list.datemode)).strftime("%Y-%m-%d")

row = 3
Oven_Push_Mon_CPLY = sheet.cell(row, 4).value
oven_Push_Mon_Tar_APP = sheet.cell(row, 5).value
oven_Push_Mon_Tar_Rev = sheet.cell(row, 6).value
oven_Push_Daily_Tar_APP = sheet.cell(row, 7).value
oven_Push_Daily_Tar_Rev = sheet.cell(row, 8).value
Oven_Push_Act = sheet.cell(row, 9).value
Oven_Push_Cum = sheet.cell(row, 11).value
Oven_Push_MRate = sheet.cell(row, 12).value
Oven_Push_APP_Fulfill = sheet.cell(row, 13).value

row=4
Sinter_Mon_CPLY = sheet.cell(row, 4).value
Sinter_Mon_Tar_APP = sheet.cell(row, 5).value
Sinter_Mon_Tar_Rev = sheet.cell(row, 6).value
Sinter_Daily_Tar_APP = sheet.cell(row, 7).value
Sinter_Daily_Tar_Rev = sheet.cell(row, 8).value
Sinter_Act = sheet.cell(row, 9).value
Sinter_Cum = sheet.cell(row, 11).value
Sinter_MRate = sheet.cell(row, 12).value
Sinter_APP_Fulfill = sheet.cell(row, 13).value

row = 5
HM_Mon_CPLY = sheet.cell(row, 4).value
HM_Mon_Tar_APP = sheet.cell(row, 5).value
HM_Mon_Tar_Rev = sheet.cell(row, 6).value
HM_Daily_Tar_APP = sheet.cell(row, 7).value
HM_Daily_Tar_Rev = sheet.cell(row, 8).value
HM_Act = sheet.cell(row, 9).value
HM_Cum = sheet.cell(row, 11).value
HM_MRate = sheet.cell(row, 12).value
HM_APP_Fulfill = sheet.cell(row, 13).value

row = 6
PI_Mon_CPLY = sheet.cell(row, 4).value
PI_Mon_Tar_APP = sheet.cell(row, 5).value
PI_Mon_Tar_Rev = sheet.cell(row, 6).value
PI_Daily_Tar_APP = sheet.cell(row, 7).value
PI_Daily_Tar_Rev = sheet.cell(row, 8).value
PI_Act = sheet.cell(row, 9).value
PI_Cum = sheet.cell(row, 11).value
PI_MRate = sheet.cell(row, 12).value
PI_APP_Fulfill = sheet.cell(row, 13).value

row = 7
CS_Mon_CPLY = sheet.cell(row, 4).value
CS_Mon_Tar_APP = sheet.cell(row, 5).value
CS_Mon_Tar_Rev = sheet.cell(row, 6).value
CS_Daily_Tar_APP = sheet.cell(row, 7).value
CS_Daily_Tar_Rev = sheet.cell(row, 8).value
CS_Act = sheet.cell(row, 9).value
CS_Cum = sheet.cell(row, 11).value
CS_MRate = sheet.cell(row, 12).value
CS_APP_Fulfill = sheet.cell(row, 13).value

row = 8
SMS_1_Mon_CPLY = sheet.cell(row, 4).value
SMS_1_Mon_Tar_APP = sheet.cell(row, 5).value
SMS_1_Mon_Tar_Rev = sheet.cell(row, 6).value
SMS_1_Daily_Tar_APP = sheet.cell(row, 7).value
SMS_1_Daily_Tar_Rev = sheet.cell(row, 8).value
SMS_1_Act = sheet.cell(row, 9).value
SMS_1_Cum = sheet.cell(row, 11).value
SMS_1_MRate = sheet.cell(row, 12).value
SMS_1_APP_Fulfill = sheet.cell(row, 13).value

row = 9
SMS_2_CC_Mon_CPLY = sheet.cell(row, 4).value
SMS_2_CC_Mon_Tar_APP = sheet.cell(row, 5).value
SMS_2_CC_Mon_Tar_Rev = sheet.cell(row, 6).value
SMS_2_CC_Daily_Tar_APP = sheet.cell(row, 7).value
SMS_2_CC_Daily_Tar_Rev = sheet.cell(row, 8).value
SMS_2_CC_Act = sheet.cell(row, 9).value
SMS_2_CC_Cum = sheet.cell(row, 11).value
SMS_2_CC_MRate = sheet.cell(row, 12).value
SMS_2_CC_APP_Fulfill = sheet.cell(row, 13).value

row = 10
BBM_Ingot_Mon_CPLY = sheet.cell(row, 4).value
BBM_Ingot_Mon_Tar_APP = sheet.cell(row, 5).value
BBM_Ingot_Mon_Tar_Rev = sheet.cell(row, 6).value
BBM_Ingot_Daily_Tar_APP = sheet.cell(row, 7).value
BBM_Ingot_Daily_Tar_Rev = sheet.cell(row, 8).value
BBM_Ingot_Act = sheet.cell(row, 9).value
BBM_Ingot_Cum = sheet.cell(row, 11).value
BBM_Ingot_MRate = sheet.cell(row, 12).value
BBM_Ingot_APP_Fulfill = sheet.cell(row, 13).value

row = 11
Rails_Mon_CPLY = sheet.cell(row, 4).value
Rails_Mon_Tar_APP = sheet.cell(row, 5).value
Rails_Mon_Tar_Rev = sheet.cell(row, 6).value
Rails_Daily_Tar_APP = sheet.cell(row, 7).value
Rails_Daily_Tar_Rev = sheet.cell(row, 8).value
Rails_Act = sheet.cell(row, 9).value
Rails_Cum = sheet.cell(row, 11).value
Rails_MRate = sheet.cell(row, 12).value
Rails_APP_Fulfill = sheet.cell(row, 13).value

row = 12
URM_Mon_CPLY = sheet.cell(row, 4).value
URM_Mon_Tar_APP = sheet.cell(row, 5).value
URM_Mon_Tar_Rev = sheet.cell(row, 6).value
URM_Daily_Tar_APP = sheet.cell(row, 7).value
URM_Daily_Tar_Rev = sheet.cell(row, 8).value
URM_Act = sheet.cell(row, 9).value
URM_Cum = sheet.cell(row, 11).value
URM_MRate = sheet.cell(row, 12).value
URM_APP_Fulfill = sheet.cell(row, 13).value

row = 13
MM_Mon_CPLY = sheet.cell(row, 4).value
MM_Mon_Tar_APP = sheet.cell(row, 5).value
MM_Mon_Tar_Rev = sheet.cell(row, 6).value
MM_Daily_Tar_APP = sheet.cell(row, 7).value
MM_Daily_Tar_Rev = sheet.cell(row, 8).value
MM_Act = sheet.cell(row, 9).value
MM_Cum = sheet.cell(row, 11).value
MM_MRate = sheet.cell(row, 12).value
MM_APP_Fulfill = sheet.cell(row, 13).value

row = 14
WRM_Mon_CPLY = sheet.cell(row, 4).value
WRM_Mon_Tar_APP = sheet.cell(row, 5).value
WRM_Mon_Tar_Rev = sheet.cell(row, 6).value
WRM_Daily_Tar_APP = sheet.cell(row, 7).value
WRM_Daily_Tar_Rev = sheet.cell(row, 8).value
WRM_Act = sheet.cell(row, 9).value
WRM_Cum = sheet.cell(row, 11).value
WRM_MRate = sheet.cell(row, 12).value
WRM_APP_Fulfill = sheet.cell(row, 13).value

row = 16
Plate_Mill_Mon_CPLY = sheet.cell(row, 4).value
Plate_Mill_Mon_Tar_APP = sheet.cell(row, 5).value
Plate_Mill_Mon_Tar_Rev = sheet.cell(row, 6).value
Plate_Mill_Daily_Tar_APP = sheet.cell(row, 7).value
Plate_Mill_Daily_Tar_Rev = sheet.cell(row, 8).value
Plate_Mill_Act = sheet.cell(row, 9).value
Plate_Mill_Cum = sheet.cell(row, 11).value
Plate_Mill_MRate = sheet.cell(row, 12).value
Plate_Mill_APP_Fulfill = sheet.cell(row, 13).value

row = 17
Semis_Mon_CPLY = sheet.cell(row, 4).value
Semis_Mon_Tar_APP = sheet.cell(row, 5).value
Semis_Mon_Tar_Rev = sheet.cell(row, 6).value
Semis_Daily_Tar_APP = sheet.cell(row, 7).value
Semis_Daily_Tar_Rev = sheet.cell(row, 8).value
Semis_Act = sheet.cell(row, 9).value
Semis_Cum = sheet.cell(row, 11).value
Semis_MRate = sheet.cell(row, 12).value
Semis_APP_Fulfill = sheet.cell(row, 13).value

row = 18
Fin_Steel_Mon_CPLY = sheet.cell(row, 4).value
Fin_Steel_Mon_Tar_APP = sheet.cell(row, 5).value
Fin_Steel_Mon_Tar_Rev = sheet.cell(row, 6).value
Fin_Steel_Daily_Tar_APP = sheet.cell(row, 7).value
Fin_Steel_Daily_Tar_Rev = sheet.cell(row, 8).value
Fin_Steel_Act = sheet.cell(row, 9).value
Fin_Steel_Cum = sheet.cell(row, 11).value
Fin_Steel_MRate = sheet.cell(row, 12).value
Fin_Steel_APP_Fulfill = sheet.cell(row, 13).value

row = 19
SS_Prod_Mon_CPLY = sheet.cell(row, 4).value
SS_Prod_Mon_Tar_APP = sheet.cell(row, 5).value
SS_Prod_Mon_Tar_Rev = sheet.cell(row, 6).value
SS_Prod_Daily_Tar_APP = sheet.cell(row, 7).value
SS_Prod_Daily_Tar_Rev = sheet.cell(row, 8).value
SS_Prod_Act = sheet.cell(row, 9).value
SS_Prod_Cum = sheet.cell(row, 11).value
SS_Prod_MRate = sheet.cell(row, 12).value
SS_Prod_APP_Fulfill = sheet.cell(row, 13).value

row = 20
SS_Desp_Mon_CPLY = sheet.cell(row, 4).value
SS_Desp_Mon_Tar_APP = sheet.cell(row, 5).value
SS_Desp_Mon_Tar_Rev = sheet.cell(row, 6).value
SS_Desp_Daily_Tar_APP = sheet.cell(row, 7).value
SS_Desp_Daily_Tar_Rev = sheet.cell(row, 8).value
SS_Desp_Act = sheet.cell(row, 9).value
SS_Desp_Cum = sheet.cell(row, 11).value
SS_Desp_MRate = sheet.cell(row, 12).value
SS_Desp_APP_Fulfill = sheet.cell(row, 13).value

#BRM Removed; As it is not entered in the spreadsheet
#17*9 fields, BRM excluded
query = """INSERT INTO T_BSP (
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

SMS_1_Mon_CPLY,
SMS_1_Mon_Tar_APP,
SMS_1_Mon_Tar_Rev,
SMS_1_Daily_Tar_APP,
SMS_1_Daily_Tar_Rev,
SMS_1_Act,
SMS_1_Cum,
SMS_1_MRate,
SMS_1_APP_Fulfill,

SMS_2_CC_Mon_CPLY,
SMS_2_CC_Mon_Tar_APP,
SMS_2_CC_Mon_Tar_Rev,
SMS_2_CC_Daily_Tar_APP,
SMS_2_CC_Daily_Tar_Rev,
SMS_2_CC_Act,
SMS_2_CC_Cum,
SMS_2_CC_MRate,
SMS_2_CC_APP_Fulfill,

BBM_ingot_Mon_CPLY,
BBM_ingot_Mon_Tar_APP,
BBM_ingot_Mon_Tar_Rev,
BBM_ingot_Daily_Tar_APP,
BBM_ingot_Daily_Tar_Rev,
BBM_Ingot_Act,
BBM_ingot_Cum,
BBM_ingot_MRate,
BBM_ingot_APP_Fulfill,

Rails_Mon_CPLY,
Rails_Mon_Tar_APP,
Rails_Mon_Tar_Rev,
Rails_Daily_Tar_APP,
Rails_Daily_Tar_Rev,
Rails_Act,
Rails_Cum,
Rails_MRate,
Rails_APP_Fulfill,

URM_Mon_CPLY,
URM_Mon_Tar_APP,
URM_Mon_Tar_Rev,
URM_Daily_Tar_APP,
URM_Daily_Tar_Rev,
URM_Act,
URM_Cum,
URM_MRate,
URM_APP_Fulfill,

MM_Mon_CPLY,
MM_Mon_Tar_APP,
MM_Mon_Tar_Rev,
MM_Daily_Tar_APP,
MM_Daily_Tar_Rev,
MM_Act,
MM_Cum,
MM_MRate,
MM_APP_Fulfill,

WRM_Mon_CPLY,
WRM_Mon_Tar_APP,
WRM_Mon_Tar_Rev,
WRM_Daily_Tar_APP,
WRM_Daily_Tar_Rev,
WRM_Act,
WRM_Cum,
WRM_MRate,
WRM_APP_Fulfill,

Plate_Mill_Mon_CPLY,
Plate_Mill_Mon_Tar_APP,
Plate_Mill_Mon_Tar_Rev,
Plate_Mill_Daily_Tar_APP,
Plate_Mill_Daily_Tar_Rev,
Plate_Mill_Act,
Plate_Mill_Cum,
Plate_Mill_MRate,
Plate_Mill_APP_Fulfill,

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

SMS_1_Mon_CPLY,
SMS_1_Mon_Tar_APP,
SMS_1_Mon_Tar_Rev,
SMS_1_Daily_Tar_APP,
SMS_1_Daily_Tar_Rev,
SMS_1_Act,
SMS_1_Cum,
SMS_1_MRate,
SMS_1_APP_Fulfill,

SMS_2_CC_Mon_CPLY,
SMS_2_CC_Mon_Tar_APP,
SMS_2_CC_Mon_Tar_Rev,
SMS_2_CC_Daily_Tar_APP,
SMS_2_CC_Daily_Tar_Rev,
SMS_2_CC_Act,
SMS_2_CC_Cum,
SMS_2_CC_MRate,
SMS_2_CC_APP_Fulfill,

BBM_Ingot_Mon_CPLY,
BBM_Ingot_Mon_Tar_APP,
BBM_Ingot_Mon_Tar_Rev,
BBM_Ingot_Daily_Tar_APP,
BBM_Ingot_Daily_Tar_Rev,
BBM_Ingot_Act,
BBM_Ingot_Cum,
BBM_Ingot_MRate,
BBM_Ingot_APP_Fulfill,

Rails_Mon_CPLY,
Rails_Mon_Tar_APP,
Rails_Mon_Tar_Rev,
Rails_Daily_Tar_APP,
Rails_Daily_Tar_Rev,
Rails_Act,
Rails_Cum,
Rails_MRate,
Rails_APP_Fulfill,

URM_Mon_CPLY,
URM_Mon_Tar_APP,
URM_Mon_Tar_Rev,
URM_Daily_Tar_APP,
URM_Daily_Tar_Rev,
URM_Act,
URM_Cum,
URM_MRate,
URM_APP_Fulfill,

MM_Mon_CPLY,
MM_Mon_Tar_APP,
MM_Mon_Tar_Rev,
MM_Daily_Tar_APP,
MM_Daily_Tar_Rev,
MM_Act,
MM_Cum,
MM_MRate,
MM_APP_Fulfill,

WRM_Mon_CPLY,
WRM_Mon_Tar_APP,
WRM_Mon_Tar_Rev,
WRM_Daily_Tar_APP,
WRM_Daily_Tar_Rev,
WRM_Act,
WRM_Cum,
WRM_MRate,
WRM_APP_Fulfill,

Plate_Mill_Mon_CPLY,
Plate_Mill_Mon_Tar_APP,
Plate_Mill_Mon_Tar_Rev,
Plate_Mill_Daily_Tar_APP,
Plate_Mill_Daily_Tar_Rev,
Plate_Mill_Act,
Plate_Mill_Cum,
Plate_Mill_MRate,
Plate_Mill_APP_Fulfill,

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

 
#print values

cursor.execute(query,values)
cursor.close();
database.commit()

database.close()

#print""
#print values
#print "Done !"

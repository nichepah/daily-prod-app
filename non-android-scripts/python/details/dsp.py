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

row = 22
Oven_Push_Mon_CPLY = sheet.cell(row, 4).value
oven_Push_Mon_Tar_APP = sheet.cell(row, 5).value
oven_Push_Mon_Tar_Rev = sheet.cell(row, 6).value
oven_Push_Daily_Tar_APP = sheet.cell(row, 7).value
oven_Push_Daily_Tar_Rev = sheet.cell(row, 8).value
Oven_Push_Act = sheet.cell(row, 9).value
Oven_Push_Cum = sheet.cell(row, 11).value
Oven_Push_MRate = sheet.cell(row, 12).value
Oven_Push_APP_Fulfill = sheet.cell(row, 13).value

row=23
Sinter_Mon_CPLY = sheet.cell(row, 4).value
Sinter_Mon_Tar_APP = sheet.cell(row, 5).value
Sinter_Mon_Tar_Rev = sheet.cell(row, 6).value
Sinter_Daily_Tar_APP = sheet.cell(row, 7).value
Sinter_Daily_Tar_Rev = sheet.cell(row, 8).value
Sinter_Act = sheet.cell(row, 9).value
Sinter_Cum = sheet.cell(row, 11).value
Sinter_MRate = sheet.cell(row, 12).value
Sinter_APP_Fulfill = sheet.cell(row, 13).value

row = 24
HM_Mon_CPLY = sheet.cell(row, 4).value
HM_Mon_Tar_APP = sheet.cell(row, 5).value
HM_Mon_Tar_Rev = sheet.cell(row, 6).value
HM_Daily_Tar_APP = sheet.cell(row, 7).value
HM_Daily_Tar_Rev = sheet.cell(row, 8).value
HM_Act = sheet.cell(row, 9).value
HM_Cum = sheet.cell(row, 11).value
HM_MRate = sheet.cell(row, 12).value
HM_APP_Fulfill = sheet.cell(row, 13).value

row = 25
PI_Mon_CPLY = sheet.cell(row, 4).value
PI_Mon_Tar_APP = sheet.cell(row, 5).value
PI_Mon_Tar_Rev = sheet.cell(row, 6).value
PI_Daily_Tar_APP = sheet.cell(row, 7).value
PI_Daily_Tar_Rev = sheet.cell(row, 8).value
PI_Act = sheet.cell(row, 9).value
PI_Cum = sheet.cell(row, 11).value
PI_MRate = sheet.cell(row, 12).value
PI_APP_Fulfill = sheet.cell(row, 13).value

row = 26
CS_Mon_CPLY = sheet.cell(row, 4).value
CS_Mon_Tar_APP = sheet.cell(row, 5).value
CS_Mon_Tar_Rev = sheet.cell(row, 6).value
CS_Daily_Tar_APP = sheet.cell(row, 7).value
CS_Daily_Tar_Rev = sheet.cell(row, 8).value
CS_Act = sheet.cell(row, 9).value
CS_Cum = sheet.cell(row, 11).value
CS_MRate = sheet.cell(row, 12).value
CS_APP_Fulfill = sheet.cell(row, 13).value

row = 27
CC_Billet_Mon_CPLY = sheet.cell(row, 4).value
CC_Billet_Mon_Tar_APP = sheet.cell(row, 5).value
CC_Billet_Mon_Tar_Rev = sheet.cell(row, 6).value
CC_Billet_Daily_Tar_APP = sheet.cell(row, 7).value
CC_Billet_Daily_Tar_Rev = sheet.cell(row, 8).value
CC_Billet_Act = sheet.cell(row, 9).value
CC_Billet_Cum = sheet.cell(row, 11).value
CC_Billet_MRate = sheet.cell(row, 12).value
CC_Billet_APP_Fulfill = sheet.cell(row, 13).value

row = 28
CC_Bloom_Mon_CPLY = sheet.cell(row, 4).value
CC_Bloom_Mon_Tar_APP = sheet.cell(row, 5).value
CC_Bloom_Mon_Tar_Rev = sheet.cell(row, 6).value
CC_Bloom_Daily_Tar_APP = sheet.cell(row, 7).value
CC_Bloom_Daily_Tar_Rev = sheet.cell(row, 8).value
CC_Bloom_Act = sheet.cell(row, 9).value
CC_Bloom_Cum = sheet.cell(row, 11).value
CC_Bloom_MRate = sheet.cell(row, 12).value
CC_Bloom_APP_Fulfill = sheet.cell(row, 13).value

row = 29
BRC_Mon_CPLY = sheet.cell(row, 4).value
BRC_Mon_Tar_APP = sheet.cell(row, 5).value
BRC_Mon_Tar_Rev = sheet.cell(row, 6).value
BRC_Daily_Tar_APP = sheet.cell(row, 7).value
BRC_Daily_Tar_Rev = sheet.cell(row, 8).value
BRC_Act = sheet.cell(row, 9).value
BRC_Cum = sheet.cell(row, 11).value
BRC_MRate = sheet.cell(row, 12).value
BRC_APP_Fulfill = sheet.cell(row, 13).value

row = 30
BRM_Mon_CPLY = sheet.cell(row, 4).value
BRM_Mon_Tar_APP = sheet.cell(row, 5).value
BRM_Mon_Tar_Rev = sheet.cell(row, 6).value
BRM_Daily_Tar_APP = sheet.cell(row, 7).value
BRM_Daily_Tar_Rev = sheet.cell(row, 8).value
BRM_Act = sheet.cell(row, 9).value
BRM_Cum = sheet.cell(row, 11).value
BRM_MRate = sheet.cell(row, 12).value
BRM_APP_Fulfill = sheet.cell(row, 13).value

row = 31
MM_Mon_CPLY = sheet.cell(row, 4).value
MM_Mon_Tar_APP = sheet.cell(row, 5).value
MM_Mon_Tar_Rev = sheet.cell(row, 6).value
MM_Daily_Tar_APP = sheet.cell(row, 7).value
MM_Daily_Tar_Rev = sheet.cell(row, 8).value
MM_Act = sheet.cell(row, 9).value
MM_Cum = sheet.cell(row, 11).value
MM_MRate = sheet.cell(row, 12).value
MM_APP_Fulfill = sheet.cell(row, 13).value

row = 32
SM_Mon_CPLY = sheet.cell(row, 4).value
SM_Mon_Tar_APP = sheet.cell(row, 5).value
SM_Mon_Tar_Rev = sheet.cell(row, 6).value
SM_Daily_Tar_APP = sheet.cell(row, 7).value
SM_Daily_Tar_Rev = sheet.cell(row, 8).value
SM_Act = sheet.cell(row, 9).value
SM_Cum = sheet.cell(row, 11).value
SM_MRate = sheet.cell(row, 12).value
SM_APP_Fulfill = sheet.cell(row, 13).value

row = 33
MSM_Mon_CPLY = sheet.cell(row, 4).value
MSM_Mon_Tar_APP = sheet.cell(row, 5).value
MSM_Mon_Tar_Rev = sheet.cell(row, 6).value
MSM_Daily_Tar_APP = sheet.cell(row, 7).value
MSM_Daily_Tar_Rev = sheet.cell(row, 8).value
MSM_Act = sheet.cell(row, 9).value
MSM_Cum = sheet.cell(row, 11).value
MSM_MRate = sheet.cell(row, 12).value
MSM_APP_Fulfill = sheet.cell(row, 13).value

row = 34
W_n_A_Mon_CPLY = sheet.cell(row, 4).value
W_n_A_Mon_Tar_APP = sheet.cell(row, 5).value
W_n_A_Mon_Tar_Rev = sheet.cell(row, 6).value
W_n_A_Daily_Tar_APP = sheet.cell(row, 7).value
W_n_A_Daily_Tar_Rev = sheet.cell(row, 8).value
W_n_A_Act = sheet.cell(row, 9).value
W_n_A_Cum = sheet.cell(row, 11).value
W_n_A_MRate = sheet.cell(row, 12).value
W_n_A_APP_Fulfill = sheet.cell(row, 13).value

row = 35
Semis_Mon_CPLY = sheet.cell(row, 4).value
Semis_Mon_Tar_APP = sheet.cell(row, 5).value
Semis_Mon_Tar_Rev = sheet.cell(row, 6).value
Semis_Daily_Tar_APP = sheet.cell(row, 7).value
Semis_Daily_Tar_Rev = sheet.cell(row, 8).value
Semis_Act = sheet.cell(row, 9).value
Semis_Cum = sheet.cell(row, 11).value
Semis_MRate = sheet.cell(row, 12).value
Semis_APP_Fulfill = sheet.cell(row, 13).value

row = 36
Fin_Steel_Mon_CPLY = sheet.cell(row, 4).value
Fin_Steel_Mon_Tar_APP = sheet.cell(row, 5).value
Fin_Steel_Mon_Tar_Rev = sheet.cell(row, 6).value
Fin_Steel_Daily_Tar_APP = sheet.cell(row, 7).value
Fin_Steel_Daily_Tar_Rev = sheet.cell(row, 8).value
Fin_Steel_Act = sheet.cell(row, 9).value
Fin_Steel_Cum = sheet.cell(row, 11).value
Fin_Steel_MRate = sheet.cell(row, 12).value
Fin_Steel_APP_Fulfill = sheet.cell(row, 13).value

row = 37
SS_Prod_Mon_CPLY = sheet.cell(row, 4).value
SS_Prod_Mon_Tar_APP = sheet.cell(row, 5).value
SS_Prod_Mon_Tar_Rev = sheet.cell(row, 6).value
SS_Prod_Daily_Tar_APP = sheet.cell(row, 7).value
SS_Prod_Daily_Tar_Rev = sheet.cell(row, 8).value
SS_Prod_Act = sheet.cell(row, 9).value
SS_Prod_Cum = sheet.cell(row, 11).value
SS_Prod_MRate = sheet.cell(row, 12).value
SS_Prod_APP_Fulfill = sheet.cell(row, 13).value

row = 38
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
query = """INSERT INTO T_DSP (
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

CC_Billet_Mon_CPLY,
CC_Billet_Mon_Tar_APP,
CC_Billet_Mon_Tar_Rev,
CC_Billet_Daily_Tar_APP,
CC_Billet_Daily_Tar_Rev,
CC_Billet_Act,
CC_Billet_Cum,
CC_Billet_MRate,
CC_Billet_APP_Fulfill,

CC_Bloom_Mon_CPLY,
CC_Bloom_Mon_Tar_APP,
CC_Bloom_Mon_Tar_Rev,
CC_Bloom_Daily_Tar_APP,
CC_Bloom_Daily_Tar_Rev,
CC_Bloom_Act,
CC_Bloom_Cum,
CC_Bloom_MRate,
CC_Bloom_APP_Fulfill,

BRC_Mon_CPLY,
BRC_Mon_Tar_APP,
BRC_Mon_Tar_Rev,
BRC_Daily_Tar_APP,
BRC_Daily_Tar_Rev,
BRC_Act,
BRC_Cum,
BRC_MRate,
BRC_APP_Fulfill,

BRM_Mon_CPLY,
BRM_Mon_Tar_APP,
BRM_Mon_Tar_Rev,
BRM_Daily_Tar_APP,
BRM_Daily_Tar_Rev,
BRM_Act,
BRM_Cum,
BRM_MRate,
BRM_APP_Fulfill,

MM_Mon_CPLY,
MM_Mon_Tar_APP,
MM_Mon_Tar_Rev,
MM_Daily_Tar_APP,
MM_Daily_Tar_Rev,
MM_Act,
MM_Cum,
MM_MRate,
MM_APP_Fulfill,

SM_Mon_CPLY,
SM_Mon_Tar_APP,
SM_Mon_Tar_Rev,
SM_Daily_Tar_APP,
SM_Daily_Tar_Rev,
SM_Act,
SM_Cum,
SM_MRate,
SM_APP_Fulfill,

MSM_Mon_CPLY,
MSM_Mon_Tar_APP,
MSM_Mon_Tar_Rev,
MSM_Daily_Tar_APP,
MSM_Daily_Tar_Rev,
MSM_Act,
MSM_Cum,
MSM_MRate,
MSM_APP_Fulfill,

W_n_A_Mon_CPLY,
W_n_A_Mon_Tar_APP,
W_n_A_Mon_Tar_Rev,
W_n_A_Daily_Tar_APP,
W_n_A_Daily_Tar_Rev,
W_n_A_Act,
W_n_A_Cum,
W_n_A_MRate,
W_n_A_APP_Fulfill,

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

CC_Billet_Mon_CPLY,
CC_Billet_Mon_Tar_APP,
CC_Billet_Mon_Tar_Rev,
CC_Billet_Daily_Tar_APP,
CC_Billet_Daily_Tar_Rev,
CC_Billet_Act,
CC_Billet_Cum,
CC_Billet_MRate,
CC_Billet_APP_Fulfill,

CC_Bloom_Mon_CPLY,
CC_Bloom_Mon_Tar_APP,
CC_Bloom_Mon_Tar_Rev,
CC_Bloom_Daily_Tar_APP,
CC_Bloom_Daily_Tar_Rev,
CC_Bloom_Act,
CC_Bloom_Cum,
CC_Bloom_MRate,
CC_Bloom_APP_Fulfill,

BRC_Mon_CPLY,
BRC_Mon_Tar_APP,
BRC_Mon_Tar_Rev,
BRC_Daily_Tar_APP,
BRC_Daily_Tar_Rev,
BRC_Act,
BRC_Cum,
BRC_MRate,
BRC_APP_Fulfill,

BRM_Mon_CPLY,
BRM_Mon_Tar_APP,
BRM_Mon_Tar_Rev,
BRM_Daily_Tar_APP,
BRM_Daily_Tar_Rev,
BRM_Act,
BRM_Cum,
BRM_MRate,
BRM_APP_Fulfill,

MM_Mon_CPLY,
MM_Mon_Tar_APP,
MM_Mon_Tar_Rev,
MM_Daily_Tar_APP,
MM_Daily_Tar_Rev,
MM_Act,
MM_Cum,
MM_MRate,
MM_APP_Fulfill,

SM_Mon_CPLY,
SM_Mon_Tar_APP,
SM_Mon_Tar_Rev,
SM_Daily_Tar_APP,
SM_Daily_Tar_Rev,
SM_Act,
SM_Cum,
SM_MRate,
SM_APP_Fulfill,

MSM_Mon_CPLY,
MSM_Mon_Tar_APP,
MSM_Mon_Tar_Rev,
MSM_Daily_Tar_APP,
MSM_Daily_Tar_Rev,
MSM_Act,
MSM_Cum,
MSM_MRate,
MSM_APP_Fulfill,

W_n_A_Mon_CPLY,
W_n_A_Mon_Tar_APP,
W_n_A_Mon_Tar_Rev,
W_n_A_Daily_Tar_APP,
W_n_A_Daily_Tar_Rev,
W_n_A_Act,
W_n_A_Cum,
W_n_A_MRate,
W_n_A_APP_Fulfill,

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

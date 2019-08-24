CREATE TABLE test.T_BSP_ACT_PRO (
Production_Date date NOT NULL,
Oven_Pushing int,
Sinter int,
HM int,
PI int,
CS int,
SMS_1 int,
SMS_2_CC int,
BBM_ingot_rolling int,
Rails int,
URM int,
MM int,
WRM int,
Plate_Mill int,
BRM int,
Semis int,
Fin_Steel int,
SS_Prod int,
SS_Desp int,
PRIMARY KEY (Production_Date)  
);

CREATE TABLE test.T_DSP_ACT_PRO (
Production_Date date NOT NULL,
Oven_Pushing int,
Sinter int,
HM int,
PI int,
CS int,
CC_Billet int,
CC_Bloom int,
BRC int,
BRM int,
MM int,
SM int,
MSM int,
W_n_A int,
Semis int,
Fin_Steel int,
SS_Prod int,
SS_Desp int,
PRIMARY KEY (Production_Date)  
);

CREATE TABLE test.T_RSP_ACT_PRO (
Production_Date date NOT NULL,
Oven_Pushing int,
Sinter int,
HM int,
PI int,
CS int,
SMS1_CC int,
SMS2_CC int,
Caster_3 int,
Plate_Mill int,
New_PM int,
HSM int,
CR_Saleable int,
CRNO int,
Semis int,
Fin_Steel int,
SS_Prod int,
SS_Desp int,
PRIMARY KEY (Production_Date)  
);

CREATE TABLE test.T_BSL_ACT_PRO (
Production_Date date NOT NULL,
Oven_Pushing int,
Sinter int,
HM int,
PI int,
CS int,
SMS_1 int,
SMS2_CC int,
SM int,
HSM int,
CRM_1_2 int,
CRM_3 int,
CR_Saleable int,
Semis int,
Fin_Steel int,
SS_Prod int,
SS_Desp int,
PRIMARY KEY (Production_Date)  
);

CREATE TABLE test.T_ISP_ACT_PRO (
Production_Date date NOT NULL,
Oven_Pushing int,
HM int,
PI int,
CS int,
CC int,
Sinter int,
WRM int,
Bar_Mill int,
USM int,
Semis int,
Fin_Steel int,
SS_Prod int,
SS_Desp int,
PRIMARY KEY (Production_Date)  
);

CREATE TABLE test.T_ALL5_ACT_PRO (
Production_Date date NOT NULL,
Oven_Pushing int,
HM int,
PI int,
CS int,
CC int,
SS_Prod int,
SS_Desp int,
PRIMARY KEY (Production_Date)  
);

CREATE TABLE test.T_ASP_ACT_PRO (
Production_Date date NOT NULL,
CS int,
CC int,
SS_Prod int,
SS_Desp int,
PRIMARY KEY (Production_Date)  
);

CREATE TABLE test.T_SSP_ACT_PRO (
	Production_Date date NOT NULL,
	CS int,
	HRM int,
	SS_Prod int,
	SS_Desp int,
	PRIMARY KEY (Production_Date)
);

CREATE TABLE test.T_VIS_ACT_PRO (
Production_Date date NOT NULL,
HM int,
PI int,
CS int,
CC int,
SS_Prod int,
SS_Desp int,
PRIMARY KEY (Production_Date)  
);

CREATE TABLE test.T_SAI_ACT_PRO (
Production_Date date NOT NULL,
Oven_Pushing int,
HM int,
PI int,
CS int,
CC int,
SS_Prod int,
SS_Desp int,
PRIMARY KEY (Production_Date)  
);

CREATE USER 'test_updater'@'localhost' IDENTIFIED BY 'updater123';
GRANT SELECT, INSERT ON test.* TO 'test_updater'@'localhost';

CREATE USER 'test'@'localhost' IDENTIFIED BY 'test';
GRANT SELECT ON test.* TO 'test'@'localhost';

CREATE DATABASE sail_user;
CREATE TABLE sail_user.T_EMPLOYEE (
E_id VARCHAR(16) NOT NULL,
Passwd VARCHAR(255),
Email VARCHAR(255),
Unit VARCHAR(16),
Desig VARCHAR(16)
Mobile VARCHAR(16)
PRIMARY KEY (E_Id));

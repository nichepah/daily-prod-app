CREATE TABLE SAILPRO.T_ASP(
Production_Date date NOT NULL,

CS_Mon_CPLY int,
CS_Mon_Tar_APP int,
CS_Mon_Tar_Rev int,
CS_Daily_Tar_APP int,
CS_Daily_Tar_Rev int,
CS_Act int,
CS_Cum int,
CS_MRate int,
CS_APP_Fulfill int,

CC_Mon_CPLY int,
CC_Mon_Tar_APP int,
CC_Mon_Tar_Rev int,
CC_Daily_Tar_APP int,
CC_Daily_Tar_Rev int,
CC_Act int,
CC_Cum int,
CC_MRate int,
CC_APP_Fulfill int,

SS_Prod_Mon_CPLY int,
SS_Prod_Mon_Tar_APP int,
SS_Prod_Mon_Tar_Rev int,
SS_Prod_Daily_Tar_APP int,
SS_Prod_Daily_Tar_Rev int,
SS_Prod_Act int,
SS_Prod_Cum int,
SS_Prod_MRate int,
SS_Prod_APP_Fulfill int,

SS_Desp_Mon_CPLY int,
SS_Desp_Mon_Tar_APP int,
SS_Desp_Mon_Tar_Rev int,
SS_Desp_Daily_Tar_APP int,
SS_Desp_Daily_Tar_Rev int,
SS_Desp_Act int,
SS_Desp_Cum int,
SS_Desp_MRate int,
SS_Desp_APP_Fulfill int,
PRIMARY KEY (Production_Date)  
);


-- CREATE USER 'test_updater'@'localhost' IDENTIFIED BY 'updater123';
GRANT SELECT, INSERT ON SAILPRO.* TO 'test_updater'@'localhost';

-- CREATE USER 'test'@'localhost' IDENTIFIED BY 'test';
GRANT SELECT ON SAILPRO.* TO 'test'@'localhost';



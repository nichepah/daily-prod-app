CREATE TABLE SAILPRO.T_DSP(
Production_Date date NOT NULL,

Oven_Push_Mon_CPLY int,
oven_Push_Mon_Tar_APP int,
oven_Push_Mon_Tar_Rev int,
oven_Push_Daily_Tar_APP int,
oven_Push_Daily_Tar_Rev int,
Oven_Push_Act int,
Oven_Push_Cum int,
Oven_Push_MRate int,
Oven_Push_APP_Fulfill int,

Sinter_Mon_CPLY int,
Sinter_Mon_Tar_APP int,
Sinter_Mon_Tar_Rev int,
Sinter_Daily_Tar_APP int,
Sinter_Daily_Tar_Rev int,
Sinter_Act int,
Sinter_Cum int,
Sinter_MRate int,
Sinter_APP_Fulfill int,

HM_Mon_CPLY int,
HM_Mon_Tar_APP int,
HM_Mon_Tar_Rev int,
HM_Daily_Tar_APP int,
HM_Daily_Tar_Rev int,
HM_Act int,
HM_Cum int,
HM_MRate int,
HM_APP_Fulfill int,

PI_Mon_CPLY int,
PI_Mon_Tar_APP int,
PI_Mon_Tar_Rev int,
PI_Daily_Tar_APP int,
PI_Daily_Tar_Rev int,
PI_Act int,
PI_Cum int,
PI_MRate int,
PI_APP_Fulfill int,

CS_Mon_CPLY int,
CS_Mon_Tar_APP int,
CS_Mon_Tar_Rev int,
CS_Daily_Tar_APP int,
CS_Daily_Tar_Rev int,
CS_Act int,
CS_Cum int,
CS_MRate int,
CS_APP_Fulfill int,

CC_Billet_Mon_CPLY int,
CC_Billet_Mon_Tar_APP int,
CC_Billet_Mon_Tar_Rev int,
CC_Billet_Daily_Tar_APP int,
CC_Billet_Daily_Tar_Rev int,
CC_Billet_Act int,
CC_Billet_Cum int,
CC_Billet_MRate int,
CC_Billet_APP_Fulfill int,

CC_Bloom_Mon_CPLY int,
CC_Bloom_Mon_Tar_APP int,
CC_Bloom_Mon_Tar_Rev int,
CC_Bloom_Daily_Tar_APP int,
CC_Bloom_Daily_Tar_Rev int,
CC_Bloom_Act int,
CC_Bloom_Cum int,
CC_Bloom_MRate int,
CC_Bloom_APP_Fulfill int,

BRC_Mon_CPLY int,
BRC_Mon_Tar_APP int,
BRC_Mon_Tar_Rev int,
BRC_Daily_Tar_APP int,
BRC_Daily_Tar_Rev int,
BRC_Act int,
BRC_Cum int,
BRC_MRate int,
BRC_APP_Fulfill int,

BRM_Mon_CPLY int,
BRM_Mon_Tar_APP int,
BRM_Mon_Tar_Rev int,
BRM_Daily_Tar_APP int,
BRM_Daily_Tar_Rev int,
BRM_Act int,
BRM_Cum int,
BRM_MRate int,
BRM_APP_Fulfill int,

MM_Mon_CPLY int,
MM_Mon_Tar_APP int,
MM_Mon_Tar_Rev int,
MM_Daily_Tar_APP int,
MM_Daily_Tar_Rev int,
MM_Act int,
MM_Cum int,
MM_MRate int,
MM_APP_Fulfill int,

SM_Mon_CPLY int,
SM_Mon_Tar_APP int,
SM_Mon_Tar_Rev int,
SM_Daily_Tar_APP int,
SM_Daily_Tar_Rev int,
SM_Act int,
SM_Cum int,
SM_MRate int,
SM_APP_Fulfill int,

MSM_Mon_CPLY int,
MSM_Mon_Tar_APP int,
MSM_Mon_Tar_Rev int,
MSM_Daily_Tar_APP int,
MSM_Daily_Tar_Rev int,
MSM_Act int,
MSM_Cum int,
MSM_MRate int,
MSM_APP_Fulfill int,

W_n_A_Mon_CPLY int,
W_n_A_Mon_Tar_APP int,
W_n_A_Mon_Tar_Rev int,
W_n_A_Daily_Tar_APP int,
W_n_A_Daily_Tar_Rev int,
W_n_A_Act int,
W_n_A_Cum int,
W_n_A_MRate int,
W_n_A_APP_Fulfill int,


Semis_Mon_CPLY int,
Semis_Mon_Tar_APP int,
Semis_Mon_Tar_Rev int,
Semis_Daily_Tar_APP int,
Semis_Daily_Tar_Rev int,
Semis_Act int,
Semis_Cum int,
Semis_MRate int,
Semis_APP_Fulfill int,

Fin_Steel_Mon_CPLY int,
Fin_Steel_Mon_Tar_APP int,
Fin_Steel_Mon_Tar_Rev int,
Fin_Steel_Daily_Tar_APP int,
Fin_Steel_Daily_Tar_Rev int,
Fin_Steel_Act int,
Fin_Steel_Cum int,
Fin_Steel_MRate int,
Fin_Steel_APP_Fulfill int,

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


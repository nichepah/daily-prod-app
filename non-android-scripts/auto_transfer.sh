#!/bin/bash
# Written by Aneesh PA on 02/03/18
# Automates spreadsheets-to-mysql conversion
# Expects spreadsheets in ~/Documents/plant_reports

timestamp()
{
 date +"%Y-%m-%d %T"
}

LOG="/home/pa/sail-production-web/18_19/log/log.txt"

for f in $(find /home/pa/Documents/plant_reports/*.xlsx 2>>$LOG)
do
  echo $(timestamp) :"======Processing $f ============"; >> $LOG
  /home/pa/sail-production-web/python/excel_to_mysql_all5.py $f 2>>$LOG
  /home/pa/sail-production-web/python/excel_to_mysql_asp.py $f 2>>$LOG
  /home/pa/sail-production-web/python/excel_to_mysql_bsl.py $f 2>>$LOG
  /home/pa/sail-production-web/python/excel_to_mysql_bsp.py $f 2>>$LOG
  /home/pa/sail-production-web/python/excel_to_mysql_dsp.py $f 2>>$LOG
  /home/pa/sail-production-web/python/excel_to_mysql_isp.py $f 2>>$LOG
  /home/pa/sail-production-web/python/excel_to_mysql_rsp.py $f 2>>$LOG
  /home/pa/sail-production-web/python/excel_to_mysql_sai.py $f 2>>$LOG
  /home/pa/sail-production-web/python/excel_to_mysql_ssp.py $f 2>>$LOG
  /home/pa/sail-production-web/python/excel_to_mysql_vis.py $f 2>>$LOG
  #/bin/mv $f /home/pa/Documents/plant_reports/bak/$(/usr/bin/basename $f)	
done

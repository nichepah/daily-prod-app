#!/bin/bash
# Written by Aneesh PA on 05/04/18
# Automates spreadsheets-to-mysql conversion; transfers all detailed process params
# Expects spreadsheets in ~/Documents/plant_reports

timestamp()
{
 date +"%Y-%m-%d %T"
}

LOG="/home/pa/sail-production-web/log/log_details.txt"

for f in $(find /home/pa/Documents/plant_reports/*.xlsx 2>>$LOG)
do
  echo $(timestamp) :"======Processing $f ============"; >> $LOG
  /home/pa/sail-production-web/python/details/all5.py $f 2>>$LOG
  /home/pa/sail-production-web/python/details/asp.py $f 2>>$LOG
  /home/pa/sail-production-web/python/details/bsl.py $f 2>>$LOG
  /home/pa/sail-production-web/python/details/bsp.py $f 2>>$LOG
  /home/pa/sail-production-web/python/details/dsp.py $f 2>>$LOG
  /home/pa/sail-production-web/python/details/isp.py $f 2>>$LOG
  /home/pa/sail-production-web/python/details/rsp.py $f 2>>$LOG
  /home/pa/sail-production-web/python/details/sai.py $f 2>>$LOG
  /home/pa/sail-production-web/python/details/ssp.py $f 2>>$LOG
  /home/pa/sail-production-web/python/details/vis.py $f 2>>$LOG
  /bin/mv $f /home/pa/Documents/plant_reports/bak/$(/usr/bin/basename $f)	
done

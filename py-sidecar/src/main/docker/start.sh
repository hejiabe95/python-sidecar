#!/bin/bash
echo "Step1----------------startup the python program!"
nohup python3 -u /python/main.py > /tmp/main.log 2>&1 &
#ps aux |grep main |grep -q -v grep
#PROCESS_1_STATUS=$?
#echo "main status..."
#echo $PROCESS_1_STATUS
#if [ $PROCESS_1_STATUS -ne 0 ]; then
#echo "Failed to start my_first_process: $PROCESS_1_STATUS"
#exit $PROCESS_1_STATUS
#fi
#sleep 5
# Start the second process
echo "Step2----------------startup the sidecar program!"
nohup java -jar /app.jar > /tmp/app.log 2>&1 &
#ps aux |grep app |grep -q -v grep
#PROCESS_2_STATUS=$?
#echo "thread2 status..."
#echo $PROCESS_2_STATUS
#if [ $PROCESS_2_STATUS -ne 0 ]; then
#echo "Failed to start my_second_process: $PROCESS_2_STATUS"
#exit $PROCESS_2_STATUS
#fi
# 每隔60秒检查进程是否运行
#while sleep 60; do
#ps aux |grep main |grep -q -v grep
#PROCESS_1_STATUS=$?
#ps aux |grep app |grep -q -v grep
#PROCESS_2_STATUS=$?
## If the greps above find anything, they exit with 0 status
## If they are not both 0, then something is wrong
#if [ $PROCESS_1_STATUS -ne 0 -o $PROCESS_2_STATUS -ne 0 ]; then
#echo "One of the processes has already exited."
#exit 1
#fi
echo "Step3----------------show the log of python!"
tail -f /tmp/main.log
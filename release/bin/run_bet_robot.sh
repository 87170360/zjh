#!/bin/bash

kill_robot_nu=0


while true 
do 
	ps -Af  >bet_client.txt
	cat bet_client.txt | grep bet_client > /dev/null 

	if [[ $? == "0" ]]
	then 
		echo `date` "Bet Client Ok"	
	else 
		echo `date` "Resteart Bet Client"
		a=$(($RANDOM%10+10))
		b=$(($a+4))
		for((i=$a;i<$b;i++)) 
		do 
			./bin/bet_client 127.0.0.1  10000 $i >/dev/null & 
		done 
	fi
	
	kill_robot_nu=$(( $kill_robot_nu + 1))
	sleep 25

	if [[ "$kill_robot_nu" -gt "120" ]] 
	then 
		echo `date` "Kill All Client"
		kill `cat bet_client.txt |grep bet_client |awk '{ print $2}'`
		kill_robot_nu=0
	fi
	sleep 5



done 






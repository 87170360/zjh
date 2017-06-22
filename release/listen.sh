#!/bin/bash 

conf_dir="./conf/"
pid_dir="./pid/"
log_dir="./log/"

bin_dir="./bin/"
crash_dir="./crash"

normal_venue_low_nu=10 
normal_venue_middle_nu=5 
normal_venue_high_nu=2 
normal_venue_rich_nu=2

prop_venue_low_nu=2 
prop_venue_middle_nu=2 
prop_venue_high_nu=2 

taotai_venue_low_nu=2 
taotai_venue_middle_nu=2 
taotai_venue_high_nu=2 

process_info=`ps -Af`
output_dev="crash/run.csh"


while true 
do 
	ps -Af  >temp.txt
	echo `date` start listening 

	#normal venue  low 
	for ((i=0; i<$normal_venue_low_nu; i++)) 
	do 
		name="${bin_dir}zjhsvr -f ${conf_dir}normal_zjhsvr_low${i}.conf" 
		#echo $name
		cat temp.txt | grep "$name" >${output_dev}
		if [[  $? -ne "0" ]]
		then 
			echo `date` $name [[Crach]] Restart
			$name>>${output_dev} &
		fi
	done 

	#normal venue middle 
	for ((i=0; i<$normal_venue_middle_nu; i++)) 
	do 
		name="${bin_dir}zjhsvr -f ${conf_dir}normal_zjhsvr_middle${i}.conf" 
		#echo $name
		cat temp.txt | grep "$name" >${output_dev}
		if [[  $? -ne "0" ]]
		then 
			echo `date` $name [[Crach]] Restart
			$name>>${output_dev} &
		fi
	done 

	#normal venue high
	for ((i=0; i<$normal_venue_high_nu; i++)) 
	do 
		name="${bin_dir}zjhsvr -f ${conf_dir}normal_zjhsvr_high${i}.conf" 
		#echo $name
		cat temp.txt | grep "$name" >${output_dev}
		if [[  $? -ne "0" ]]
		then 
			echo `date` $name [[Crach]] Restart
			$name>>${output_dev} &
		fi
	done 

	#normal venue rich 
	for ((i=0; i<$normal_venue_rich_nu; i++)) 
	do 
		name="${bin_dir}zjhsvr -f ${conf_dir}normal_zjhsvr_rich${i}.conf" 
		#echo $name
		cat temp.txt | grep "$name" >${output_dev}
		if [[  $? -ne "0" ]]
		then 
			echo `date` $name [[Crach]] Restart
			$name>>${output_dev} &
		fi
	done 


	#normal venue low 
	for ((i=0; i<$prop_venue_low_nu; i++)) 
	do 
		name="${bin_dir}zjhsvr -f ${conf_dir}prop_zjhsvr_low${i}.conf" 
		#echo $name
		cat temp.txt | grep "$name" >${output_dev}
		if [[  $? -ne "0" ]]
		then 
			echo `date` $name [[Crach]] Restart
			$name>>${output_dev} &
		fi
	done 


	#normal venue middle 
	for ((i=0; i<$prop_venue_middle_nu; i++)) 
	do 
		name="${bin_dir}zjhsvr -f ${conf_dir}prop_zjhsvr_middle${i}.conf" 
		#echo $name
		cat temp.txt | grep "$name" >${output_dev}
		if [[  $? -ne "0" ]]
		then 
			echo `date` $name [[Crach]] Restart
			$name>>${output_dev} &
		fi
	done 


	#normal venue high
	for ((i=0; i<$prop_venue_high_nu; i++)) 
	do 
		name="${bin_dir}zjhsvr -f ${conf_dir}prop_zjhsvr_high${i}.conf" 
		#echo $name
		cat temp.txt | grep "$name" >${output_dev}
		if [[  $? -ne "0" ]]
		then 
			echo `date` $name [[Crach]] Restart
			$name>>${output_dev} &
		fi
	done 





	#lottery
	name="${bin_dir}lottery -f ${conf_dir}lottery.conf"
	#echo $name
	cat temp.txt | grep "$name" >${output_dev}
	if [[  $? -ne  "0" ]]
	then 
		echo `date` $name [[Crach]] Restart
		$name>>${output_dev} &
	fi

	#speaker 
	name="${bin_dir}speaker -f ${conf_dir}speaker.conf"
	cat temp.txt | grep "$name" >${output_dev}
	if [[  $? -ne "0" ]]
	then 
		echo `date` $name [[Crach]] Restart
		$name>>${output_dev} &
	fi


	#allkill 
	name="${bin_dir}allkill -f ${conf_dir}allkill.conf"
	cat temp.txt | grep "$name" >${output_dev}
	if [[  $? -ne "0" ]]
	then 
		echo `date` $name [[Crach]] Restart
		$name>>${output_dev} &
	fi

	#beauty 
	name="${bin_dir}beauty -f ${conf_dir}beauty.conf"
	cat temp.txt | grep "$name" >${output_dev}
	if [[  $? -ne "0" ]]
	then 
		echo `date` $name [[Crach]] Restart
		$name>>${output_dev} &
	fi

	sleep 30




done 



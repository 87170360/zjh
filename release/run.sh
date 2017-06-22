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

output_dev="crash/run.csh"

#check dir exist 
for dir in $conf_dir $pid_dir $log_dir $crash_dir;
do
	if [ ! -d "$dir" ]
	then 
		echo "Create Dir $dir"
		mkdir $dir 
	fi
done 

#start  normal venue low 
for ((i=0; i<$normal_venue_low_nu; i++)) 
do 
	echo "Start ${bin_dir}zjhsvr -f  ${conf_dir}normal_zjhsvr_low${i}.conf"
	${bin_dir}zjhsvr -f ${conf_dir}normal_zjhsvr_low${i}.conf>>${output_dev} &
done 

#start  normal venue middle
for ((i=0; i<$normal_venue_middle_nu; i++)) 
do 
	echo "Start ${bin_dir}zjhsvr -f  ${conf_dir}normal_zjhsvr_middle${i}.conf "
	${bin_dir}zjhsvr -f ${conf_dir}normal_zjhsvr_middle${i}.conf>>${output_dev} &
done 


#start  normal venue high
for ((i=0; i<$normal_venue_high_nu; i++)) 
do 
	echo "Start ${bin_dir}zjhsvr -f  ${conf_dir}normal_zjhsvr_high${i}.conf "
	${bin_dir}zjhsvr -f ${conf_dir}normal_zjhsvr_high${i}.conf >>${output_dev} &
done 

#start normal venue  rich
for ((i=0; i<$normal_venue_rich_nu; i++)) 
do 
	echo "Start ${bin_dir}zjhsvr -f  ${conf_dir}normal_zjhsvr_rich${i}.conf "
	${bin_dir}zjhsvr -f ${conf_dir}normal_zjhsvr_rich${i}.conf >>${output_dev} &
done 


#start prop venue low 
for ((i=0; i<$prop_venue_low_nu; i++)) 
do 
	echo "Start ${bin_dir}zjhsvr -f  ${conf_dir}prop_zjhsvr_low${i}.conf "
	${bin_dir}zjhsvr -f ${conf_dir}prop_zjhsvr_low${i}.conf>>${output_dev} &

done 


#start prop venue middle
for ((i=0; i<$prop_venue_middle_nu; i++)) 
do 
	echo "Start ${bin_dir}zjhsvr -f  ${conf_dir}prop_zjhsvr_middle${i}.conf "
	${bin_dir}zjhsvr -f ${conf_dir}prop_zjhsvr_middle${i}.conf>>${output_dev}  &

done 

#start prop venue high
for ((i=0; i<$prop_venue_high_nu; i++)) 
do 
	echo "${bin_dir}zjhsvr -f  ${conf_dir}prop_zjhsvr_high${i}.conf "
	${bin_dir}zjhsvr -f ${conf_dir}prop_zjhsvr_high${i}.conf>>${output_dev} &
done 



#start Lottery 
echo "Start Lottery"
${bin_dir}lottery -f ${conf_dir}lottery.conf>>${output_dev} &

#Start Speaker 
echo "Start Speaker" 
${bin_dir}speaker -f ${conf_dir}speaker.conf>>${output_dev} &

#Start allkill 
echo "All Kill"
${bin_dir}allkill -f ${conf_dir}allkill.conf>>${output_dev} &

#start beauty 
echo "All beauty"
${bin_dir}beauty -f ${conf_dir}beauty.conf>>${output_dev} &












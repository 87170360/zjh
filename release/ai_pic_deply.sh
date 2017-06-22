#!/bin/bash


pic_root="zjhimage"


i=10
for filename in `ls pic`
do
	name="image_"$i".png"
	echo $name
	md5_str=`echo -n $name | md5sum`
	#echo $md5_str
	dir_name="${md5_str:0:2}/${md5_str:2:2}"

	if [ ! -d "$dir_name" ]
	then
		mkdir -p  "$pic_root/$dir_name" 
	fi

	cp "pic/$filename" "$pic_root/$dir_name/$name"
	((i=i+1))

done 



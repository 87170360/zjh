
build:
	make -C libxtnet
	make -C libxtgame
	make -C lottery 
	make -C speaker 
	make -C libzjh  
	make -C zjhsvr 
	make -C robot
	make -C allkill
	make -C beauty
	make -C party


release: build
	cp lottery/lottery  ../release/bin
	cp speaker/speaker  ../release/bin
	cp zjhsvr/zjhsvr 	../release/bin
	cp robot/robots		../release/bin
	cp allkill/allkill  ../release/bin
	cp beauty/beauty  ../release/bin
	cp party/party  ../release/bin

clean :
	make -C lottery  clean
	make -C speaker clean 
	make -C libzjh clean
	make -C zjhsvr  clean 
	make -C robot 	clean
	make -C allkill  clean
	make -C beauty clean
	make -C party clean

cp : build
	cp -f lottery/lottery /data/game/bin
	cp -f speaker/speaker /data/game/bin
	cp -f zjhsvr/zjhsvr /data/game/bin
	cp -f robot/robots /data/game/bin
	cp -f allkill/allkill /data/game/bin
	cp -f beauty/beauty /data/game/bin
	cp -f party/party /data/game/bin

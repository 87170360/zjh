#coding=utf-8
#Normal Venue 

import types

#conf_dir="/etc/zjh/conf/"
conf_dir="./conf/"
pid_dir="./pid/"
log_dir="./log/"


def DictToJson(dict_content):
	list_item=[]
	for (k,v) in dict_content.items():
		str_k=""
		if type(k) is types.StringType: 
			str_k="\"%s\""%k
		else:
			str_k=str(k)
	
		if type(v) is types.StringType:
			str_v="\"%s\""%v
		elif type(v) is types.DictType:
			str_v=DictToJson(v)
		else:
			str_v=str(v)

		list_item.append(str_k+":"+str_v)

	result_str=",".join(list_item)

	return  "{"+result_str+"}"




venue_cfg={
		"normal":{
			"low": {
				"port": { "start":9200, 	 "nu":10, "name":"low",   "host":"0.0.0.0" },
				"table":{
					"begin": 1, "end": 1000,
					"vid": 1, "zid": 9100,
					"type": 1,
					"min_money": 300, "max_money": 0,
					"base_money": 300,
					"min_round" : 3, "max_round" : 20,
					"fee" : "0.1",
					"lose_exp" : 0, "win_exp" : 2
					},
				},

			"middle":{
				"port":{ "start":9220, "nu":5,  "name":"middle","host":"0.0.0.0" },
				"table":{
					"begin": 1, "end": 1000,
					"vid": 2,
					"zid": 9100,
					"type": 1,
					"min_money": 800, "max_money": 0,
					"base_money": 800,
					"min_round" : 3, "max_round" : 20,
					"fee" : "0.1",
					"lose_exp" : 0, "win_exp" : 4
					},
				},

			"high":{
				"port":{ "start":9240, 	 "nu":2 , "name":"high",  "host":"0.0.0.0" },
				"table":{
					"begin": 1, "end": 1000,
					"vid": 3,
					"zid": 9100,
					"type": 1,
					"min_money": 1500, "max_money": 0,
					"base_money": 1500,
					"min_round" : 3, "max_round" : 20,
					"fee" : "0.1",
					"lose_exp" : 0, "win_exp" : 8
					},
				},
			"rich":{
					"port":{ "start":9260,   "nu":2 , "name":"rich",  "host":"0.0.0.0" },
					"table":{
						"begin": 1, "end": 1000,
						"vid": 4, "zid": 9100,
						"type": 1,
						"min_money": 10000, "max_money": 0,
						"base_money": 10000,
						"min_round" : 3, "max_round" : 20,
						"fee" : "0.1",
						"lose_exp" : 0, "win_exp" : 16
						},
					}
			},



		"prop":{
				"low":{
					"port":{ "start":9400,    "nu":2,  "name":"low",    "host":"0.0.0.0" },
					"table":{
						"begin": 1, "end": 1000,
						"vid": 11, "zid": 9100,
						"type": 1,
						"min_money": 100, "max_money": 0,
						"base_money": 100,
						"min_round" : 3, "max_round" : 20,
						"fee" : "0.1",
						"lose_exp" : 0, "win_exp" : 2
						},
					},
				"middle":{
					"port":{ "start":9420, "nu":2,  "name":"middle", "host":"0.0.0.0" },
					"table":{
						"begin": 1, "end": 1000,
						"vid": 12, "zid": 9100,
						"type": 1,
						"min_money": 500, "max_money": 0,
						"base_money": 500,
						"min_round" : 3, "max_round" : 20,
						"fee" : "0.1",
						"lose_exp" : 0, "win_exp" : 4
						},
					},

				"high":{
					"port":{ "start":9440,   "nu":2 , "name":"high",   "host":"0.0.0.0" },
					"table":{
						"begin": 1, "end": 1000,
						"vid": 13, "zid": 9100,
						"type": 1,
						"min_money": 1000, "max_money": 0,
						"base_money": 1000,
						"min_round" : 3, "max_round" : 20,
						"fee" : "0.1",
						"lose_exp" : 0, "win_exp" : 8
						}
					},
				},
		}





lottery_cfg={
		"host":"0.0.0.0",
		"port":9100,
		"lottery_money":20000
		}

speaker_cfg={
		"host":"0.0.0.0",
		"port":9000 ,
		"speaker_money":5000,
		}


sql_cfg={
		"host":"127.0.0.1",
		"port":3306,
		"user":"zjh_game",
		"pass":"zjh_game",
		"dbname":"zjh_game"
		}




all_kill_cfg={
		"game":{"host":"0.0.0.0","port":10000},
		"venue":{
			"id":0,
			"base_money":10000,
			"ask_role_min":50000000,
			"sys_fee":0.04,
			"un_role_limit":30000000,
			"rottle_min_open_money":1000000,
			"role_another_radio":30,
			"sys_role":{
				"name":"系统女王",
				"avatar":"image_0.png",
				"uid":0,
				"sex":2,
				"money":999999999
				},
			"enter_chat":"欢迎来到万人场，希望你玩得愉快。",
			"chat_role":{
				"name":"系统女王",
				"avatar":"image_0.png",
				"uid":0,
				"sex":2,
				},
			"rottle_radio":{
				"bao_zhi":0.5,
				"shun_jin":0.4,
				"jin_hua":0.3,
				"win_rottle_fee":0.011
				},
			"game_history_nu":10
			}
		}


beauty_cfg={
		"game":{"host":"0.0.0.0","port":11000},
		"venue":{
			"base_money":10000,
			"middle_radio":5,
			"min_bet_money":100000,
			"fee":0.05,
			"game_history_nu":10
			}

		}



sub_redis_cfg={
		"host":"127.0.0.1",
		"portStart":6200,
		"nu":1,
		"pass":"zjh_pass"
		}

pub_redis_cfg={
		"host":"127.0.0.1",
		"portStart":6200,
		"nu":1,
		"pass":"zjh_pass"
		}



data_redis_cfg={
		"host":"127.0.0.1",
		"portStart":6000,
		"nu":10,
		"pass":"zjh_pass"
		}

eventlog_redis_cfg={
		"host":"127.0.0.1",
		"port":6200,
		"pass":"zjh_pass"
		}

cache_redis_cfg={
		"host":"127.0.0.1",
		"port":6100,
		"pass":"zjh_pass"
		}

speaker_redis_cfg={
		"host":"127.0.0.1",
		"port":6200,
		"pass":"zjh_pass"
		}


logfile_cfg={
		"level": 5,
		"console": 0,
		"rotate": 1,
		"max_size": 1073741824,
		"max_file": 10
		}


game_template_str="""\t"game":{ "host":"%s", "port":%d }"""

redis_template_str="""{ "host":"%s", "port":%d, "pass":"%s" }"""

log_template_str="""\t"log":{"log_file":"%s","level":%d,"console":%d,"rotate":%d,"max_size":%d,"max_file":%d}"""







data_redis_str="""\t"main-db":[\n"""
str_list=[]
for i in range(data_redis_cfg["portStart"],data_redis_cfg["portStart"]+data_redis_cfg["nu"]):
	str_list.append("\t\t"+redis_template_str%(data_redis_cfg["host"],i,data_redis_cfg["pass"]))
data_redis_str+=",\n".join(str_list)
data_redis_str+="\n\t]"



sub_redis_str="""\t"sub-db":[\n"""
str_list=[]
for i in range(sub_redis_cfg["portStart"],sub_redis_cfg["portStart"]+sub_redis_cfg["nu"]):
	str_list.append("\t\t"+redis_template_str%(sub_redis_cfg["host"],i,sub_redis_cfg["pass"]))

sub_redis_str+=",\n".join(str_list)
sub_redis_str+="\n\t]"


pub_redis_str="""\t"pub-db":[\n"""
str_list=[]
for i in range(pub_redis_cfg["portStart"],pub_redis_cfg["portStart"]+pub_redis_cfg["nu"]):
	str_list.append( "\t\t"+redis_template_str%(pub_redis_cfg["host"],i,pub_redis_cfg["pass"]))

pub_redis_str+=",\n".join(str_list)
pub_redis_str+="\n\t]"



eventlog_redis_str="""\t"eventlog-db":{"host":"%s","port":%d,"pass":"%s"}"""%(eventlog_redis_cfg["host"],eventlog_redis_cfg["port"],eventlog_redis_cfg["pass"])


cache_redis_str="""\t"cache-db":{"host":"%s","port":%d,"pass":"%s"}"""%(cache_redis_cfg["host"],cache_redis_cfg["port"],cache_redis_cfg["pass"])

speaker_redis_str="""\t"speaker-db":{"host":"%s","port":%d,"pass":"%s"}"""%(speaker_redis_cfg["host"],speaker_redis_cfg["port"],speaker_redis_cfg["pass"])









#generate venue normal file 

def FileContent_CreateNormalAndProp(venue_name,info):
	for k,v in info.items():
		port=v["port"]
		for i in range(port["start"],port["start"]+port["nu"]):
			name=venue_name+"_zjhsvr_"+k+str(i-port["start"])

			file_content="{\n"

			#self 
			file_content+="""\t"self":"%s" """%(conf_dir+name+".conf")+",\n"


			#pid 
			file_content+="""\t"pid_file":"%s" """%(pid_dir+name+".pid")+",\n"

			#log 
			log_str=log_template_str%(log_dir+name+".log",logfile_cfg["level"],logfile_cfg["console"],logfile_cfg["rotate"],logfile_cfg["max_size"],logfile_cfg["max_file"])

			file_content+=log_str+",\n"


			#game 
			file_content+=game_template_str%(port["host"],i)+",\n"

			#redis
			file_content+=data_redis_str+",\n"

			#event log 
			file_content+=eventlog_redis_str+",\n"

			file_content+=cache_redis_str+",\n"

			table_str="\t\"tables\":{"
			for tk,tv in v["table"].items():
				if type(tv) == str:
					table_str+=""""%s":"%s","""%(tk,tv)
				else :
					table_str+=""""%s":%d,"""%(tk,tv)

			table_str+=""""xxxx":"xxxx"}\n"""

			file_content+=table_str

			file_content+="}\n"



			fd=open(conf_dir+name+".conf","w+")
			fd.write(file_content)
			fd.close()

			print file_content


def FileContent_CreateLottery(cfg):
	name="lottery"

	file_content="{\n"

	#pid 
	file_content+="""\t"pid_file":"%s" """%(pid_dir+name+".pid")+",\n"

	#log 
	log_str=log_template_str%(log_dir+name+".log",logfile_cfg["level"],logfile_cfg["console"],logfile_cfg["rotate"],logfile_cfg["max_size"],logfile_cfg["max_file"])
	file_content+=log_str+",\n"

	#server 
	file_content+="""\t"server":{"host":"%s","port":%d}"""%(cfg["host"],cfg["port"])+",\n"

	#user 
	file_content+="""\t"user":{"lottery_money":%d}"""%(cfg["lottery_money"])+",\n"


	#redis
	file_content+=data_redis_str+",\n"

	#event log 
	file_content+=eventlog_redis_str+",\n"
	file_content+=cache_redis_str+"\n"

	file_content+="}\n"

	fd=open(conf_dir+name+".conf","w+")
	fd.write(file_content)
	fd.close()


def FileContent_CreateSpeaker(cfg):
	name="speaker"

	file_content="{\n"

	#pid 
	file_content+="""\t"pid_file":"%s" """%(pid_dir+name+".pid")+",\n"

	#log 
	log_str=log_template_str%(log_dir+name+".log",logfile_cfg["level"],logfile_cfg["console"],logfile_cfg["rotate"],logfile_cfg["max_size"],logfile_cfg["max_file"])
	file_content+=log_str+",\n"

	#server 
	file_content+="""\t"server":{"host":"%s","port":%d}"""%(cfg["host"],cfg["port"])+",\n"

	#user 
	file_content+="""\t"user":{"speaker_money":%d}"""%(cfg["speaker_money"])+",\n"


	#data redis
	file_content+=data_redis_str+ ",\n"

	#sub_redis 
	file_content+=sub_redis_str + ",\n"

	#pub_redis 
	file_content+=pub_redis_str + ",\n"






	#event log 
	file_content+=eventlog_redis_str+"\n"

	file_content+="}\n"

	fd=open(conf_dir+name+".conf","w+")
	fd.write(file_content)
	fd.close()


def FileContent_CreateAllKill(cfg):
	name="allkill"

	file_content="{\n"

	#self 
	file_content+="""\t"self":"%s" """%(conf_dir+name+".conf")+",\n"

	#pid 
	file_content+="""\t"pid_file":"%s" """%(pid_dir+name+".pid")+",\n"

	#log 
	log_str=log_template_str%(log_dir+name+".log",logfile_cfg["level"],logfile_cfg["console"],logfile_cfg["rotate"],logfile_cfg["max_size"],logfile_cfg["max_file"])

	file_content+=log_str+",\n"


	#game 
	file_content+=game_template_str%(cfg["game"]["host"],cfg["game"]["port"])+",\n"

	#redis
	file_content+=data_redis_str+",\n"
	file_content+=cache_redis_str+",\n"
	file_content+=speaker_redis_str+",\n"


	#event log 
	file_content+=eventlog_redis_str+",\n"

	file_content+="\t\"venue\":"+DictToJson(cfg["venue"])+",\n"
	file_content+="\t\"sql-db\":"+DictToJson(sql_cfg)+"\n"

	file_content+="}"

	fd=open(conf_dir+name+".conf","w+")
	fd.write(file_content)
	fd.close()


def FileContent_CreateAllBeauty(cfg):
	name="beauty"

	file_content="{\n"

	#self 
	file_content+="""\t"self":"%s" """%(conf_dir+name+".conf")+",\n"

	#pid 
	file_content+="""\t"pid_file":"%s" """%(pid_dir+name+".pid")+",\n"

	#log 
	log_str=log_template_str%(log_dir+name+".log",logfile_cfg["level"],logfile_cfg["console"],logfile_cfg["rotate"],logfile_cfg["max_size"],logfile_cfg["max_file"])

	file_content+=log_str+",\n"


	#game 
	file_content+=game_template_str%(cfg["game"]["host"],cfg["game"]["port"])+",\n"

	#redis
	file_content+=data_redis_str+",\n"


	#event log 
	file_content+=eventlog_redis_str+",\n"
	file_content+=cache_redis_str+",\n"
	file_content+=speaker_redis_str+",\n"

	file_content+="\t\"venue\":"+DictToJson(cfg["venue"])+",\n"
	file_content+="\t\"sql-db\":"+DictToJson(sql_cfg)+"\n"

	file_content+="}"

	fd=open(conf_dir+name+".conf","w+")
	fd.write(file_content)
	fd.close()





FileContent_CreateNormalAndProp("normal",venue_cfg["normal"])
FileContent_CreateNormalAndProp("prop",venue_cfg["prop"])

FileContent_CreateLottery(lottery_cfg)
FileContent_CreateSpeaker(speaker_cfg)
FileContent_CreateAllKill(all_kill_cfg)
FileContent_CreateAllBeauty(beauty_cfg)





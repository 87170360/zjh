#include <mysql/errmsg.h>
#include <stdio.h>
#include "XtSqlClient.h"


XtSqlClient::XtSqlClient()
{
	m_host="";
	m_port=0;
	m_username="";
	m_passwd="";
	m_dbname="";

	m_mysql=NULL;
	m_result=NULL;
}


XtSqlClient::~XtSqlClient()
{
	if(m_mysql)
	{
		mysql_close(m_mysql);
		m_mysql=NULL;
	}
}




int XtSqlClient::connect(const char* host,int port,const char* username,const char* passwd,const char* db)
{
	m_host=host;
	m_port=port;
	m_username=username;
	m_passwd=passwd;
	m_dbname=db;
	return connectSql();
}


int XtSqlClient::query(const char* sql)
{
	if(!m_mysql)
	{
		int re_ret=connectSql();
		if(re_ret!=0)
		{
			return -1;
		}
	}
	int ret=mysql_query(m_mysql,sql);

	if(ret!=0)
	{
		int re_ret=connectSql();
		if(re_ret==0)
		{
			ret=mysql_query(m_mysql,sql);
		}
	}

	if(ret==0)
	{
		return 0;
	}

	return -1;
}

int XtSqlClient::connectSql()
{

	if(m_mysql)
	{
		mysql_close(m_mysql);
		m_mysql=NULL;
	}


	MYSQL* sql=mysql_init(NULL);
	if(sql==NULL)
	{
		return -1;
	}

	m_mysql=mysql_real_connect(sql,m_host.c_str(),m_username.c_str(),m_passwd.c_str(),m_dbname.c_str(),m_port,NULL,0);
	if(m_mysql==NULL)
	{
		mysql_close(sql);
		return -1;
	}

	return 0;
}






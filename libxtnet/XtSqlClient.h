#ifndef _XT_SQL_CLIENT_H_
#define _XT_SQL_CLIENT_H_

#include <mysql/mysql.h>
#include <string>

class XtSqlClient 
{
	public:
		XtSqlClient();
		~XtSqlClient();

	public:
		int connect(const char* ip,int port,const char* username,const char* passwd,const char* dbname);
		int query(const char* sql);

	public:
		int connectSql();



	private:
		std::string m_host;
		int  m_port;
		std::string m_username;
		std::string m_passwd;
		std::string m_dbname;

		MYSQL* m_mysql;
		MYSQL_RES* m_result;
		MYSQL_ROW m_row;

};



#endif /*_XT_SQL_CLIENT_H_*/




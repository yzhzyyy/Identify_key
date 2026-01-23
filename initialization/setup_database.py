import mysql.connector
import argparse

def create_database_from_sql(host, user, password, database_name, sql_file):
    """Create a MySQL database from a .sql file."""
    try:
        # 连接 MySQL 服务器
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = conn.cursor()
        print(f"✅ Connected to MySQL server at {host}")

        # 创建数据库（如果不存在）
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"📦 Database '{database_name}' created or already exists.")

        # 切换到新数据库
        conn.database = database_name

        # 读取并执行 SQL 文件
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_commands = f.read()

        for statement in sql_commands.split(';'):
            if statement.strip():
                cursor.execute(statement)

        conn.commit()
        print(f"🎉 Database '{database_name}' successfully initialized from '{sql_file}'")

    except mysql.connector.Error as err:
        print(f"❌ MySQL Error: {err}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create MySQL database from SQL file")
    parser.add_argument("--host", default="localhost", help="MySQL server host")
    parser.add_argument("--user", default="root", help="MySQL username")
    parser.add_argument("--password", required=True, help="MySQL password")
    parser.add_argument("--database", default="Hockey", help="Database name to create")
    parser.add_argument("--sql", default="Hockey.sql", help="Path to the SQL file")

    args = parser.parse_args()

    create_database_from_sql(args.host, args.user, args.password, args.database, args.sql)

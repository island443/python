import pymysql
from django.conf import settings

settings.configure()
pymysql.install_as_MySQLdb()  # 用pymysql替换django默认的mysqldb

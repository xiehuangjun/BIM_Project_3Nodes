import pymysql, json, configparser, os, datetime

path = os.path.abspath('.')
cfgpath = path.split('BIM_P_API_3N')[0] + 'BIM_P_API_3N/config.ini'

config = configparser.ConfigParser()
config.read(cfgpath)


mysql = pymysql.connect(user = config['MYSQL']["user"], password = config['MYSQL']["password"], port = int(config["MYSQL"]["port"]), host = config['MYSQL']["host"])
cur = mysql.cursor()
#cur.execute('''CREATE DATABASE BIMP;''')

#cur.execute('''CREATE TABLE IF NOT EXISTS BIMP.Project_Name (
#                Project_id CHAR(100) NOT NULL PRIMARY KEY, 
#                Project_update_times CHAR(50) NOT NULL,
#                Project_getall_times CHAR(100))ENGINE = InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_unicode_ci;''')
#mysql.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS BIMP3N.Project_hash_verify(
    Project_id VARCHAR(100),
    Element_id VARCHAR(100),
    Check_in_status VARCHAR(50),
    Project_element_hashcode VARCHAR(150),
    DB_get_data_time VARCHAR(500),
    DB_data_encrypt_time VARCHAR(500),
    BC_get_data_time VARCHAR(500),
    BC_data_encrypt_time VARCHAR(500),
    Compared_time VARCHAR(500),
    Verify_time VARCHAR(500)
    )ENGINE = InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_unicode_ci;''')

mysql.commit()



cur.close()





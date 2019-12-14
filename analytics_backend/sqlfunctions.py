import mysql.connector as msqlc
from mysql.connector import Error


def sql_generator(params_list,table_name):
    column_names=",".join(params_list)
    sql = "SELECT "+column_names+"FROM "+table_name

    
def execute_select_query(params_list,table_name):
    try:
        connection = msqlc.connect(host='localhost', database='banking_bisleshok', user='nativeuser', password='paltupati07277')

        print('success')

    except Error as e:
        print("error")

    cursor=connection.cursor()

    cursor.execute(sql_generator(parmas_list, table_name))

    return cursor.fetchall()




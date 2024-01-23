# -*- coding: utf-8 -*-
import os
import pymysqlpool
from pymysql.cursors import DictCursor
from dotenv import load_dotenv
# from utils import crypto

load_dotenv()

def create_pool():

    try:
        config = {
            'host': os.environ.get('HOST'),
            'user': os.environ.get('USERNAME'),
            'password': os.environ.get('PASSWORD'),
            'database': os.environ.get('DB'),
            'port': int(os.environ.get('PORT')),
            'autocommit': True,
            'cursorclass': DictCursor
        }

        pool = pymysqlpool.ConnectionPool(size=2, maxsize=5, pre_create_num=2, name='pool', **config)
    
    except Exception as e:
        raise e
    
    return pool

def execute_query(pool, sql, data):
    con = pool.get_connection()
    cur = con.cursor()
    
    try:
        cur.execute(sql, data)
        con.commit()
    except Exception as e:
        con.rollback()
        raise e
    finally:
        con.close()

def select(pool, sql, args):

    con=pool.get_connection()
    cur = con.cursor()

    try:
        cur.execute(sql, args)
        result = cur.fetchall()
    except Exception as e:
        raise e
    finally:
        con.close()
        return result

def insert_dataframe(pool, table_name, dataframe):

    con = pool.get_connection()
    cur = con.cursor()

    try:
        con.begin()  # 트랜잭션 시작
        for index, row in dataframe.iterrows():

            columns = ', '.join(row.index)
            placeholders = ', '.join(['%s'] * len(row))
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            args = tuple(row)

            cur.execute(sql, args)

        con.commit()  # 모든 삽입 작업이 성공하면 커밋

    except Exception as e:
        con.rollback()  # 삽입 중 예외가 발생하면 롤백
        raise e

    finally:
        con.close()
        
def upsert_dataframe(pool, table_name, dataframe):

    con = pool.get_connection()
    cur = con.cursor()

    try:
        con.begin()  # 트랜잭션 시작
        for index, row in dataframe.iterrows():
            columns = ', '.join(row.index)
            placeholders = ', '.join(['%s'] * len(row))
            update_stmt = ', '.join([f"{col}=VALUES({col})" for col in row.index])

            sql = f"""INSERT INTO {table_name} ({columns}) VALUES ({placeholders})
                      ON DUPLICATE KEY UPDATE {update_stmt}"""

            args = tuple(row)

            cur.execute(sql, args)

        con.commit()  # 모든 삽입/업데이트 작업이 성공하면 커밋

    except Exception as e:
        con.rollback()  # 작업 중 예외가 발생하면 롤백
        raise e

    finally:
        con.close()
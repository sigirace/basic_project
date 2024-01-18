# -*- coding: utf-8 -*-
import os
import pymysqlpool
from pymysql.cursors import DictCursor
from dotenv import load_dotenv
# from utils import crypto

load_dotenv()

def create_pool(key):

    try:

        # pymysqlpool.logger.setLevel('DEBUG')
        # key = devkey
        # aes = crypto.AESCipher(key=key)
        config = {
            'host': os.environ.get('HOST'),
            'user': os.environ.get('USERNAME'),
            # 'password': aes.decrypt(os.environ.get('PASSWORD')),
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

def select(pool, sql, data):

    con=pool.get_connection()
    cur = con.cursor()

    try:
        cur.execute(sql, data)
        result = cur.fetchall()
    except Exception as e:
        raise e
    finally:
        con.close()
    return result

# -*- coding: utf-8 -*-
import os
import pymysqlpool
from pymysql.cursors import DictCursor
from dotenv import load_dotenv
from src.utils import crypto

load_dotenv()


def create_pool(key):

    try:

        # pymysqlpool.logger.setLevel('DEBUG')
        # key = devkey
        aes = crypto.AESCipher(key=key)
        config = {
            'host': os.environ.get('HOST'),
            'user': os.environ.get('USERNAME'),
            'password': aes.decrypt(os.environ.get('PASSWORD')),
            'database': os.environ.get('DB'),
            'port': int(os.environ.get('PORT')),
            'autocommit': True,
            'cursorclass': DictCursor
        }

        pool = pymysqlpool.ConnectionPool(size=2, maxsize=5, pre_create_num=2, name='pool', **config)
    
    except Exception as e:
        raise e
    
    return pool

def execute_query(pool, sql, args):
    con = pool.get_connection()
    cur = con.cursor()
    
    try:
        cur.execute(sql, args)
        con.commit()
    except Exception as e:
        con.rollback()
        raise e
    finally:
        con.close()

def select_one(pool, sql, args):

    con=pool.get_connection()
    cur = con.cursor()

    try:
        cur.execute(sql, args)
        result = cur.fetchone()
    except Exception as e:
        raise e
    finally:
        con.close()
    return result

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

def update(pool, sql, args):
    execute_query(pool, sql, args)

def insert(pool, sql, args):
    execute_query(pool, sql, args)

def delete(pool, sql, args):
    execute_query(pool, sql, args)
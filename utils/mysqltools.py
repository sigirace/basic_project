# -*- coding: utf-8 -*-
import pymysql
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def mysql_create_session():
  
  conn = pymysql.connect(host=os.environ.get('HOST'), 
                         user=os.environ.get('USERNAME'),
                         password=os.environ.get('PASSWORD'), 
                         db=os.environ.get('DB'), 
                         charset="utf8mb4", 
                         cursorclass=pymysql.cursors.DictCursor)
  cursor = conn.cursor()
  return conn, cursor

def select(sql, data=None):
    """
    :param sql: string
    :return: cursor
    """
    conn, cursor = mysql_create_session()

    try:
        if data:
          cursor.execute(sql, data)
        else:
           cursor.execute(sql)
    finally:
       conn.close()
    return cursor

def update(sql, data=None):
    """
    :param sql: string
    :return: True on success, False on failure
    """
    conn, cursor = mysql_create_session()

    try:
        if data:
            cursor.execute(sql, data)
        else:
            cursor.execute(sql)
        conn.commit()  # 변경 내용 커밋
    except Exception as e:
        print(e)
        return False
    finally:
       conn.close()
    return True

def delete(sql, data=None):
    """
    :param sql: string
    :return: True on success, False on failure
    """
    conn, cursor = mysql_create_session()

    try:
        if data:
            cursor.execute(sql, data)
        else:
            cursor.execute(sql)
        conn.commit()  # 변경 내용 커밋
    except Exception as e:
        print(e)
        return False
    finally:
       conn.close()
    return True

def insert(sql, data=None):
    """
    :param sql: string
    :return: True on success, False on failure
    """
    conn, cursor = mysql_create_session()

    try:
        if data:
            cursor.execute(sql, data)
        else:
            cursor.execute(sql)
        conn.commit()  # 변경 내용 커밋
    except Exception as e:
        print(e)
        return False
    finally:
       conn.close()
    return True
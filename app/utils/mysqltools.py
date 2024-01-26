# -*- coding: utf-8 -*-
import os
import aiomysql
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

async def create_pool(db_type=''):

    config = {
        'host': os.getenv('{}_HOST'.format(db_type)),
        'port': int(os.getenv('{}_PORT'.format(db_type))),
        'user': os.getenv('{}_USERNAME'.format(db_type)),
        'password': os.getenv('{}_PASSWORD'.format(db_type)),
        'db': os.getenv('{}_DB'.format(db_type)),
        'cursorclass': aiomysql.DictCursor,
        'autocommit': True
    }

    pool = await aiomysql.create_pool(**config)

    return pool

async def execute_query(pool, sql, args=None, one=False):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql, args)
            result = None
            if sql.strip().upper().startswith("SELECT"):
                if one:
                    result = await cur.fetchone()
                    result = list(result.values())[0]
                else:
                    result = await cur.fetchall()
            return result

async def select(pool, sql, args=None, one=False):
    return await execute_query(pool, sql, args, one)
        
async def insert_dataframe(pool, table_name: str, dataframe: pd.DataFrame):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await conn.begin()
            try:
                for index, row in dataframe.iterrows():
                    columns = ', '.join(row.index)
                    placeholders = ', '.join(['%s'] * len(row))
                    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                    args = tuple(row)
                    await cur.execute(sql, args)
                await conn.commit()
            except Exception as e:
                await conn.rollback()
                raise
        
async def upsert_dataframe(pool, table_name: str, dataframe: pd.DataFrame):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await conn.begin()
            try:
                for index, row in dataframe.iterrows():
                    columns = ', '.join(row.index)
                    placeholders = ', '.join(['%s'] * len(row))
                    update_stmt = ', '.join([f"{col}=VALUES({col})" for col in row.index])
                    sql = f"""INSERT INTO {table_name} ({columns}) VALUES ({placeholders})
                              ON DUPLICATE KEY UPDATE {update_stmt}"""
                    args = tuple(row)
                    await cur.execute(sql, args)
                await conn.commit()
            except Exception as e:
                await conn.rollback()
                raise

async def close_pool(pool):
    pool.close()
    await pool.wait_closed()
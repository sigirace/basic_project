import os
import yaml
import traceback
import argparse
import os
from utils import mysqltools as db
from utils import logger
import psutil

from typing import Union
from fastapi import FastAPI
from http import HTTPStatus
import asyncio

# application import

app_name = 'test_process'
log = logger.get_logger()

QUERY_PATH = os.path.join(os.getcwd(), "config/queries.yaml")

with open(QUERY_PATH, 'r') as file:
    loaded_queries = yaml.safe_load(file)

read_pool = db.create_pool()
write_pool = db.create_pool()
app = FastAPI()

@app.get("/select_sync/{name}")
def select_sync(name: str):
    
    try:
        # Start process
        log.info('START SELECT PROCESS: {} application.'.format(app_name))
        
        log.info("START select DB")
        # db select
        select_result = db.select(pool=read_pool, sql=loaded_queries['select_by_name'], args=(name,))
        log.info("END select DB")

        result = {"statusCode": HTTPStatus.OK,
                  "status": "{} selected.".format(len(select_result))}
        # End process
        log.info('DONE PROCESS.')
        
    except Exception as e:
        log.error(e)
        log.error(str(e))
        log.error(traceback.format_exc())
        result = {"statusCode":HTTPStatus.INTERNAL_SERVER_ERROR,
                  "status": str(e)}

    return {"result": result}

@app.get("/select_async/{name}")
async def select_async(name:str):
    
    try:
        # Start process
        log.info('START SELECT PROCESS: {} application.'.format(app_name))
        
        log.info("START select DB")
        # db select
        select_result = db.select(pool=read_pool, sql=loaded_queries['select_by_name'], args=(name,))
        log.info("END select DB")

        result = {"statusCode": HTTPStatus.OK,
                  "status": "{} selected.".format(len(select_result))}
        # End process
        log.info('DONE PROCESS.')
        
    except Exception as e:
        log.error(e)
        log.error(str(e))
        log.error(traceback.format_exc())
        result = {"statusCode":HTTPStatus.INTERNAL_SERVER_ERROR,
                  "status": str(e)}

    return {"result": result}

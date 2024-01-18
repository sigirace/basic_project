import os
import yaml
import traceback
import argparse
import os
from utils import mysqltools as db
from utils import logger

from typing import Union
from fastapi import FastAPI

# application import

app_name = 'test_process'
log = logger.get_logger()

QUERY_PATH = os.path.join(os.getcwd(), "config/queries.yaml")

with open(QUERY_PATH, 'r') as file:
    loaded_queries = yaml.safe_load(file)

db_pool = db.create_pool(key="devkey")
app = FastAPI()

@app.get("/select_sync/{name}")
def select_sync(name: str):
    
    # Start process
    log.info('START SELECT PROCESS: {} application.'.format(app_name))
    
    log.info("START select DB")
    # db select
    result = db.select(pool=db_pool, sql=loaded_queries['select_by_name'], data=(name,))
    log.info("END select DB")
    
    # End process
    log.info('DONE PROCESS.')

    return {"result": result}

@app.get("/select_async/{name}")
async def select_async(name:str):
    
    # Start process
    log.info('START SELECT PROCESS: {} application.'.format(app_name))
    
    log.info("START select DB")
    # db select
    result = db.select(pool=db_pool, sql=loaded_queries['select_by_name'], data=(name,))
    log.info("END select DB")
    
    # End process
    log.info('DONE PROCESS.')

    return {"result": result}
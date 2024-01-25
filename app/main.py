import os
import yaml
import traceback
import os
from utils import mysqltools as db
from utils import logger

from fastapi import FastAPI
from http import HTTPStatus

# application import

app = FastAPI()
app_name = 'test_process'

QUERY_PATH = os.path.join(os.getcwd(), "config/queries.yaml")

@app.on_event("startup")
async def startup_event():
    app.state.pool = await db.create_pool()
    app.state.log = logger.get_logger()
    with open(QUERY_PATH, 'r') as file:
        app.state.queries = yaml.safe_load(file)
    app.state.log.info('START UP')

@app.get("/select/{resource_id}")
async def select_endpoint(resource_id: int):
    
    try:
        # Start process
        app.state.log.info('START SELECT PROCESS: {} application.'.format(app_name))
        app.state.log.info("START select DB")

        # db select
        select_result = await db.select(pool=app.state.pool, sql=app.state.queries['select_by_name'], args=(resource_id,))
        app.state.log.info("END select DB")

        result = {"statusCode": HTTPStatus.OK,
                  "status" : "ok",
                  "result": "{} selected.".format(len(select_result))}
        
        # End process
        app.state.log.info('DONE PROCESS.')
        
    except Exception as e:
        app.state.log.error(e)
        app.state.log.error(str(e))
        app.state.log.error(traceback.format_exc())

        result = {"statusCode":HTTPStatus.INTERNAL_SERVER_ERROR,
                  "status": "internal server error",
                  "result": str(e)}

    return {"result": result}

@app.on_event("shutdown")
async def shutdown_event():
    await db.close_pool(app.state.pool)
    app.state.log.info('SHUT DOWN')
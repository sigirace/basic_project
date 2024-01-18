import os
import yaml
import traceback
import argparse
import os
from utils import mysqltools as db
from utils import logger

# application import

app_name = 'test_process'
log = logger.get_logger()

QUERY_PATH = os.path.join(os.getcwd(), "config/queries.yaml")

with open(QUERY_PATH, 'r') as file:
    loaded_queries = yaml.safe_load(file)

db_pool = db.create_pool(key="devkey")

def main(args):
    
    try:

        # Start log
        log.info('START PROCESS: {} application.'.format(app_name))

        # function log
        log.info("START insert DB")
        db.execute_query(pool=db_pool, sql=loaded_queries['insert_name'], data=("test_name",))
        log.info("END insert DB")

        # function log
        log.info("START insert DB")
        db.execute_query(pool=db_pool, sql=loaded_queries['insert_name'], data=("test_name2",))
        log.info("END insert DB")

        # function log
        log.info("START select DB")
        result = db.select(pool=db_pool, sql=loaded_queries['select_by_name'], data=("test_name",))
        print(result)
        log.info("END select DB")

        # function log
        log.info("START select DB")
        result = db.select(pool=db_pool, sql=loaded_queries['select_by_name_in'], data=(args.list,))
        print(result)
        log.info("END select DB")

        # function log
        log.info("START update DB")
        db.execute_query(pool=db_pool, sql=loaded_queries['update_by_name'], data=("test_name2", "test_name3"))
        log.info("END update DB")

        # function log
        log.info("START select DB")
        result = db.select(pool=db_pool, sql=loaded_queries['select_by_name'], data=("test_name3",))
        print(result)
        log.info("END select DB")

        # function log
        log.info("START delete DB")
        db.execute_query(pool=db_pool, sql=loaded_queries['delete_by_name'], data=("test_name",))
        log.info("END delete DB")

        # function log
        log.info("START delete DB")
        db.execute_query(pool=db_pool, sql=loaded_queries['delete_by_name'], data=("test_name3",))
        log.info("END delete DB")

        # End log
        log.info('DONE PROCESS.')

    except:
        # Error log
        msg_err = traceback.format_exc()
        log.error("ERROR PROCESS\n{}".format(msg_err))
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--add_arg", type=str, default="arg1", help="argument")
    parser.add_argument("--list", nargs="+", type=str, help="List of items")
    args = parser.parse_args()
    main(args)
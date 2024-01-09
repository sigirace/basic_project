from utils import mysqltools as db
from utils import logger
import yaml
import traceback

app_name = 'test_process'
log = logger.get_logger()

with open('./config/queries.yaml', 'r') as file:
    loaded_queries = yaml.safe_load(file)

def main(log=log):
    
    try:

        log.info('START PROCESS: {} application.'.format(app_name))

        log.info("START insert DB")
        print(db.insert(loaded_queries['insert_name'], data=("test_name",)))
        log.info("END insert DB")

        log.info("START select DB")
        result = db.select(loaded_queries['select_by_name'], data=("test_name",))
        print(vars(result))
        log.info("END select DB")

        log.info("START update DB")
        print(db.update(loaded_queries['delete_by_name'], data=("test_name",)))
        log.info("END update DB")

        log.info("START select DB")
        result = db.select(loaded_queries['select_by_name'], data=("test_name",))
        print(vars(result))
        log.info("END select DB")

        log.info('DONE PROCESS.')

    except:
        msg_err = traceback.format_exc()
        log.error("ERROR PROCESS\n{}".format(msg_err))
        

if __name__ == "__main__":
    main()
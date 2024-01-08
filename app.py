from utils import mysqltools as db
from utils import logger
import yaml
import traceback

log = logger.get_logger()

def main(log=log):

    with open('./config/queries.yaml', 'r') as file:
        loaded_queries = yaml.safe_load(file)
    
    try:
        log.info("START insert DB")
        print(db.insert(loaded_queries['insert_name'], data=("kangsigi",)))
        log.info("END insert DB")

        log.info("START select DB")
        result = db.select(loaded_queries['select_by_name'], data=("kangsigi",))
        print(vars(result))
        log.info("END select DB")

        log.info("START update DB")
        print(db.update(loaded_queries['delete_by_name'], data=("kangsigi",)))
        log.info("END update DB")

        log.info("START select DB")
        result = db.select(loaded_queries['select_by_name'], data=("kangsigi",))
        print(vars(result))
        log.info("END select DB")

    except:
        msg_err = traceback.format_exc()
        log.error("ERROR PROCESS\n{}".format(msg_err))
        

if __name__ == "__main__":
    main()
import time
from mylogger import logger


def algorithm_start(id):
    logger.info('start --> %s ' ,id[0])
    time.sleep(2)
    logger.info('finish --> %s ' ,id[0])
    return 'excute the algorithm.py'
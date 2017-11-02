import logging
from logging.handlers import RotatingFileHandler
from liebiao.settings import LOG_FILE

formatter = logging.Formatter('[%(filename)-12s]: [%(levelname)-6s] [%(asctime)s]: %(message)s')

rotating_handler = RotatingFileHandler(LOG_FILE, mode='a', maxBytes=5 * 1024 * 1024,
                                       backupCount=2, encoding=None, delay=0)
rotating_handler.setFormatter(formatter)
rotating_handler.setLevel(logging.INFO)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger.addHandler(rotating_handler)


if __name__ == "__main__":
    while 1:
        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')
import logging
import logging.handlers

def log_config():
    # logger
    logger = logging.getLogger()
    # handler
    file_handler = logging.handlers.TimedRotatingFileHandler('server.log', when='M', interval=1, backupCount=3,encoding='utf-8')
    # formatter
    log_my_formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)-9s - %(filename)-8s : %(lineno)s line - %(message)s")
    # set handler
    file_handler.setFormatter(log_my_formatter)
    # set logger
    logger.addHandler(file_handler)

def log_requests(url, data):
    logging.info(url)
    logging.info(data)

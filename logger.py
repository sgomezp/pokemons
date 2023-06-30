import logging
import sys
#from logging.handlers import
import datetime


def setup_logger(log_file):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s  %(filename)s %(funcName)s %(lineno)s - %(message)s', datefmt='%d-%m-%Y %H:%M:%S')


    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Para salida por consola

    logStreamFormatter = logging.Formatter(
        fmt=f"%(levelname)-8s %(asctime)s \t %(filename)s @function %(funcName)s line %(lineno)s - %(message)s",
        datefmt="%H:%M:%S"
    )
    consoleHandler = logging.StreamHandler(stream=sys.stdout)
    consoleHandler.setFormatter(logStreamFormatter)
    consoleHandler.setLevel(level=logging.DEBUG)

    logger.addHandler(consoleHandler)

    return logger

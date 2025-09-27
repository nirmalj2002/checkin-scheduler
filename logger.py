"""
Configures and manages logging for the utility.
"""
import logging

def setup_logger():
    logger = logging.getLogger('CheckinScheduler')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('scheduler.log')
    fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    if not logger.hasHandlers():
        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger

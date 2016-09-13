# exception_decorator.py

import functools
import logging
from blog.configurations.config import (LOGNAME, LOGFILENAME,
                                        LOGLEVEL, LOGFORMAT)


def create_logger():
    """
    Creates a logging object and returns it
    """

    logger = logging.getLogger(LOGNAME)
    logger.setLevel(LOGLEVEL)

    # create the logging file handler
    fh = logging.FileHandler(LOGFILENAME)
    fmt = LOGFORMAT.replace('?','%')
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)
    return logger


def write_bug_to_file(function):
    """
    A decorator that wraps the passed in function and logs
    exceptions
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            # log the exception
            logger = create_logger()
            err = "There was an exception in  " + function.__name__
            logger.exception(err)
    return wrapper
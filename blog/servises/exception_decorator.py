# exception_decorator.py

import functools
import logging


def create_logger():
    """
    Creates a logging object and returns it

    """

    logger = logging.getLogger("blog_logger")
    logger.setLevel(logging.DEBUG)

    # create the logging file handler
    fh = logging.FileHandler("blog_logs.log")

    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
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
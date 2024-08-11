import inspect

import logging


class LogGenerator:

    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler(".\\Logs\\BankApplogs.log")
        logformat = logging.Formatter(
            "%(asctime)s : %(levelname)s :  %(name)s : %(funcName)s : %(lineno)d : %(message)s"
        )
        logfile.setFormatter(logformat)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger

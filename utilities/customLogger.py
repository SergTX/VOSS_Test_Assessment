import logging

class LogGen:
    @staticmethod
    def loggen(self):
        logging.basicConfig(filename=".//Logs//logs.log")
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        return logger

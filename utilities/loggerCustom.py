import logging

class Logging:
    @staticmethod
    def logging():
        logging.basicConfig(filename='..//Logs//logs.log',
                                format='%(asctime)s: %(levelname)s: %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger

ll = Logging.logging()
ll.info('*** Just info ****')
ll.critical('*** Critical info ****')
ll.error('*** Error info ****')
ll.debug('*** Debug info ****')
ll.warning('*** Warning info ****')




# # class Logging:
# #     @staticmethod
# def loggen():
#     logging.basicConfig(filename='..//Logs//logs.log',
#                         format='%(asctime)s: %(levelname)s: %(message)s',
#                         datefmt='%m/%d/%Y %I : %M:%S %p')
#     logger = logging.getLogger()
#     logger.setLevel(logging.DEBUG)
#     return logger
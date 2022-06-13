
import configparser
 # read data from config.ini
config = configparser.RawConfigParser()
config.read("..//Configuration//config.ini")

class ReadConfig:
    @staticmethod
    def getURL():
        url = config.get('common info', 'urlmain_auto')
        return url
    @staticmethod
    def userEmail():
         userEmail = config.get('common info', 'userEmail')
         return  userEmail
    @staticmethod
    def userPW():
        password = config.get('common info', 'userPassword')
        return password

    @staticmethod
    def sign_URL():
        url_signin = config.get('common info', 'url_signin')
        return url_signin

    @staticmethod
    def baseUrl():
        baseURL = config.get('fill info', 'baseUrl')
        return baseURL

    @staticmethod
    def L_name():
        L_name = config.get('fill info', 'L_name' )
        return L_name

    @staticmethod
    def L_message():
        L_messg = config.get('fill info', 'L_message' )
        return L_messg

    @staticmethod
    def R_name():
        R_name = config.get('fill info', 'R_name' )
        return R_name

    @staticmethod
    def R_message():
        R_messg = config.get('fill info', 'R_message' )
        return R_messg

    @staticmethod
    def purchase_url():
        purchase_url = config.get('purchase url', 'baseURl')
        return purchase_url

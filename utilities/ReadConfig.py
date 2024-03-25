# import configparser
#
# config=configparser.RawConfigParser() ;
#
# filepath="D:\\PYTHON CT15\\FINAL_REVISION\\configuration\\config.ini" ;
#
# config.read(filepath) ;
#
# class ReadConfig():
#
#     @staticmethod
#     def getUserName():
#         username=config.get('common data', 'username') ;
#         return username ;
#
#     @staticmethod
#     def getPassWord() :
#         password=config.get('common data', 'password') ;
#         return password ;
# import configparser
#
# config=configparser.RawConfigParser() ;
#
# filepath = "D:\\PYTHON CT15\\FINAL_REVISION\\configuration\\config.ini"
#
# config.read(filepath) ;
#
# class ReadConfig():
#
#     @staticmethod
#     def getUserName():
#         username=config.get('common data', 'username') ;
#         return username ;
#     @staticmethod
#     def getPassWord():
#         password=config.get('common data', 'password') ;
#         return password ;
# import configparser
#
# config=configparser.RawConfigParser() ;
#
# filepath = "D:\\PYTHON CT15\\FINAL_REVISION\\configuration\\config.ini" ;
#
# config.read(filepath) ;
#
# class ReadConfig():
#
#     @staticmethod
#     def getUserName():
#         username=config.get('common data', 'username') ;
#         return username ;
#
#     @staticmethod
#     def getPassWord():
#
#         password=config.get('common data', 'password') ;
#         return password ;
import configparser

config=configparser.RawConfigParser() ;

filepath = "D:\\PYTHON CT15\\FINAL_REVISION\\configuration\\config.ini"

config.read(filepath) ;

class ReadConfig():

    @staticmethod
    def getUserName():
        username=config.get('common data', 'username') ;
        return username ;

    @staticmethod
    def getPassWord():
        password=config.get('common data', 'password') ;
        return password ;
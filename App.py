## Project:     SkyAuctions
## Author:      Emily Goodwin
## Description : Contains code to implement a singleton that holds configuration file fed objects 
## Using Kevin Browne's sample project, the App class as a start
## Uses singleton pattern

import configparser
from logging import Logger
from Logger import SingletonFileLogger

# singleton that contains all read-only state data that is needed across the application:
# config data, logging data, database connection
class App():
    _instance = None
    GENERIC_TYPE = SingletonFileLogger.GENERIC_TYPE
    def setup(self):
        config = configparser.ConfigParser()
        config.read("config.cfg")

        self.__logger = None
        self.__logTypes = []
        if (config["Logging"]["LOG"] == "TRUE"):
            self.__logger = SingletonFileLogger(config["Logging"]["FILE_NAME"])
        if (config["Logging"]["DEBUG"] == "TRUE"):
            self.__logTypes.append(SingletonFileLogger.GENERIC_TYPE.DEBUG)
        if (config["Logging"]["NORMAL"] == "TRUE"):
            self.__logTypes.append(SingletonFileLogger.GENERIC_TYPE.NORMAL)
        if (config["Logging"]["ERROR"] == "TRUE"):
            self.__logTypes.append(SingletonFileLogger.GENERIC_TYPE.ERROR)
        if (config["Logging"]["OTHER"] == "TRUE"):
            self.__logTypes.append(SingletonFileLogger.GENERIC_TYPE.OTHER)
        
        self.dbdriver = config["Database"]["DRIVER"]
        self.dbserver = config["Database"]["SERVER"]
        self.dbdatabase = config["Database"]["DATABASE"]
        self.dbuser = config["Database"]["USER"]
        self.dbpassword = config["Database"]["PASSWORD"]

    # log the information
    def Log(self, type, message, genericType = SingletonFileLogger.GENERIC_TYPE.DEBUG):
        if self.__logger == None:
            return
        else:
            if (genericType in self.__logTypes):
                self.__logger.Log(type, message, genericType)

    # create or return singleton instance
    def __new__(cls):
        if (cls._instance is None):
            cls._instance = super(App, cls).__new__(cls)
            cls._instance.setup()

        return cls._instance
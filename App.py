## Project:     SkyAuctions
## Author:      Emily Goodwin
## Description : Contains code to implement a singleton that holds configuration file fed objects 
## Using Kevin Browne's sample project, the App class as a start
## Uses singleton pattern

import configparser
from logging import Logger
from Logger import SingletonFileLogger
from os.path import exists
import os
# singleton that contains all read-only state data that is needed across the application:
# config data, logging data, database connection
class App():
    _instance = None
    GENERIC_TYPE = SingletonFileLogger.GENERIC_TYPE
    def setup(self):
        if exists("config_local.cfg"):
            config = configparser.ConfigParser()
            config.read("config_local.cfg")

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
        else:
            self.__logger = None
            self.__logTypes = []
            if (os.environ["CONFIG_LOG"] == "TRUE"):
                self.__logger = SingletonFileLogger(os.environ["CONFIG_LOG_FILENAME"])
            if (os.environ["CONFIG_LOG_DEBUG"] == "TRUE"):
                self.__logTypes.append(SingletonFileLogger.GENERIC_TYPE.DEBUG)
            if (os.environ["CONFIG_LOG_NORMAL"] == "TRUE"):
                self.__logTypes.append(SingletonFileLogger.GENERIC_TYPE.NORMAL)
            if (os.environ["CONFIG_LOG_ERROR"] == "TRUE"):
                self.__logTypes.append(SingletonFileLogger.GENERIC_TYPE.ERROR)
            if (os.environ["CONFIG_LOG_OTHER"] == "TRUE"):
                self.__logTypes.append(SingletonFileLogger.GENERIC_TYPE.OTHER)

            self.dbdriver = os.environ["CONFIG_DRIVER"]
            self.dbserver = os.environ["CONFIG_SERVER"]
            self.dbdatabase = os.environ["CONFIG_DATABASE"]
            self.dbuser = os.environ["CONFIG_USER"]
            self.dbpassword = os.environ["CONFIG_PASSWORD"]
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
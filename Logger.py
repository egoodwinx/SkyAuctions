## Project:     SkyAuctions
## Author:      Emily Goodwin
## Description :Contains code for the singleton logger which writes logs to a file. 
##              Uses https://refactoring.guru/design-patterns/singleton/python/example#example-1
from datetime import datetime
from threading import Lock
from enum import Enum

class SingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwds):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwds)
                cls._instances[cls] = instance
        return cls._instances[cls]

class SingletonFileLogger(metaclass=SingletonMeta):
    filename = None
    GENERIC_TYPE = Enum("GENERIC_TYPE", "DEBUG, NORMAL, ERROR, OTHER")

    def __init__(self, fileName="SkyAuctions.log"):
        self.filename = fileName

    def Log(self, type, message, generictype = GENERIC_TYPE.DEBUG):
        logFile = open(self.filename, "a+")
        logFile.write(str(datetime.now()) +"[" + str(generictype.name) + "] : " + type  + " : " + str(message)  + "\n")
        logFile.close()


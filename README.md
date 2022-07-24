# SkyAuctions
A project for 4SA3. Uses REST API from Hypixel and SQL Server Database.

Config should be in config.cfg file in working directory.
```
[Database]
DRIVER = 
SERVER =
DATABASE = 
USER = 
PASSWORD = 
[Logging]
FILE_NAME = SkyAuctions.log
LOG = TRUE
DEBUG = FALSE
NORMAL = TRUE
ERROR = TRUE
OTHER = TRUE
```

User Environment Variables for Azure Cloud/Local
```
[
  {
    "name": "ALLOWED_HOSTS",
    "value": "[]",
    "slotSetting": false
  },
  {
    "name": "ALLOWED_ORIGINS",
    "value": "[]",
    "slotSetting": false
  },
  {
    "name": "CONFIG_DATABASE",
    "value": "SkyAuctionsDB",
    "slotSetting": false
  },
  {
    "name": "CONFIG_DRIVER",
    "value": "SQL Server",
    "slotSetting": false
  },
  {
    "name": "CONFIG_LOG",
    "value": "TRUE",
    "slotSetting": false
  },
  {
    "name": "CONFIG_LOG_DEBUG",
    "value": "FALSE",
    "slotSetting": false
  },
  {
    "name": "CONFIG_LOG_ERROR",
    "value": "TRUE",
    "slotSetting": false
  },
  {
    "name": "CONFIG_LOG_FILENAME",
    "value": "Skyauctions.log",
    "slotSetting": false
  },
  {
    "name": "CONFIG_LOG_NORMAL",
    "value": "TRUE",
    "slotSetting": false
  },
  {
    "name": "CONFIG_LOG_OTHER",
    "value": "TRUE",
    "slotSetting": false
  },
  {
    "name": "CONFIG_PASSWORD",
    "value": "<dbpassword>",
    "slotSetting": false
  },
  {
    "name": "CONFIG_SERVER",
    "value": "<dbserver>",
    "slotSetting": false
  },
  {
    "name": "CONFIG_USER",
    "value": "<dbuser>",
    "slotSetting": false
  },
  {
    "name": "DATABASES",
    "value": "{   'default': {         'NAME':'<dbname>',         'ENGINE':'mssql',         'HOST':'<host>',         'USER':'<user>',         'PASSWORD':'<password>'     } }",
    "slotSetting": false
  },
  {
    "name": "DEBUG",
    "value": "1",
    "slotSetting": false
  },
  {
    "name": "SCM_DO_BUILD_DURING_DEPLOYMENT",
    "value": "true",
    "slotSetting": false
  },
  {
    "name": "SECRET_KEY",
    "value": "",
    "slotSetting": false
  },
]
```

Use ```python hypixel.py``` to start database updater

Use ```python manage.py runserver``` to start django instance

Then host static website via IIS or via cloud services.

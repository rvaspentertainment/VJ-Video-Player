import re
from os import environ

# Bot Session Name
SESSION = environ.get('SESSION', 'TechVJBot')

# Your Telegram Account Api Id And Api Hash
API_ID = int(environ.get('API_ID', '13828860'))
API_HASH = environ.get('API_HASH', 'bbcd5f94dcd9f8a5eedc5de7397b4127')

# Bot Token, This Is Main Bot
BOT_TOKEN = environ.get('BOT_TOKEN', "7419820448:AAH3AGFN4Sqd4xoR3MT_UTkXTVW7Zre-TQ8")

# Admin Telegram Account Id For Withdraw Notification Or Anything Else
ADMIN = int(environ.get('ADMIN', '591732965'))

# Back Up Bot Token For Fetching Message When Floodwait Comes
BACKUP_BOT_TOKEN = environ.get('BACKUP_BOT_TOKEN', "8020773384:AAEC12HX_Zeh3srp0X4OT4lVOtkHNs4Y3_8")

# Log Channel, In This Channel Your All File Stored.
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001611423558'))

# Mongodb Database For User Link Click Count Etc Data Store.
MONGODB_URI = environ.get("MONGODB_URI", "mongodb+srv://rebelstarcreations123:Z5aWnjBR96lmn4FW@cluster0.gg7js7w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Stream Url Means Your Deploy Server App Url, Here You Media Will Be Stream And Ads Will Be Shown.
STREAM_URL = environ.get("STREAM_URL", "")

# This Link Used As Permanent Link That If Your Deploy App Deleted Then You Change Stream Url, So This Link Will Redirect To Stream Url.
LINK_URL = environ.get("LINK_URL", "https://testrvasp.blogspot.com/p/rvasp-test.html")

# Others, Not Usefull
PORT = environ.get("PORT", "8080")
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False

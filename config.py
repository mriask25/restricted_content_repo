# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21309033"))
API_HASH = getenv("API_HASH", "c98a9e45defd5228c1ba962e4ccec401")
BOT_TOKEN = getenv("BOT_TOKEN", "8194685042:AAEVd4V9Y20CYtrVyvGNgDB88v8phPLHxQY")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6624253591").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://savebot:RxxBfvkv1xnGsbPL@cluster0.9zpw7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "1002223267642"))

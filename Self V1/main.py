#---- By @Rex_Developer ----#
#---- Self Bot V1 ----#
#---------------------------# Import Modules #---------------------------#
from re import match, IGNORECASE
from pyrogram import Client, filters, idle
from pyrogram.raw import functions
from pyrogram.types import *
from pyrogram import enums
from Helper import helper
from functions import func


#---------------------------# Bot Information #---------------------------#
plugins = dict(root="plugins")
print("#------Self v1------#")
print("#------by @Rex_Developer------#")
Rex = Client(
    "Self",
    api_id = 10858272,
    api_hash = "bdbf5fd78fc08ba1aef82685a6bd398d",
    plugins=plugins
)
sudo = 468354860

Rex.start()
helper.start()
idle()
Rex.stop()
helper.stop()
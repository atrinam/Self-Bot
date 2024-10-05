#---- By @MR_Rex ----#
#---- Self Bot V1 ----#
#---------------------------# Import Modules #---------------------------#
from pyrogram import Client, idle
from pyrogram.types import *
from Helper import helper


#---------------------------# Bot Information #---------------------------#
plugins = dict(root="plugins")
print("#------Self v1------#")
print("#------by @MR_Rex------#")
Rex = Client(
    "Self",
    api_id = 999999999999999999,
    api_hash = "api_hash",
    plugins=plugins
)
sudo = 99999999999

Rex.start()
helper.start()
idle()
Rex.stop()
helper.stop()
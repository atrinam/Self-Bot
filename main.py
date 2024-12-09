#---- By @rainbow ----#
#---- Self Bot V1 ----#
#---------------------------# Import Modules #---------------------------#
from pyrogram import Client, idle
from pyrogram.types import *
from Helper import helper


#---------------------------# Bot Information #---------------------------#
plugins = dict(root="plugins")
print("#------Self v1------#")
print("#------by @rainbow------#")
Rex = Client(
    "Self",
    api_id = 27227089,
    api_hash = "03ac3b8dd6a14cf5a231203db4660f59",
    plugins=plugins
)
sudo = 7803950092

Rex.start()
helper.start()
idle()
Rex.stop()
helper.stop()

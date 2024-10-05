from pyrogram import Client as Rex
from pyrogram import filters, enums, errors
from pyrogram.types import InputMediaPhoto, InputMediaVideo, ChatPermissions
from pyrogram.raw import functions, types
from asyncio import sleep
import requests
import json
import random
import os
from functions.func import ChangeMod

sudo = 468354860

if os.path.exists(f"self.json"):
    with open("self.json", "r") as x:
        self = json.load(x)
else:
    self = {
    "status" : "on",
    "enemys" : {},
    "friends" : {},
    "tempenemy_name" : 0,
    "tempenemy_id" : 0,
    "tempgp" : 0,
    "muteallhelper" : "",
    "monshitext": "سلام من یعنی فرزین الان آفلاینه\nاگر کارش داری پیغام بذار\nآنلاین بشه جوابتو میده :)",
    "monshiuser": 0,
    "monshimedia": {
        "monshiphoto": 0,
        "monshigif": 0,
        "monshisticker": 0,
        "monshivoice": 0,
        "monshicaption" : 0
    },
    "firstcm_channels" : [],
    "firstcm_text" : "کامنت اول :)",
    "settings" : {
        "typing" : "off",
        "poker" : "off",
        "firstcomment" : "off",
        "monshi" : "on",
        "mute": [],
        "offtime" : 10,
        "font" : "off",
        "bold" : "off",
        "underline" : "off",
        "inlinetext" : "off",
        "mention" : "off",
        "lockch" : 0,
    },
    "enemygroup" : {},
    "enemypv" : {},
    "enemyspecial" : {},
    "userprofile" : {
        "name" : "",
        "id" : "",
        "username" : ""
    }
}
    with open(f"self.json", "w") as f:
        json.dump(self, f, indent=4)

StartPm = ("♛","♚","⌯","♤","⇌","↯","↬","●","₪","⇝","✧","✩","✪","✯","➠","➥","➪","➲","❥")
emoji = ["😀", "😄","シ","ッ","ツ","ヅ"]


async def selfstatus(Rex, message):
    global StartPm
    global emoji
    R_START = random.choice(StartPm)
    R_END = random.choice(emoji)
    text = str(message.text)
    chat_id = message.chat.id
    new_status = text.replace("self ","")
    with open("self.json", "r") as x:
        self = json.load(x)
    if new_status == "on":
        if self["status"] == "on":
            await Rex.delete_messages(chat_id, message.id)
            await Rex.send_message(chat_id, f"{R_START} Self is AllReady Online {R_END}")
        else:
            self["status"] = "on"
            with open(f"self.json", "w") as f:
                json.dump(self, f, indent=4)
            await Rex.delete_messages(chat_id, message.id)
            await Rex.send_message(chat_id, f"{R_START} Self is Online Now {R_END}")
    elif new_status == "off":
        if self["status"] == "off":
            await Rex.delete_messages(chat_id, message.id)
            await Rex.send_message(chat_id, f"{R_START} Self is AllReady Offline {R_END}")
        else:
            self["status"] = "off"
            with open(f"self.json", "w") as f:
                json.dump(self, f, indent=4)
            await Rex.delete_messages(chat_id, message.id)
            await Rex.send_message(chat_id, f"{R_START} Self is Offline Now {R_END}")

#---------------------------# Inline Panels #---------------------------#
async def Panel(Rex, message):
    chat_id = message.chat.id
    result = await Rex.get_inline_bot_results("RexSelf_bot", "")
    await Rex.delete_messages(chat_id, message.id)
    with open("self.json", "r") as x:
        self = json.load(x)
    self["tempgp"] = message.chat.id
    with open(f"self.json", "w") as f:
        json.dump(self, f, indent=4)
    await Rex.send_inline_bot_result(chat_id, result.query_id, result.results[0].id, reply_to_message_id=message.id)

async def Panelgp(Rex, message):
    chat_id = message.chat.id
    result = await Rex.get_inline_bot_results("RexSelf_bot", "")
    await Rex.delete_messages(chat_id, message.id)
    with open("self.json", "r") as x:
        self = json.load(x)
    self["tempgp"] = message.chat.id
    with open(f"self.json", "w") as f:
        json.dump(self, f, indent=4)
    await Rex.send_inline_bot_result(chat_id, result.query_id, result.results[1].id, reply_to_message_id=message.id)

async def EnemyPanel(Rex, message):
    chat_id = message.chat.id
    result = await Rex.get_inline_bot_results("RexSelf_bot", "")
    with open("self.json", "r") as x:
        self = json.load(x)
    self["tempenemy_name"] = message.reply_to_message.from_user.first_name
    self["tempenemy_id"] = message.reply_to_message.from_user.id
    self["tempgp"] = message.chat.id
    with open(f"self.json", "w") as f:
        json.dump(self, f, indent=4)
    await Rex.send_inline_bot_result(chat_id, result.query_id, result.results[2].id, reply_to_message_id=message.reply_to_message.id)

async def UserPanel(Rex, message):
    chat_id = message.chat.id
    print(message)
    result = await Rex.get_inline_bot_results("RexSelf_bot", "")
    await Rex.delete_messages(chat_id, message.id)
    with open("self.json", "r") as x:
        self = json.load(x)
    self["tempgp"] = message.chat.id
    self["userprofile"]["name"] = message.reply_to_message.from_user.first_name
    self["userprofile"]["id"] = message.reply_to_message.from_user.id
    self["userprofile"]["username"] = message.reply_to_message.from_user.username
    with open(f"self.json", "w") as f:
        json.dump(self, f, indent=4)
    await Rex.send_inline_bot_result(chat_id, result.query_id, result.results[3].id, reply_to_message_id=message.reply_to_message.id)

#---------------------------# Ping #---------------------------#
async def Ping(Rex, message):
    text = message.text
    chat_id = message.chat.id
    await sleep(1)
    mychar = ""
    charlist = ["I","M"," O","N","L","I","N","E"," :))"]
    for char in charlist:
        mychar += char
        await Rex.edit_message_text(chat_id, message.id, f"**{mychar}**")
        await sleep(0.3)

#---------------------------# Card #---------------------------#
async def Card(Rex, message):
    global StartPm
    global emoji
    R_END = random.choice(emoji)
    text = message.text
    chat_id = message.chat.id
    await sleep(1)
    mychar = ""
    charlist = ["شماره ", "کارت ↯", "\n\n5022 ","2910 ","8326 ","5353 ","\n\n محمدرضا"," نظری ","\n\nپس از انتقال ","از رسید ",f"عکس بفرستید {R_END}"]
    for char in charlist:
        mychar += char
        await Rex.edit_message_text(chat_id, message.id, f"**{mychar}**")
        await sleep(0.3)

#---------------------------# Send Game #---------------------------#
async def SendGame(Rex, message):
    chat_id = message.chat.id
    games = ["Neon Blaster","Neon Blaster 2","Block Buster","Gravity Ninja","Hexonix","Geometry Run 3D","Disco Ball"]
    result = await Rex.get_inline_bot_results("gamee", random.choice(games))
    await Rex.send_inline_bot_result(chat_id, result.query_id, result.results[0].id)
#---------------------------# Send Pic #---------------------------#
async def SendPic(Rex, message):
    global StartPm
    global emoji
    R_START = random.choice(StartPm)
    text = str(message.text)
    chat_id = message.chat.id
    picname = text.split(" ")[1]
    picnum = text.split(" ")[2]
    try:
        if int(picnum) <= 999999999999:
            picnum = int(picnum)
    except:
        picnum = text.split(" ")[3]
        picname = text.split(" ")[1] + " " + text.split(" ")[2]
    result = await Rex.get_inline_bot_results("pic ", picname)
    print(len(result.results))
    sucss = 0
    if int(picnum) >= 13:
        picnum = int(picnum)
        picnum = 12
    for x in range(int(picnum)):
        try:
            await Rex.send_inline_bot_result("me", result.query_id, result.results[random.choice(range(0,len(result.results)))].id, reply_to_message_id=message.id)
            sucss+=1
        except errors.WebpageCurlFailed:
            continue
        except errors.MediaEmpty:
            continue
    history_list = []
    async for history in Rex.get_chat_history("me", limit=sucss):
        history_list.append(history.photo.file_id)
        await Rex.delete_messages("me", history.id)
    medias = [InputMediaPhoto(history_list[x], caption=f"{R_START} {picname}") for x in range(0, len(history_list))]
    await Rex.send_media_group(
        chat_id,
        medias
    )

#---------------------------# Send Gif #---------------------------#
async def SendGif(Rex, message):
    global StartPm
    global emoji
    R_START = random.choice(StartPm)
    text = message.text
    chat_id = message.chat.id
    gifname = text.replace("gif ","")
    gresult = await Rex.get_inline_bot_results("gif ", gifname)
    for x in range(3):
        await Rex.send_inline_bot_result(chat_id, gresult.query_id, gresult.results[random.choice(range(0,30))].id, reply_to_message_id=message.id)
    # sucss = 0
    # for x in range(3):
    #     try:
    #         await Rex.send_inline_bot_result("me", gresult.query_id, gresult.results[random.choice(range(0,30))].id, reply_to_message_id=message.id)
    #         sucss+=1
    #     except errors.WebpageCurlFailed:
    #         continue
    # history_list = []
    # async for history in Rex.get_chat_history("me", limit=sucss):
    #     print(history)
    #     history_list.append(history.animation.file_id)
    #     await Rex.delete_messages("me", history.id)
    # file_list = []
    # for x in range(0, len(history_list)):
    #     file = await Rex.download_media(history_list[x], f"gif{x}.mkv")
    #     file_list.append(file)
    # medias = [InputMediaVideo(file_list[x], caption=f"{R_START} {gifname}") for x in range(0, len(file_list))]
    # print(file_list)
    # #try:
    # await Rex.send_media_group(
    #     chat_id,
    #     medias
    # )
    # except errors.MediaEmpty as x:
    #     print(x)
    #     # for x in range(3):
    #     #     await Rex.send_inline_bot_result(chat_id, gresult.query_id, gresult.results[random.choice(range(0,30))].id, reply_to_message_id=message.id)

#---------------------------# Send Music #---------------------------#
async def SendMusic(Rex, message):
    text = message.text
    chat_id = message.chat.id
    gifname = text.replace("music ","")
    gresult = await Rex.get_inline_bot_results("melobot", gifname)
    await Rex.send_inline_bot_result(chat_id, gresult.query_id, gresult.results[0].id, reply_to_message_id=message.id)

#---------------------------# MME #---------------------------#
async def Mme(Rex, message):
    chat_id = message.chat.id
    api = "http://api.oboobs.ru/noise/1"
    json_data = requests.get(api).json()
    condition = json_data[0]["preview"]
    url = f"http://media.oboobs.ru/{condition}"
    r = requests.get(url, allow_redirects=True)
    open('boobs.webp', 'wb').write(r.content)
    await Rex.send_sticker(chat_id, "boobs.webp", reply_to_message_id=message.id)

#---------------------------# Bot Reaload #---------------------------#
async def Reload(Rex, message):
    global StartPm
    global emoji
    R_START = random.choice(StartPm)
    R_END = random.choice(emoji)
    chat_id = message.chat.id
    mychar = ""
    reloading = [
f"{R_START} Bot Reloading please wait...",
f"{R_START} Bot Reloading please wait",
f"{R_START} Bot Reloading please wait." ,
f"{R_START} Bot Reloading please wait..",
f"{R_START} Bot Reloading please wait...",
f"{R_START} Loading Files",
f"{R_START} Loading Files.",
f"{R_START} Loading Files..",
f"{R_START} Loading Files..." ,
f"{R_START} Loading Files...." ,
f"{R_START} Loading Files.....",
f"{R_START} Loading Files",
f"{R_START} Files Loaded !" ,
"█▒▒▒▒▒▒▒▒▒10%",
"██▒▒▒▒▒▒▒▒20%",
"███▒▒▒▒▒▒▒30%",
"████▒▒▒▒▒▒40%",
"█████▒▒▒▒▒50%",
"██████▒▒▒▒60%" ,
"███████▒▒▒70%" ,
"████████▒▒80%",
"█████████▒90%" ,
"██████████100%" ,
f"{R_START} Self Bot Reloaded {R_END}",
]
    for char in reloading:
        mychar += char
        await Rex.edit_message_text(chat_id, message.id, f"**{char}**")
        await sleep(0.3)

#---------------------------# Font Change #---------------------------#
async def Fontchange(Rex, message):
    text = message.text
    chat_id = message.chat.id
    enbigwords = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","9","8","7","6","5","4","3","2","1"]
    ensmallwords= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","9","8","7","6","5","4","3","2","1"]
    try:
        print(text)
        fonts_en1 = ["ⓐ","ⓑ","ⓒ","ⓓ","ⓔ","ⓕ","ⓖ","ⓗ","ⓘ","ⓙ","ⓚ","ⓛ","ⓜ","ⓝ","ⓞ","ⓟ","ⓠ","ⓡ","ⓢ","ⓣ","ⓤ","ⓥ","ⓦ","ⓧ","ⓨ","ⓩ","⓪","➈","➇","➆","➅","➄","➃","➂","➁","➀"]
        fonts_en2 = ["α","в","c","∂","є","ƒ","g","н","ι","נ","к","ℓ","м","η","σ","ρ","q","я","ѕ","т","υ","ν","ω","χ","у","z","0","9","8","7","6","5","4","3","2","1"]
        fonts_en3 = ["α","в","¢","đ","e","f","g","ħ","ı","נ","κ","ł","м","и","ø","ρ","q","я","š","т","υ","ν","ω","χ","ч","z","0","9","8","7","6","5","4","3","2","1"]
        fonts_en4 = ["Æ","þ","©","Ð","E","F","ζ","Ħ","Ї","¿","ズ","ᄂ","M","Ñ","Θ","Ƿ","Ø","Ґ","Š","τ","υ","¥","w","χ","y","շ","0","9","8","7","6","5","4","3","2","1"]
        en_fonts = [fonts_en1,fonts_en2,fonts_en3,fonts_en4]
        font_en = random.choice(en_fonts)
        print(font_en)
        newtext = text.replace("a", font_en[0]).replace("b", font_en[1]).replace("c", font_en[2]).replace("d",font_en[3]).replace("e",font_en[4]).replace("f",font_en[5]).replace("g",font_en[6]).replace("h",font_en[7]).replace("i",font_en[8]).replace("j",font_en[9]).replace("k",font_en[10]).replace("l",font_en[11]).replace("m",font_en[12]).replace("n",font_en[13]).replace("o",font_en[14]).replace("p",font_en[15]).replace("q",font_en[16]).replace("r",font_en[17]).replace("s",font_en[18]).replace("t",font_en[19]).replace("u",font_en[20]).replace("v",font_en[21]).replace("w",font_en[22]).replace("x",font_en[23]).replace("y",font_en[24]).replace("z",font_en[25]).replace("0",font_en[26]).replace("9",font_en[27]).replace("8",font_en[28]).replace("7",font_en[29]).replace("6",font_en[30]).replace("5",font_en[31]).replace("4",font_en[32]).replace("3",font_en[33]).replace("2",font_en[34]).replace("1",font_en[35])
        print(newtext)
        await Rex.edit_message_text(chat_id, message.id, newtext)
    except:
        fonts_fa1 = ['ضً','صً','ثہ','قہً','فُہ','غہ','عہُ','ه','خہ','حہ','جہ','شہ','سہ','يہ','ٻً','لہ','ٳ','تہ','نٍ','كُہ','مْ','ةً','ء','ظً','طہ','ذً','دِ','زً','ڒٍ','وٌ','ىّ']
        fonts_fa2 = ['ڞ','ڝ','ﭦ','ڦ','ڤ','ﻏ̐','؏','هـﮧ','خ','ڂ','چ','شَ','ﺳ̭͠','يِّ','ﭜ','لَ','ٱ','ﭠ','ڻ','ڳ','م','ةً','ء','ڟ','ط','ڎ','ﮃ','ژ','ر','و','يِّ']
        fonts_fa3 = ['ضِٰـﮧِۢ','صِٰـﮧِۢ','ثِٰـﮧِۢ','قِٰـﮧِۢ','فِٰ͒ـِﮧۢ','غِٰـﮧِۢ','عِٰـﮧِۢ','ۿۿہ','خِٰ̐ـﮧِۢ','حِٰـﮧِۢ','جِٰـﮧِۢ','شِٰـﮧِۢ','سِٰـﮧِ','يِٰـﮧِۢ','بِٰـِﮧۢ','لِٰـِﮧۢ','آ','تِٰـﮧِۢ','نِٰـﮧِۢ','مِٰـﮧِۢ','ڪِٰـﮧِۢ','ةً','ء','ظِٰـﮧِۢ','طِٰـﮧِۢ','ذٰ','د','ژ','رٰ','ﯛ̲୭','ىٍ']
        font_fa = random.choice([fonts_fa1, fonts_fa2, fonts_fa3])
        newtext = text.replace('ض',font_fa[0]).replace('ص',font_fa[1]).replace('ث',font_fa[2]).replace('ق',font_fa[3]).replace('ف',font_fa[4]).replace('غ',font_fa[5]).replace('ع',font_fa[6]).replace('ه',font_fa[7]).replace('خ',font_fa[8]).replace('ح',font_fa[9]).replace('ج',font_fa[10]).replace('ش',font_fa[11]).replace('س',font_fa[12]).replace('ي',font_fa[13]).replace('ب',font_fa[14]).replace('ل',font_fa[15]).replace('ا',font_fa[16]).replace('ت',font_fa[17]).replace('ن',font_fa[18]).replace('ك',font_fa[19]).replace('م',font_fa[20]).replace('ة',font_fa[21]).replace('ء',font_fa[22]).replace('ظ',font_fa[23]).replace('ط',font_fa[24]).replace('ذ',font_fa[25]).replace('د',font_fa[26]).replace('ز',font_fa[27]).replace('ر',font_fa[28]).replace('و',font_fa[29]).replace('ى',font_fa[30])
        print(newtext)
        await Rex.edit_message_text(chat_id, message.id, newtext)

#---------------------------# Poker Mod #---------------------------#
@ChangeMod
async def Poker(Rex, message, mod):
    return "ok"

#---------------------------# Monshi #---------------------------#
@ChangeMod
async def Monshi(Rex, message, mod):
    return "ok"

async def MonshiAnswers(Rex, message):
    global StartPm
    global emoji
    R_START = random.choice(StartPm)
    R_END = random.choice(emoji)
    chat_id = message.chat.id
    with open("self.json", "r") as x:
        self = json.load(x)
    if message.reply_to_message.caption:
        self["monshimedia"]["monshicaption"] = message.reply_to_message.caption
        self["monshitext"] = 0
    if message.reply_to_message.animation:
        self["monshimedia"]["monshigif"] = message.reply_to_message.animation.file_id
        self["monshitext"] = 0
        self["monshimedia"]["monshiphoto"] = 0
        self["monshimedia"]["monshisticker"] = 0
        self["monshimedia"]["monshivoice"] = 0
    elif message.reply_to_message.photo:
        self["monshimedia"]["monshiphoto"] = message.reply_to_message.photo.file_id
        self["monshitext"] = 0
        self["monshimedia"]["monshigif"] = 0
        self["monshimedia"]["monshisticker"] = 0
        self["monshimedia"]["monshivoice"] = 0
    elif message.reply_to_message.voice:
        self["monshimedia"]["monshivoice"] = message.reply_to_message.voice.file_id
        self["monshimedia"]["monshigif"] = 0
        self["monshimedia"]["monshisticker"] = 0
        self["monshimedia"]["monshiphoto"] = 0
        self["monshitext"] = 0
    elif message.reply_to_message.sticker:
        self["monshimedia"]["monshisticker"] = message.reply_to_message.sticker.file_id
        self["monshimedia"]["monshigif"] = 0
        self["monshimedia"]["monshivoice"] = 0
        self["monshimedia"]["monshiphoto"] = 0
        self["monshitext"] = 0
    elif message.reply_to_message.text:
        self["monshitext"] = message.reply_to_message.text
        self["monshimedia"]["monshiphoto"] = 0
        self["monshimedia"]["monshigif"] = 0
        self["monshimedia"]["monshisticker"] = 0
        self["monshimedia"]["monshivoice"] = 0
        self["monshimedia"]["monshicaption"] = 0
    with open(f"self.json", "w") as f:
        json.dump(self, f, indent=4)
    await Rex.edit_message_text(chat_id, message.id, f"{R_START} **Monshi Answer** Updated {R_END}")

#---------------------------# Monshi Time #---------------------------#
async def MonshiTime(Rex, message):
    global StartPm
    global emoji
    R_START = random.choice(StartPm)
    R_END = random.choice(emoji)
    text = message.text
    chat_id = message.chat.id
    with open("self.json", "r") as x:
        self = json.load(x)
    offtime = text.replace("offtime ","")
    try:
        if int(offtime) < 999999999999999999:
            self["settings"]["offtime"] = int(offtime)
            await Rex.delete_messages(chat_id, message.id)
            await Rex.send_message(chat_id, f"{R_START} **Monshi Enable Time** setted to {offtime} minutes {R_END}")
            with open(f"self.json", "w") as f:
                json.dump(self, f, indent=4)
    except:
        await Rex.delete_messages(chat_id, message.id)
        await Rex.send_message(chat_id, f"{R_START} Wrong minute :/")

#---------------------------# Mute Mod #---------------------------#
async def Muteuser(Rex, message):
    global StartPm
    global emoji
    R_START = random.choice(StartPm)
    R_END = random.choice(emoji)
    text = message.text
    userid = message.chat.id
    with open("self.json", "r") as x:
        self = json.load(x)
    newmod = text.replace(f"mute ","") 
    if newmod == "on":
        if userid not in self["settings"]["mute"]:
            self["settings"]["mute"].append(userid)
            await Rex.delete_messages(userid, message.id)
            await Rex.send_message(userid, f"{R_START} **Mute Mod** is On now {R_END}")
            with open(f"self.json", "w") as f:
                json.dump(self, f, indent=4)
        else:
            await Rex.delete_messages(userid, message.id)
            await Rex.send_message(userid, f"{R_START} **Mute Mod** is AlReady On {R_END}")
    elif newmod == "off":
        if userid in self["settings"]["mute"]:
            self["settings"]["mute"].remove(userid)
            await Rex.delete_messages(userid, message.id)
            await Rex.send_message(userid, f"{R_START} **Mute Mod** is Off now {R_END}")
            with open(f"self.json", "w") as f:
                json.dump(self, f, indent=4)
        else:
            await Rex.delete_messages(userid, message.id)
            await Rex.send_message(userid, f"{R_START} **Mute Mod** is AlReady Off {R_END}")

#---------------------------# Typing #---------------------------#
@ChangeMod
async def Typing(Rex, message, mod):
    return("ok")

#---------------------------# Font Text #---------------------------#
@ChangeMod
async def FontText(Rex, message, mod):
    return("ok")

#---------------------------# Bold Text #---------------------------#
@ChangeMod
async def Boldtext(Rex, message, mod):
    return("ok")

#---------------------------# Underline Text #---------------------------#
@ChangeMod
async def Underlinetext(Rex, message, mod):
    return("ok")

#---------------------------# Inline Text #---------------------------#
@ChangeMod
async def Inlinetext(Rex, message, mod):
    return("ok")

#---------------------------# Mention Text #---------------------------#
@ChangeMod
async def Mentiontext(Rex, message, mod):
    return("ok")

#---------------------------# On Messages #---------------------------#
@Rex.on_message(filters.me, group=0)
async def specials(Rex, message):
    with open("self.json", "r") as x:
        self = json.load(x)
    global StartPm
    global emoji
    R_START = random.choice(StartPm)
    R_END = random.choice(emoji)
    print(message)
    with open("self.json", "r") as x:
        self = json.load(x)
    text = str(message.text)
    chat_id = message.chat.id
    if text.startswith("self "):
        await selfstatus(Rex, message)
    if self["status"] == "on":
        if text.startswith("setchlock "):
            chid = text.replace("setchlock ","")
            if "-" in chid:
                chid = int(chid)
            self["settings"]["lockch"] = chid
            with open(f"self.json", "w") as f:
                json.dump(self, f, indent=4)
            await Rex.delete_messages(chat_id, message.id)
            await Rex.send_message(chat_id, f"{R_START} New Private Channel Setted For Download {R_END}")
        if text.startswith("dwnch "):
            await Rex.delete_messages(chat_id, message.id)
            mid = text.replace("dwnch ","")
            chid = self["settings"]["lockch"]
            m = await Rex.get_messages(chid, int(mid))
            print(m)
            if m.text:
                await Rex.copy_message(chat_id, chid, int(mid))
            else:
                file = await Rex.download_media(m, in_memory=True)
                file_name = file.name
                print(f"File Name: {file_name}")
                if m.caption:
                    caption = m.caption
                else:
                    caption = ""
                if m.photo : 
                    await Rex.send_photo(chat_id, file, caption=caption)
                elif m.voice:
                    await Rex.send_voice(chat_id, file, caption=caption)
                elif m.video:
                    await Rex.send_video(chat_id, file, caption=caption)
        elif text.startswith("chfname "):
            newfname = text.replace("chfname ","")
            await Rex.update_profile(first_name=newfname)
            await Rex.delete_messages(chat_id, message.id)
            await Rex.send_message(chat_id, f"{R_START} First Name Changed to {newfname} {R_END}")
        elif text.startswith("chlname "):
            newlname = text.replace("chlname ","")
            await Rex.update_profile(last_name=newlname)
            await Rex.delete_messages(chat_id, message.id)
            await Rex.send_message(chat_id, f"{R_START} Last Name Changed to {newlname} {R_END}")
        elif text.startswith("changebio "):
            newbio = text.replace("changebio ","")
            await Rex.update_profile(bio=newbio)
            await Rex.delete_messages(chat_id, message.id)
            await Rex.send_message(chat_id, f"{R_START} Bio Changed to {newlname} {R_END}")
        elif text.startswith("chusername "):
            newusername = text.replace("chusername ","")
            await Rex.set_username(newusername)
            await Rex.delete_messages(chat_id, message.id)
            await Rex.send_message(chat_id, f"{R_START} Username Changed to @{newusername} {R_END}")
        elif text.startswith("addcm_ch "):
            newch = text.replace("addcm_ch ","")
            try:
                if int(newch) in self["firstcm_channels"]:
                    await Rex.delete_messages(chat_id, message.id)
                    await Rex.send_message(chat_id, f"{R_START} this Channel AllReady in First Comment Channels list {R_END}")
                else:
                    self["firstcm_channels"].append(int(newch))
                    with open(f"self.json", "w") as f:
                        json.dump(self, f, indent=4)
                    await Rex.delete_messages(chat_id, message.id)
                    await Rex.send_message(chat_id, f"{R_START} New Channel Successfully Added to First Comment Channels list {R_END}")
            except:
                if newch in self["firstcm_channels"]:
                    await Rex.delete_messages(chat_id, message.id)
                    await Rex.send_message(chat_id, f"{R_START} this Channel AllReady in First Comment Channels list {R_END}")
                else:
                    self["firstcm_channels"].append(newch)
                    with open(f"self.json", "w") as f:
                        json.dump(self, f, indent=4)
                    await Rex.delete_messages(chat_id, message.id)
                    await Rex.send_message(chat_id, f"{R_START} New Channel Successfully Added to First Comment Channels list {R_END}")
        elif text.startswith("removecm_ch "):
            remch = text.replace("removecm_ch ","")
            try:
                if int(newch) not in self["firstcm_channels"]:
                    await Rex.delete_messages(chat_id, message.id)
                    await Rex.send_message(chat_id, f"{R_START} this Channel not in First Comment Channels list {R_END}")
                else:
                    self["firstcm_channels"].remove(int(newch))
                    with open(f"self.json", "w") as f:
                        json.dump(self, f, indent=4)
                    await Rex.delete_messages(chat_id, message.id)
                    await Rex.send_message(chat_id, f"{R_START} Channel Successfully Removed from First Comment Channels list {R_END}")
            except:
                if remch not in self["firstcm_channels"]:
                    await Rex.delete_messages(chat_id, message.id)
                    await Rex.send_message(chat_id, f"{R_START} this Channel not in First Comment Channels list {R_END}")
                else:
                    self["firstcm_channels"].remove(remch)
                    with open(f"self.json", "w") as f:
                        json.dump(self, f, indent=4)
                    await Rex.delete_messages(chat_id, message.id)
                    await Rex.send_message(chat_id, f"{R_START} Channel Successfully Removed from First Comment Channels list {R_END}")
        elif text.startswith("cmtext "):
            cmtext = text.replace("cmtext ","")
            self["firstcm_text"] = cmtext
            with open(f"self.json", "w") as f:
                json.dump(self, f, indent=4)
            await Rex.delete_messages(chat_id, message.id)
            await Rex.send_message(chat_id, f"{R_START} Text Successfully Setted for First Comment in Channels {R_END}")

        elif text == "enemy" and message.reply_to_message:
            #print(message)
            await Rex.delete_messages(chat_id, message.id)
            await EnemyPanel(Rex, message)
        elif text.startswith("typing "):
            await Typing(Rex, message, "typing")
        elif text.startswith("font "):
            await FontText(Rex, message, "font")
        elif text.startswith("poker "):
            await Poker(Rex, message, "poker")
        elif text.startswith("monshi "):
            await Monshi(Rex, message, "monshi")
        elif text == "setmonshi" and message.reply_to_message:
            print(message)
            await MonshiAnswers(Rex, message)
        elif text.startswith("offtime "):
            await MonshiTime(Rex, message)
        elif text.startswith("mute ") and message.chat.type == enums.chat_type.ChatType.PRIVATE:
            await Muteuser(Rex, message)
        elif text.startswith("bold "):
            await Boldtext(Rex, message, "bold")
        elif text.startswith("underline "):
            await Underlinetext(Rex, message, "underline")
        elif text.startswith("inlinetext "):
            await Inlinetext(Rex, message, "inlinetext")
        elif text.startswith("mention "):
            await Mentiontext(Rex, message, "mention")
        elif text == "ping":
            await Ping(Rex, message)
        elif text == "card":
            await Card(Rex, message)
        elif text == "reload":
            await Reload(Rex, message)
        elif text == "game":
            await Rex.delete_messages(chat_id, message.id)
            await SendGame(Rex, message)
        elif text == "ممه":
            await Rex.delete_messages(chat_id, message.id)
            await Mme(Rex, message)
        elif text.startswith("pic "):
            await Rex.delete_messages(chat_id, message.id)
            await SendPic(Rex, message)
        elif text.startswith("gif "):
            await Rex.delete_messages(chat_id, message.id)
            await SendGif(Rex, message)
        elif text.startswith("music "):
            await Rex.delete_messages(chat_id, message.id)
            await SendMusic(Rex, message)
        elif text == "mydel":
            await Rex.delete_user_history(chat_id, "me")
        elif text == "share":
            await Rex.delete_messages(chat_id, message.id)
            await Rex.send_contact(chat_id, "+7 977 476 2300", "Mr Rex :)", reply_to_message_id=message.id)
        elif text == "getonline":
            #print(message)
            #await Rex.delete_messages(chat_id, message.id)
            online = await Rex.get_chat_online_count(chat_id)
            await Rex.edit_message_text(chat_id, message.id, f"تعداد افراد آنلاین گروه : {online}")
        elif text == "getuser" and message.reply_to_message:
            #await Rex.delete_messages(chat_id, message.id)
            userinfo = await Rex.get_users(message.reply_to_message.from_user.id)
            await Rex.edit_message_text(chat_id, message.id, userinfo)
        elif text == "updatemsg":
            await Rex.edit_message_text(chat_id, message.id, message)
        elif text == "panel" and "-100" in str(chat_id) and not message.reply_to_message:
            await Panelgp(Rex, message)
        elif text == "panel" and not message.reply_to_message:
            await Panel(Rex, message)
        elif text == "panel" and message.reply_to_message:
            await UserPanel(Rex, message)
        elif text == "bots":
            bots = []
            async for m in Rex.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BOTS):
                bots.append(m.user.id)
            print(bots)
        elif text == "members":
            async for member in Rex.get_chat_members(chat_id):
                #print(member)
                if member.user.status == enums.UserStatus.LONG_AGO:
                    print("User status is LONG_AGO")
        elif text == "like" and message.reply_to_message:
            await Rex.delete_messages(chat_id, message.id)
            await Rex.send_reaction(chat_id, message.reply_to_message.id, "🔥")
        elif text.startswith("gpname "):
            newgpname = text.replace("gpname ", "")
            await Rex.set_chat_title(chat_id, newgpname)
            await Rex.edit_message_text(chat_id, message.id, f"{R_START} Chat title successfully Changed to {newgpname} {R_END}")
        elif text == "gpdesc" and message.reply_to_message:
            await Rex.set_chat_description(chat_id, message.reply_to_message.text)
            await Rex.edit_message_text(chat_id, message.id, f"{R_START} Chat Description successfully Changed {R_END}")
        elif text == "muteall":
            try:
                await Rex.set_chat_permissions(chat_id, ChatPermissions())
                await Rex.edit_message_text(chat_id, message.id, f"{R_START} Group Muted now {R_END}")
            except errors.ChatAdminRequired:
                await Rex.edit_message_text(chat_id, message.id, f"{R_START} im not Admin in this Group {R_END}")
            except errors.ChatNotModified:
                await Rex.edit_message_text(chat_id, message.id, f"{R_START} Group Muted allready {R_END}")

        elif text == "unmuteall":
            try:
                await Rex.set_chat_permissions(
                    chat_id,
                    ChatPermissions(
                        can_send_messages=True,
                        can_send_media_messages=True,
                        can_send_other_messages=True,
                        can_send_polls=True,
                        can_add_web_page_previews=True,
                        can_invite_users=True
                    )
                )
                await Rex.edit_message_text(chat_id, message.id, f"{R_START} Group UnMuted now{R_END}")
            except errors.ChatAdminRequired:
                await Rex.edit_message_text(chat_id, message.id, f"{R_START} im not Admin in this Group {R_END}")
            except errors.ChatNotModified:
                await Rex.edit_message_text(chat_id, message.id, f"{R_START} Group UnMuted allready {R_END}")
        elif text and self["settings"]["font"] == "on":
            await Fontchange(Rex, message)
        elif text and self["settings"]["bold"] == "on":
            if message.animation:
                pass
            elif message.video or message.photo or message.voice:
                if message.caption:
                    try:
                        await Rex.edit_message_caption(chat_id, message.id, f"**{message.caption}**")
                    except:
                        pass
            else:
                try:
                    await Rex.edit_message_text(chat_id, message.id, f"**{message.text}**")
                except:
                    pass
                
        elif text and self["settings"]["underline"] == "on":
            if message.animation:
                pass
            elif message.video or message.photo or message.voice:
                if message.caption:
                    try:
                        await Rex.edit_message_caption(chat_id, message.id, f"**{message.caption}**")
                    except:
                        pass
            else:
                try:
                    await Rex.edit_message_text(chat_id, message.id, f"--{message.text}--")
                except:
                    pass
        elif text and self["settings"]["inlinetext"] == "on":
            if message.animation:
                pass
            elif message.video or message.photo or message.voice:
                if message.caption:
                    try:
                        await Rex.edit_message_caption(chat_id, message.id, f"**{message.caption}**")
                    except:
                        pass
            else:
                try:
                    await Rex.edit_message_text(chat_id, message.id, f"`{message.text}`")
                except:
                    pass
        elif text and self["settings"]["mention"] == "on":
            if message.animation:
                pass
            elif message.video or message.photo or message.voice:
                if message.caption:
                    try:
                        await Rex.edit_message_caption(chat_id, message.id, f"**{message.caption}**")
                    except:
                        pass
            else:
                try:
                    await Rex.edit_message_text(chat_id, message.id, f"[{message.text}](tg://user?id={sudo})")
                except:
                    pass

#---------------------------# On Raw Updates #---------------------------#
@Rex.on_raw_update(filters.channel)
async def raw(Rex, update, users, chats):
    #print(update)
    draft = await Rex.invoke(
            functions.messages.GetAllDrafts()
        )
    #print(draft)
    if draft.updates:
        if draft.updates[0].draft.message == "dwn":
            if draft.chats:
                if draft.chats[0]:
                    await Rex.invoke(
                    functions.messages.SaveDraft(
                        peer = types.InputPeerChannel(channel_id = draft.chats[0].id, access_hash = draft.chats[0].access_hash), #await Rex.resolve_peer(draft.chats[0].id),
                        message = "dwnch -postid (send post from Private Channels)"
                        )
                    )
            else:
                await Rex.invoke(
                    functions.messages.SaveDraft(
                        peer = await Rex.resolve_peer(draft.users[0].id),
                        message = "dwnch -postid (send post from Private Channels)"
                    )
                )
        elif draft.updates[0].draft.message == "inline":
            if draft.chats:
                if draft.chats[0]:
                    await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = types.InputPeerChannel(channel_id = draft.chats[0].id, access_hash = draft.chats[0].access_hash),
                            message = "inlinetext on"
                        )
                    )
            else:
                await Rex.invoke(
                    functions.messages.SaveDraft(
                        peer = await Rex.resolve_peer(draft.users[0].id),
                        message = "inlinetext on"
                    )
                )
        elif draft.updates[0].draft.message == "type":
            if draft.chats:
                if draft.chats[0]:
                    await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = types.InputPeerChannel(channel_id = draft.chats[0].id, access_hash = draft.chats[0].access_hash),
                            message = "typing on"
                        )
                    )
            else:
                await Rex.invoke(
                    functions.messages.SaveDraft(
                        peer = await Rex.resolve_peer(draft.users[0].id),
                        message = "typing on"
                    )
                )
        elif draft.updates[0].draft.message == "get":
            if draft.chats:
                if draft.chats[0]:
                    await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = types.InputPeerChannel(channel_id = draft.chats[0].id, access_hash = draft.chats[0].access_hash),
                            message = "getonline or getuser or updatemsg"
                        )
                    )
            else:
                await Rex.invoke(
                    functions.messages.SaveDraft(
                        peer = await Rex.resolve_peer(draft.users[0].id),
                        message = "getonline or getuser or updatemsg"
                    )
                )
import json
import random
from pyrogram import Client as helper
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyromod.helpers import ikb


sudo = 7803950092


StartPm = ("♛","♚","⌯","♤","⇌","↯","↬","●","₪","⇝","✧","✩","✪","✯","➠","➥","➪","➲","❥")
R_START = random.choice(StartPm)
emoji = ["😁", "🙃", "😎", "😃", "🤩", "😜", "😚", "😉", "😀", "😄","シ","ッ","ツ","ヅ"]
R_END = random.choice(emoji)

#---------------------------# Enemy #---------------------------#
class Enemy:
    "Add or Remove Enemys from List"

    async def SetEnemyall(name, userid):
        with open("self.json", "r") as x:
            self = json.load(x)
        self["enemys"][str(name)] = userid
        try:
            del self["friends"][name]
        except:
            pass
        self["tempenemy"] = 0
        with open(f"self.json", "w") as f:
            json.dump(self, f, indent=4)

    async def SetEnemyPrivate(name, userid):
        with open("self.json", "r") as x:
            self = json.load(x)
        self["enemypv"][str(name)] = userid
        try:
            del self["friends"][name]
        except:
            pass
        self["tempenemy"] = 0
        with open(f"self.json", "w") as f:
            json.dump(self, f, indent=4)

    async def SetEnemyGroup(name, userid):
        with open("self.json", "r") as x:
            self = json.load(x)
        self["enemygroup"][str(name)] = userid
        try:
            del self["friends"][name]
        except:
            pass
        self["tempenemy"] = 0
        with open(f"self.json", "w") as f:
            json.dump(self, f, indent=4)

    async def SetEnemySpecial(chatid, userid):
        with open("self.json", "r") as x:
            self = json.load(x)
        if str(userid) in self["enemyspecial"]:
            self["enemyspecial"][str(userid)].append(chatid)
        else:
            self["enemyspecial"] = {userid : [chatid]}
        self["tempenemy"] = 0
        self["tempgp"] = 0
        with open(f"self.json", "w") as f:
            json.dump(self, f, indent=4)

    async def RemEnemyByReply(chatid, name, userid):
        with open("self.json", "r") as x:
            self = json.load(x)
        try:
            del self["enemys"][name]
        except:
            pass
        try:
            del self["enemygroup"][name]
        except:
            pass
        try:
            del self["enemypv"][name]
        except:
            pass
        try:
            self["enemyspecial"][str(userid)].remove(chatid)
        except:
            pass
    
        with open(f"self.json", "w") as f:
            json.dump(self, f, indent=4)


#---------------------------# Friend #---------------------------#

class AddFriend:
    "Add Friends to Friends List :)"
    with open("self.json", "r") as x:
        self = json.load(x)
    def __init__(self, name, userid, chatid):
        self.name = name
        self.userid = userid
        self.chatid = chatid

        AddFriend.self["friends"][self.name] = self.userid
        try:
            del AddFriend.self["enemys"][self.name]
        except:
            pass
        try:
            del AddFriend.self["enemygroup"][self.name]
        except:
            pass
        try:
            del AddFriend.self["enemypv"][self.name]
        except:
            pass
        try:
            AddFriend.self["enemyspecial"][str(self.userid)].remove(self.chatid)
        except:
            pass
        with open(f"self.json", "w") as f:
            json.dump(AddFriend.self, f, indent=4)

class RemoveFriend:
    "Remove Friends from Friends List :)"
    with open("self.json", "r") as x:
        self = json.load(x)
    def __init__(self, name):
        self.name = name

        del RemoveFriend.self["friends"][self.name]
        with open(f"self.json", "w") as f:
            json.dump(RemoveFriend.self, f, indent=4)


#---------------------------# Change Mod Decorator #---------------------------#
def ChangeMod(func):
    async def wrapper(Rex, message, mod):
        print(f"wrapper running {mod}")
        global StartPm
        global emoji
        R_START = random.choice(StartPm)
        R_END = random.choice(emoji)
        text = message.text
        chat_id = message.chat.id
        with open("self.json", "r") as x:
            self = json.load(x)
        newmod = text.replace(f"{mod} ","") 
        if mod == "poker":
            modtext = "**Poker Mod**"
        elif mod == "monshi":
            modtext = "**Monshi**"
        elif mod == "typing":
            modtext = "**Type Mod**"
        elif mod == "font":
            modtext = "**FØÑτ Mod**"
        elif mod == "bold":
            modtext = "**Bold Mod**"
        elif mod == "underline":
            modtext = "--Underline Mod--"
        elif mod == "inlinetext":
            modtext = "`Inlinetext Mod`"
        elif mod == "mention":
            modtext = f"[MENTION MOD](tg://user?id={sudo})"
        if newmod == "on":
            if self["settings"][mod] == "off":
                self["settings"][mod] = "on"
                if mod == "font":
                    self["settings"]["inlinetext"] = "off"
                    self["settings"]["underline"] = "off"
                    self["settings"]["bold"] = "off"
                    self["settings"]["mention"] = "off"
                elif mod == "bold":
                    self["settings"]["inlinetext"] = "off"
                    self["settings"]["font"] = "off"
                    self["settings"]["underline"] = "off"
                    self["settings"]["mention"] = "off"
                elif mod == "underline":
                    self["settings"]["inlinetext"] = "off"
                    self["settings"]["font"] = "off"
                    self["settings"]["bold"] = "off"
                    self["settings"]["mention"] = "off"
                elif mod == "inlinetext":
                    self["settings"]["underline"] = "off"
                    self["settings"]["font"] = "off"
                    self["settings"]["bold"] = "off"
                    self["settings"]["mention"] = "off"
                elif mod == "mention":
                    self["settings"]["underline"] = "off"
                    self["settings"]["font"] = "off"
                    self["settings"]["bold"] = "off"
                    self["settings"]["inlinetext"] = "off"
                await Rex.delete_messages(chat_id, message.id)
                await Rex.send_message(chat_id, f"{R_START} {modtext} is On now {R_END}")
                with open(f"self.json", "w") as f:
                    json.dump(self, f, indent=4)
            else:
                await Rex.delete_messages(chat_id, message.id)
                await Rex.send_message(chat_id, f"{R_START} {modtext} is AlReady On {R_END}")
        elif newmod == "off":
            if self["settings"][mod] == "on":
                self["settings"][mod] = "off"
                await Rex.delete_messages(chat_id, message.id)
                await Rex.send_message(chat_id, f"{R_START} {modtext} is Off now {R_END}")
                with open(f"self.json", "w") as f:
                    json.dump(self, f, indent=4)
            else:
                await Rex.delete_messages(chat_id, message.id)
                await Rex.send_message(chat_id, f"{R_START} {modtext} is AlReady Off {R_END}")
    return wrapper

#---------------------------# Inline Change Mod Decorator #---------------------------#
def Inline_ChangeMod(func):
    async def wrapper(helper, call, mod):
        print(f"Inline wrapper running {mod}")
        global StartPm
        global emoji
        R_START = random.choice(StartPm)
        R_END = random.choice(emoji)
        with open("self.json", "r") as x:
            self = json.load(x)
        callmsg = call.data
        with open("self.json", "r") as x:
            self = json.load(x)
        if self["settings"][mod] == "on":
            print("Enabled")
            status = "Enabled"
        else:
            status = "Disabled"
        mod_menu = ikb([
        [(f"{R_START} {mod} Status : {status}", "/")],
        [(f"{R_START} Disable", f"/{mod}off"), (f"{R_START} Enable", f"/{mod}on")],
        [(f"{R_START} Back", "/backoptions")]
        ])
        backoptions_button = ikb([
        [(f"{R_START} Back","/backoptions")]
        ])
        if callmsg == f"/{mod}":
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} Please Select Wich Options you Want to Enable on {mod} Mod {R_END}", reply_markup=mod_menu)
        if mod == "poker":
            modtext = "**Poker Mod**"
        elif mod == "monshi":
            modtext = "**Monshi**"
        elif mod == "typing":
            modtext = "**Type Mod**"
        elif mod == "font":
            modtext = "**FØÑτ Mod**"
        elif mod == "bold":
            modtext = "**Bold Mod**"
        elif mod == "underline":
            modtext = "--Underline Mod--"
        elif mod == "inlinetext":
            modtext = "`Inlinetext Mod`"
        elif mod == "mention":
            modtext = f"[MENTION MOD](tg://user?id={sudo})"
        if callmsg == f"/{mod}on":
            if self["settings"][mod] == "off":
                self["settings"][mod] = "on"
                if mod == "font":
                    self["settings"]["inlinetext"] = "off"
                    self["settings"]["underline"] = "off"
                    self["settings"]["bold"] = "off"
                    self["settings"]["mention"] = "off"
                elif mod == "bold":
                    self["settings"]["inlinetext"] = "off"
                    self["settings"]["font"] = "off"
                    self["settings"]["underline"] = "off"
                    self["settings"]["mention"] = "off"
                elif mod == "underline":
                    self["settings"]["inlinetext"] = "off"
                    self["settings"]["font"] = "off"
                    self["settings"]["bold"] = "off"
                    self["settings"]["mention"] = "off"
                elif mod == "inlinetext":
                    self["settings"]["underline"] = "off"
                    self["settings"]["font"] = "off"
                    self["settings"]["bold"] = "off"
                    self["settings"]["mention"] = "off"
                elif mod == "mention":
                    self["settings"]["underline"] = "off"
                    self["settings"]["font"] = "off"
                    self["settings"]["bold"] = "off"
                    self["settings"]["inlinetext"] = "off"
                await helper.edit_inline_text(call.inline_message_id, f"{R_START} {modtext} is On now {R_END}", reply_markup=backoptions_button)
                with open(f"self.json", "w") as f:
                    json.dump(self, f, indent=4)
            else:
                await call.answer(f"{R_START} {modtext} is AlReady On {R_END}", show_alert=False)
        elif callmsg == f"/{mod}off":
            if self["settings"][mod] == "on":
                self["settings"][mod] = "off"
                await helper.edit_inline_text(call.inline_message_id, f"{R_START} {modtext} is Off now {R_END}", reply_markup=backoptions_button)
                with open(f"self.json", "w") as f:
                    json.dump(self, f, indent=4)
            else:
                await call.answer(f"{R_START} {modtext} is AlReady Off {R_END}", show_alert=False)
    return wrapper

backmain_button = ikb([
    [(f"{R_START} Back","/backmain")]
])

async def inline_selfstatus(helper, call):
    global StartPm
    global emoji
    R_START = random.choice(StartPm)
    R_END = random.choice(emoji)
    callmsg = call.data
    with open("self.json", "r") as x:
        self = json.load(x)
    if self["status"] == "on":
        status = "Enabled"
    else:
        status = "Disabled"
    self_menu = ikb([
        [(f"{R_START} Self Status : {status}", "/")],
        [(f"{R_START} Disable", f"/selfoff"), (f"{R_START} Enable", f"/selfon")],
        [(f"{R_START} Back", "/backmain")]
        ])
    if callmsg == "/self":
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} Please Select Wich Status you Want to Enable on Self Bot {R_END}", reply_markup=self_menu)
    if callmsg == "/selfon":
        if self["status"] == "on":
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} Self is AllReady Online {R_END}", reply_markup=backmain_button)
        else:
            self["status"] = "on"
            with open(f"self.json", "w") as f:
                json.dump(self, f, indent=4)
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} Self is Online Now {R_END}", reply_markup=backmain_button)
    elif callmsg == "/selfoff":
        if self["status"] == "off":
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} Self is AllReady Offline {R_END}", reply_markup=backmain_button)
        else:
            self["status"] = "off"
            with open(f"self.json", "w") as f:
                json.dump(self, f, indent=4)
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} Self is Offline Now {R_END}", reply_markup=backmain_button)

backoptions_button = ikb([
    [(f"{R_START} Back","/backoptions")]
])
backcomment_button = ikb([
    [(f"{R_START} Back","/firstcm")]
])

async def first_comment(helper, call):
    global StartPm
    global emoji
    R_START = random.choice(StartPm)
    R_END = random.choice(emoji)
    callmsg = call.data
    with open("self.json", "r") as x:
        self = json.load(x)
    if self["settings"]["firstcomment"] == "on":
        status = "Enabled"
    else:
        status = "Disabled"

    firstcm_menu = ikb([
        [(f"{R_START} First Comment Status : {status}", "/")],
        [(f"{R_START} Turn off", "/firstcmoff"), (f"{R_START} Turn on", "/firstcmon")],
        [(f"{R_START} Remove Channel", "/removecm"), (f"{R_START} Add Channel", "/addcm")],
        [(f"{R_START} First Comment Text", "/cmtext"), (f"{R_START} Channels List", "/firstcmlist")],
        [(f"{R_START} Back", "/backoptions")]
    ])
    if callmsg == "/firstcm":
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} Please Select Wich Options you Want to Do {R_END}", reply_markup=firstcm_menu) 
    elif callmsg == "/addcm":
        await helper.send_message(sudo, "addcm")
        await call.answer(f"{R_START} Please Send command in your Draft with Channel id or username for setting New First Comment Channel {R_END}", show_alert=True)
    elif callmsg == "/removecm":
        await helper.send_message(sudo, "removecm")
        await call.answer(f"{R_START} Please Send command in your Draft with Channel id or username for setting New First Comment Channel {R_END}", show_alert=True)
    elif callmsg == "/cmtext":
        await helper.send_message(sudo, "cmtext")
        await call.answer(f"{R_START} Please Send command in your Draft with Text you Want to Send for First Comment in Channels {R_END}", show_alert=True)
    elif callmsg == "/firstcmlist":
        with open("self.json", "r") as x:
            self = json.load(x)
        results = []
        if len(self["firstcm_channels"]) < 1:
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} List is Empty {R_END}", reply_markup = backcomment_button)
        else:
            for x in self["firstcm_channels"]:
                results.append(InlineKeyboardButton(x, url = f"t.me/{x}"))   
            results.append(InlineKeyboardButton(f"{R_START} Back", callback_data="/firstcm"))
            keyboard_elements = [[element] for element in results]
            firstcm_channels = InlineKeyboardMarkup(inline_keyboard=keyboard_elements)    
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} List of Channel setted for First Comment {R_END}", reply_markup = firstcm_channels)
    elif callmsg == "/firstcmon":
        with open("self.json", "r") as x:
            self = json.load(x)
        if self["settings"]["firstcomment"] == "on":
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} First Comment Mod is AllReady On {R_END}", reply_markup = backcomment_button)
        else:
            self["settings"]["firstcomment"] = "on"
            with open(f"self.json", "w") as f:
                json.dump(self, f, indent=4)
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} First Comment Mod is On Now {R_END}", reply_markup = backcomment_button)
    elif callmsg == "/firstcmoff":
        with open("self.json", "r") as x:
            self = json.load(x)
        if self["settings"]["firstcomment"] == "off":
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} First Comment Mod is AllReady Off {R_END}", reply_markup = backcomment_button)
        else:
            self["settings"]["firstcomment"] = "off"
            with open(f"self.json", "w") as f:
                json.dump(self, f, indent=4)
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} First Comment Mod is Off Now {R_END}", reply_markup = backcomment_button)

async def inline_mute(helper, call):
    global StartPm
    global emoji
    R_START = random.choice(StartPm)
    R_END = random.choice(emoji)
    callmsg = call.data
    with open("self.json", "r") as x:
        self = json.load(x)
    user = self["tempgp"]
    if user in self["settings"]["mute"]:
        status = "Enabled"
    else:
        status = "Disabled"
    mute_menu = ikb([
        [(f"{R_START} Status : {status}", "/")],
        [(f"{R_START} Disable", f"/muteoff"), (f"{R_START} Enable", f"/muteon")],
        [(f"{R_START} Back", "/backoptions")]
    ])
    if callmsg == f"/mute":
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} Please Select Wich Options you Want to Enable {R_END}", reply_markup=mute_menu)
    elif callmsg == "/muteon":
        if user not in self["settings"]["mute"]:
            self["settings"]["mute"].append(user)
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} **Mute Mod** is On now {R_END}", reply_markup=backoptions_button)
            with open(f"self.json", "w") as f:
                json.dump(self, f, indent=4)
        else:
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} **Mute Mod** is AlReady On {R_END}", reply_markup=backoptions_button)
    elif callmsg == "/muteoff":
        if user in self["settings"]["mute"]:
            self["settings"]["mute"].remove(user)
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} **Mute Mod** is Off now {R_END}", reply_markup=backoptions_button)
            with open(f"self.json", "w") as f:
                json.dump(self, f, indent=4)
        else:
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} **Mute Mod** is AlReady Off {R_END}", reply_markup=backoptions_button)

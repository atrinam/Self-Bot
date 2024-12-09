from pyrogram import Client as Rex
from pyrogram import filters, enums, errors
from pyrogram.raw import functions
from pyrogram.types import ChatPermissions
import random
import json
import os
from asyncio import sleep
import time

sudo = 7803950092
Helper = 8020661908

fohsh = ["گص کش","کس ننه","کص ننت","کس خواهر","کس خوار","کس خارت","کس ابجیت","کص لیس","ساک بزن","ساک مجلسی","ننه الکسیس","نن الکسیس",
"ناموستو گاییدم","ننه زنا","کس خل","کس مخ","کس مغز","کس مغذ","خوارکس","خوار کس","خواهرکس","خواهر کس","حروم زاده","حرومزاده",
"خار کس","تخم سگ","پدر سگ","پدرسگ","پدر صگ","پدرصگ","ننه سگ","نن سگ","نن صگ","ننه صگ","ننه خراب","تخخخخخخخخخ","نن خراب","مادر سگ",
"مادر خراب","مادرتو گاییدم","تخم جن","تخم سگ","مادرتو گاییدم","ننه حمومی","نن حمومی","نن گشاد","ننه گشاد","نن خایه خور","تخخخخخخخخخ",
"نن ممه","کس عمت","کس کش","کس بیبیت","کص عمت","کص خالت","کس بابا","کس خر","کس کون","کس مامیت","کس مادرن","مادر کسده","خوار کسده",
"تخخخخخخخخخ","ننه کس","بیناموس","بی ناموس","شل ناموس","سگ ناموس","ننه جندتو گاییدم باو ","چچچچ نگاییدم سیک کن پلیز D:","ننه حمومی","چچچچچچچ",
"لز ننع","ننه الکسیس","کص ننت","بالا باش","ننت رو میگام","کیرم از پهنا تو کص ننت","مادر کیر دزد","ننع حرومی","تونل تو کص ننت","کیر تک تک بکس رکس کمپانی تو کص ننت",
"کص خوار بدخواه","خوار کصده","ننع باطل","حروم لقمع","ننه سگ ناموس","منو ننت شما همه چچچچ","ننه کیر قاپ زن","ننع اوبی","ننه کیر دزد",
"ننه کیونی","ننه کصپاره","زنا زادع","کیر سگ تو کص نتت پخخخ","ولد زنا","ننه خیابونی","هیس بع کس حساسیت دارم","کص نگو ننه سگ که میکنمتتاااا","کص نن جندت",
"ننه سگ","ننه کونی","ننه زیرابی","بکن ننتم","ننع فاسد","ننه ساکر","کس ننع بدخواه","نگاییدم","مادر سگ","ننع شرطی","گی ننع",
"بابات شاشیدتت چچچچچچ","ننه ماهر","حرومزاده","ننه کص","کص ننت باو","پدر سگ","سیک کن کص ننت نبینمت","کونده","ننه ولو","ننه سگ",
"مادر جنده","کص کپک زدع","ننع لنگی","ننه خیراتی","سجده کن سگ ننع","ننه خیابونی","ننه کارتونی","تکرار میکنم کص ننت","تلگرام تو کس ننت",
"کص خوارت","خوار کیونی","پا بزن چچچچچ","مادرتو گاییدم","گوز ننع","کیرم تو دهن ننت","ننع همگانی","کیرم تو کص زیدت","کیر تو ممهای ابجیت",
"ابجی سگ","کس دست ریدی با تایپ کردنت چچچ","ابجی جنده","ننع سگ سیبیل","بده بکنیم چچچچ","کص ناموس","شل ناموس","ریدم پس کلت چچچچچ","ننه شل",
"ننع قسطی","ننه ول","دست و پا نزن کس ننع","ننه ولو","خوارتو گاییدم","محوی!؟","ننت خوبع!؟","کس زنت","شاش ننع","ننه حیاطی /:","نن غسلی",
"کیرم تو کس ننت بگو مرسی چچچچ","ابم تو کص ننت :/","فاک یور مادر خوار سگ پخخخ","کیر سگ تو کص ننت","کص زن","ننه فراری","بکن ننتم من باو جمع کن ننه جنده /:::",
"ننه جنده بیا واسم ساک بزن","حرف نزن که نکنمت هااا :|","کیر تو کص ننت😐","کص کص کص ننت😂","کصصصص ننت جووون","سگ ننع","کص خوارت",
"کیری فیس","کلع کیری","تیز باش سیک کن نبینمت","فلج تیز باش چچچ","بیا ننتو ببر","بکن ننتم باو ","کیرم تو بدخواه","چچچچچچچ","ننه جنده","ننه کص طلا",
"ننه کون طلا","کس ننت بزارم بخندیم!؟","کیرم دهنت","مادر خراب","ننه کونی","هر چی گفتی تو کص ننت خخخخخخخ","کص ناموست بای","کص ننت بای ://",
"کص ناموست باعی تخخخخخ","کون گلابی!","ریدی آب قطع","کص کن ننتم کع","نن کونی","نن خوشمزه","ننه لوس"," نن یه چشم ","ننه چاقال","ننه جینده",
"ننه حرصی ","نن لشی","ننه ساکر","نن تخمی","ننه بی هویت","نن کس","نن سکسی","نن فراری","لش ننه","سگ ننه","شل ننه","ننه تخمی","ننه تونلی","ننه کوون",
"نن خشگل","نن جنده","نن ول ","نن سکسی","نن لش","کس نن ","نن کون","نن رایگان","نن خاردار","ننه کیر سوار","نن پفیوز","نن محوی",
"ننه بگایی","ننه بمبی","ننه الکسیس","نن خیابونی","نن عنی","نن ساپورتی","نن لاشخور","ننه طلا","ننه عمومی","ننه هر جایی","نن دیوث",
"تخخخخخخخخخ","نن ریدنی","نن بی وجود","ننه سیکی","ننه کییر","نن گشاد","نن پولی","نن ول","نن هرزه","نن دهاتی","ننه ویندوزی","نن تایپی",
"نن برقی","نن شاشی","ننه درازی","شل ننع","یکن ننتم که","کس خوار بدخواه","آب چاقال","ننه جریده","ننه سگ سفید","آب کون","ننه 85",
"ننه سوپری","بخورش","کس نن","خوارتو گاییدم","خارکسده","گی پدر","آب چاقال","زنا زاده","زن جنده","سگ پدر","مادر جنده","ننع کیر خور",
"چچچچچ","تیز بالا","ننه سگو با کسشر در میره","کیر سگ تو کص ننت","kos kesh","kir","kiri","nane lashi","kos","kharet","blis kirmo","دهاتی",
"کیرم لا کص خارت","کیری","ننه لاشی","ممه","کص","کیر","بی خایه","ننه لش","بی پدرمادر","خارکصده","مادر جنده","کصکش"]

#---------------------------# Monshi #---------------------------#
async def Monshi(Rex, message):
    StartPm = ("↫","⇜","⌯","℘","↜","⇋","↯","➲","●","₪","▪️")
    R_START = random.choice(StartPm)
    emoji = ["😁", "🙃", "😎", "✋", "😃", "🤩", "😜", "😚", "😉", "😀", "😄"]
    R_END = random.choice(emoji)
    userid = message.chat.id
    if os.path.exists(f"self.json"):
        with open("self.json", "r") as x:
            self = json.load(x)
        if self["monshitext"] != 0:
            await Rex.send_message(userid, f"{R_START} {self['monshitext']}")
            self["monshiuser"] = userid
        elif self["monshimedia"]["monshiphoto"] != 0:
            if self["monshimedia"]["monshicaption"] != 0:
                caption = self["monshimedia"]["monshicaption"]
            else:
                caption = " "
            await Rex.send_photo(userid, self["monshimedia"]["monshiphoto"], caption)
            self["monshiuser"] = userid
        elif self["monshimedia"]["monshigif"] != 0:
            if self["monshimedia"]["monshicaption"] != 0:
                caption = self["monshimedia"]["monshicaption"]
            else:
                caption = " "
            await Rex.send_animation(userid, self["monshimedia"]["monshigif"], caption)
            self["monshiuser"] = userid
        elif self["monshimedia"]["monshisticker"] != 0:
            await Rex.send_sticker(userid, self["monshimedia"]["monshisticker"])
            self["monshiuser"] = userid
        elif self["monshimedia"]["monshivoice"] != 0:
            if self["monshimedia"]["monshicaption"] != 0:
                caption = self["monshimedia"]["monshicaption"]
            else:
                caption = " "
            await Rex.send_voice(userid, self["monshimedia"]["monshivoice"], caption)
            self["monshiuser"] = userid
        with open(f"self.json", "w") as f:
            json.dump(self, f, indent=4)

@Rex.on_message(group=1)
async def users(Rex, message):
    #print(message)
    text = str(message.text)
    chat_id = message.chat.id
    StartPm = ("♛","♚","⌯","♟","♤","⇌","↯","↬","●","₪","⇝","✧","✩","✪","✯","➠","➥","➪","➲","❥")
    R_START = random.choice(StartPm)
    emoji = ["😁", "🙃", "😎", "😃", "🤩", "😜", "😚", "😉", "😀", "😄","シ","ッ","ツ","ヅ"]
    R_END = random.choice(emoji)
    if os.path.exists(f"self.json"):
        with open("self.json", "r") as x:
            self = json.load(x)
        if text and message.chat.type == enums.chat_type.ChatType.CHANNEL and self["settings"]["firstcomment"] == "on":
            #print(message)

            if int(message.sender_chat.id) in self["firstcm_channels"]:
                await sleep(1)
                m = await Rex.get_discussion_message(message.sender_chat.id, message.id)
                await m.reply(self["firstcm_text"])

            if message.sender_chat.username in self["firstcm_channels"]:
                await sleep(1)
                m = await Rex.get_discussion_message(message.sender_chat.id, message.id)
                await m.reply(self["firstcm_text"])
            
        if self["settings"]["typing"] == "on":
            await Rex.send_chat_action(chat_id, enums.ChatAction.TYPING)
        if message.from_user:
            user = message.from_user.id
            if text[:7] == "offtime" and user == Helper:
                self["settings"]["offtime"] = int(text[8:10])
                with open(f"self.json", "w") as f:
                    json.dump(self, f, indent=4)
            elif text == "/fname" and user == Helper:
                await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = await Rex.resolve_peer(self["tempgp"]),
                            message = "chfname New First Name"
                        )
                    )
            elif text == "/lname" and user == Helper:
                await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = await Rex.resolve_peer(self["tempgp"]),
                            message = "chlname New Last Name"
                        )
                    )
            elif text == "/username" and user == Helper:
                await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = await Rex.resolve_peer(self["tempgp"]),
                            message = "chusername New Username without @"
                        )
                    )
            elif text == "/bio" and user == Helper:
                await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = await Rex.resolve_peer(self["tempgp"]),
                            message = "changebio New Bio"
                        )
                    )
            elif text == "dwnch" and user == Helper:
                await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = await Rex.resolve_peer(self["tempgp"]),
                            message = "dwnch Postid"
                        )
                    )
            elif text == "setchlock" and user == Helper:
                await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = await Rex.resolve_peer(self["tempgp"]),
                            message = "setchlock channel id"
                        )
                    )
            elif text == "addcm" and user == Helper:
                await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = await Rex.resolve_peer(self["tempgp"]),
                            message = "addcm_ch channel id or channel username"
                        )
                    )
            elif text == "removecm" and user == Helper:
                await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = await Rex.resolve_peer(self["tempgp"]),
                            message = "removecm_ch channel id or channel username"
                        )
                    )
            elif text == "cmtext" and user == Helper:
                await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = await Rex.resolve_peer(self["tempgp"]),
                            message = "cmtext text you want to Send for First Comment"
                        )
                    )
            elif text == "pic" and user == Helper:
                await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = await Rex.resolve_peer(self["tempgp"]),
                            message = "pic keyword"
                        )
                    )
            elif text == "music" and user == Helper:
                await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = await Rex.resolve_peer(self["tempgp"]),
                            message = "music keyword"
                        )
                    )
            elif text == "gif" and user == Helper:
                await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = await Rex.resolve_peer(self["tempgp"]),
                            message = "gif keyword"
                        )
                    )
            elif text == "game" and user == Helper:
                games = ["Neon Blaster","Neon Blaster 2","Block Buster","Gravity Ninja","Hexonix","Geometry Run 3D","Disco Ball"]
                result = await Rex.get_inline_bot_results("gamee", random.choice(games))
                await Rex.send_inline_bot_result(self["tempgp"], result.query_id, result.results[0].id)
            elif text == "/clbots" and user == Helper:
                bots = []
                async for m in Rex.get_chat_members(self["tempgp"], filter=enums.ChatMembersFilter.BOTS):
                    bots.append(m)
                    await Rex.ban_chat_member(self["tempgp"], m.user.id)
            elif text == "/cldel" and user == Helper:
                async for member in Rex.get_chat_members(self["tempgp"]):
                    if member.user.status == enums.UserStatus.LONG_AGO:
                        print("User status is LONG_AGO")
                        await Rex.ban_chat_member(self["tempgp"], member.user.id)
            elif text == "/clmsg" and user == Helper:
                msglist = []
                async for message in Rex.get_chat_history(self["tempgp"]):
                    print(message.text)
                    msglist.append(message.id)
                await Rex.delete_messages(self["tempgp"], msglist)
                for x in msglist:
                    await Rex.delete_messages(self["tempgp"], x)
                await Rex.send_message(self["tempgp"], f"{R_START} All Group Messages Successfully Deleted {R_END}")
            elif text == "/gpname" and user == Helper:
                await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = await Rex.resolve_peer(self["tempgp"]),
                            message = "gpname newname"
                        )
                    )
            elif text == "/gpdesc" and user == Helper:
                await Rex.invoke(
                        functions.messages.SaveDraft(
                            peer = await Rex.resolve_peer(self["tempgp"]),
                            message = "gpdesc reply to text"
                        )
                    )
            # elif text == "userprofile" and user == Helper:
            #     print(message)
            elif text == "muteall" and user == Helper:
                try:
                    await Rex.set_chat_permissions(self["tempgp"], ChatPermissions())
                    self["muteallhelper"] = "mute_enable"
                    #await Rex.send_message(self["tempgp"], f"{R_START} Group Muted now{R_END}")
                except errors.ChatAdminRequired:
                    #await Rex.send_message(self["tempgp"], f"{R_START} im not Admin in this Group {R_END}")
                    self["muteallhelper"] = "mute_admin"
                except errors.ChatNotModified:
                    #await Rex.send_message(self["tempgp"], f"{R_START} group muted allready {R_END}")
                    self["muteallhelper"] = "mute_enabled"
                finally:
                    with open(f"self.json", "w") as f:
                        json.dump(self, f, indent=4)
                
            elif text == "unmuteall" and user == Helper:
                try:
                    await Rex.set_chat_permissions(
                        self["tempgp"],
                        ChatPermissions(
                            can_send_messages=True,
                            can_send_media_messages=True,
                            can_send_other_messages=True,
                            can_send_polls=True,
                            can_add_web_page_previews=True,
                            can_invite_users=True
                        )
                    )
                    self["muteallhelper"] = "unmute_enable"
                    #await Rex.send_message(self["tempgp"], f"{R_START} Group Muted now{R_END}")
                except errors.ChatAdminRequired:
                    #await Rex.send_message(self["tempgp"], f"{R_START} im not Admin in this Group {R_END}")
                    self["muteallhelper"] = "unmute_admin"
                except errors.ChatNotModified:
                    #await Rex.send_message(self["tempgp"], f"{R_START} group muted allready {R_END}")
                    self["muteallhelper"] = "unmute_enabled"
                finally:
                    with open(f"self.json", "w") as f:
                        json.dump(self, f, indent=4)
            elif text == "فرزین" and user in self["friends"].values():
                await Rex.send_chat_action(chat_id, enums.ChatAction.TYPING)
                await sleep(1)
                await Rex.send_message(chat_id, "ژوون جیگر", reply_to_message_id=message.id)
            if text and user in self["enemys"].values():
                await Rex.send_chat_action(chat_id, enums.ChatAction.TYPING)
                await sleep(1)
                await Rex.send_message(chat_id, random.choice(fohsh), reply_to_message_id=message.id)
            elif text and user in self["enemygroup"].values():
                if message.chat.type == enums.chat_type.ChatType.SUPERGROUP:
                    await Rex.send_chat_action(chat_id, enums.ChatAction.TYPING)
                    await sleep(1)
                    await Rex.send_message(chat_id, random.choice(fohsh), reply_to_message_id=message.id)
            elif text and user in self["enemypv"].values():
                if message.chat.type == enums.chat_type.ChatType.PRIVATE:
                    await Rex.send_chat_action(chat_id, enums.ChatAction.TYPING)
                    await sleep(1)
                    await Rex.send_message(chat_id, random.choice(fohsh), reply_to_message_id=message.id)
            elif text and str(user) in self["enemyspecial"].keys() and int(chat_id) in self["enemyspecial"][str(user)]:
                await Rex.send_chat_action(chat_id, enums.ChatAction.TYPING)
                await sleep(1)
                await Rex.send_message(chat_id, random.choice(fohsh), reply_to_message_id=message.id)
            elif "😐" in text and self["settings"]["poker"] == "on":
                await Rex.send_chat_action(chat_id, enums.ChatAction.TYPING)
                await sleep(1)
                await Rex.send_message(chat_id, "😐", reply_to_message_id=message.id)
            elif text and message.chat.type == enums.chat_type.ChatType.PRIVATE and int(chat_id) in self["settings"]["mute"]:
                await Rex.delete_messages(chat_id, message.id)

            if text and message.chat.type == enums.ChatType.PRIVATE and user not in self["enemypv"] and user not in self["settings"]["mute"] and self["settings"]["monshi"] == "on":
                if user != sudo and user != self["monshiuser"]:
                    await sleep(1)
                    getme = await Rex.get_me()
                    if getme.last_online_date:
                        print(getme.last_online_date.minute)
                        now = time.localtime()
                        print(now.tm_min)
                        offmin = now.tm_min - getme.last_online_date.minute
                        print(offmin)
                        offtime = int(self["settings"]["offtime"])
                        if offmin >= offtime:
                        #if getme.status == enums.UserStatus.OFFLINE:
                            await Rex.send_chat_action(chat_id, enums.ChatAction.TYPING)
                            await Monshi(Rex, message)
            else:
                pass

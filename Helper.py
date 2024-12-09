from asyncio import sleep
from pyrogram import Client, filters, enums, errors
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from pyromod.helpers import ikb
from pyromod import listen
import random
import json
from functions.func import Enemy, AddFriend, RemoveFriend, Inline_ChangeMod, first_comment, inline_mute, inline_selfstatus

print("Helper Running")
helper = Client(
    "SelfHelper",
    api_id = 27227089,
    api_hash = "03ac3b8dd6a14cf5a231203db4660f59",
    bot_token = "8020661908:AAFqAHx0GvscnyARVXUcr-YsMhnTQPDs53I"
)

sudo = 7803950092


StartPm = ("♛","♚","⌯","♤","⇌","↯","●","₪","✧","✩","✪","✯","➲","❥")
R_START = random.choice(StartPm)
emoji = ["😁", "🙃", "😎", "😃", "🤩", "😜", "😚", "😉", "😀", "😄","シ","ッ","ツ","ヅ"]
R_END = random.choice(emoji)


user_menu = ikb([
    [("Profile info 👤", "/userprofile")],
    [("Enemy 😈", "/enemy"), ("Friend 👻", "/friend")],
    [(f"{R_START} Close", "/shutup")]
])

friend_menu = ikb([
    [(f"{R_START} Remove Friend", "/removefriend"), (f"{R_START} Add Friend", "/addfriend")],
    [(f"{R_START} Back", "/backmain")]
])


helpergpkeyboard = ikb([
    [("Self Status 🚬", "/self")],
    [("Profile Settings 🎩", "/profile"), ("Group Settings 👥", "/group")],
    [("Options 🧤", "/options"), ("Fun 💥", "/funs")],
    [("Reload ♻️", "/reload"), ("Ping 🔹", "/ping")],
    [(f"{R_START} Close", "/shutup")]
])

helperkeyboard = ikb([
    [("Self Status 🚬", "/self")],
    [("Profile Settings 🎩", "/profile")],
    [("Options 🧤", "/options"), ("Fun 💥", "/funs")],
    [("Reload ♻️", "/reload"), ("Ping 🔹", "/ping")],
    [(f"{R_START} Close", "/shutup")]
])

profile_menu = ikb([
    [(f"{R_START} First Name {R_START}", "/fname"), (f"{R_START} Last Name {R_START}", "/lname")],
    [(f"{R_START} UserName {R_START}", "/username"), (f"{R_START} Bio {R_START}", "/bio")],
    [(f"{R_START} Back", "/backmain")]
])

group_menu = ikb([
    [(f"{R_START} Group Name {R_START}", "/gpname"), (f"{R_START} Group Description {R_START}", "/gpdesc")],
    [(f"{R_START} Group Cleans 🗑", "/gpclean"), ("Mute Group 🔇", "/muteall")],
    [(f"{R_START} Back", "/backmain")]
])

clean_menu = ikb([
    [(f"{R_START} Clean Bots {R_START}", "/clbots"), (f"{R_START} Clean Deleted Accounts {R_START}", "/cldel")],
    [(f"{R_START} Clean all Messages in Group {R_START}", "/clmsg")],
    [(f"{R_START} Back", "/group")]
])


options_menu = ikb([
    [("Typing Mod ⌨️", "/typing"), ("Poker Mod 😐", "/poker")],
    [("First Comment Channels 💬", "/firstcm")],
    [("Secretary 👩🏽", "/monshi"),("Secretary Time 🕛", "/offtime")],
    [("Set Locked Channel 🔑", "/setchlock")],
    [("Enemys List 🤬", "/enemylist"),("Friends List 👻", "/friendlist")],
    [("Mute User 🔇", "/mute")],
    [("Bold Mod 🖊", "/bold"), ("FØÑτ Mod 🖊","/font")],
    [("Underline Mod 🖊","/underline")],
    [("InlineText Mod 🖊", "/inlinetext"), ("Mention Mod 🖊","/mention")],
    [(f"{R_START} Back", "/backmain")]
])

fun_menu = ikb([
    [("Download from Locked Channels 📥", "/dwnch")],
    [("Game 🧩", "/game"), ("Wallpaper 🏞", "/pic")],
    [("Music 🎧", "/music"), ("Gif 💦", "/gif")],
    [(f"{R_START} Back", "/backmain")]
])

enemylist_menu = ikb([
    [(f"{R_START} All", "/alllist"), (f"{R_START} Pv", "/pvlist"), (f"{R_START} Groups", "/gpslist")],
    [(f"{R_START} Back", "/backoptions")]
])

muteall_menu = ikb([
    [(f"{R_START} Disable", "/mutealloff"), (f"{R_START} Enable", "/muteallon")],
    [(f"{R_START} Back", "/backoptions")]
])

backmain_button = ikb([
    [(f"{R_START} Back","/backmain")]
])


backoptions_button = ikb([
    [(f"{R_START} Back","/backoptions")]
])

backfuns_button = ikb([
    [(f"{R_START} Back","/backfuns")]
])

backuser_button = ikb([
    [(f"{R_START} Back","/backuser")]
])

backgp_button = ikb([
    [(f"{R_START} Back","/group")]
])


backclean_button = ikb([
    [(f"{R_START} Back","/gpclean")]
])

backcomment_button = ikb([
    [(f"{R_START} Back","/firstcm")]
])

async def reload(helper, call):
    global StartPm
    global emoji
    R_START = random.choice(StartPm)
    R_END = random.choice(emoji)
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
        try:
            await helper.edit_inline_text(call.inline_message_id, f"**{char}**")
            await sleep(0.4)
        except errors.FloodWait as x:
            print(f"Sleeping {x.value} Seconds :)")
            await sleep(x.value)

@Inline_ChangeMod
async def inline_typing(helper, call, mod):
    pass
    

@Inline_ChangeMod
async def inline_poker(helper, call, mod):
    pass

@Inline_ChangeMod
async def inline_monshi(helper, call, mod):
    pass

@Inline_ChangeMod
async def inline_font(helper, call, mod):
    pass

@Inline_ChangeMod
async def inline_bold(helper, call, mod):
    pass

@Inline_ChangeMod
async def inline_underline(helper, call, mod):
    pass

@Inline_ChangeMod
async def inline_inlinetext(helper, call, mod):
    pass

@Inline_ChangeMod
async def inline_mention(helper, call, mod):
    pass

async def inline_offtime(helper, call):
    global StartPm
    global emoji
    R_START = random.choice(StartPm)
    R_END = random.choice(emoji)
    callmsg = call.data
    with open("self.json", "r") as x:
        self = json.load(x)
    offtime = self["settings"]["offtime"]
    offtime_menu = ikb([
        [(f"{R_START} Secretary Enable Time at Now is {offtime} Minutes", "/")],
        [("5 min 🕐","/5"),("10 min 🕑","/10"),("15 min 🕒","/15"),("20 min 🕓","/20")],
        [("30 min 🕕","/30"),("40 min 🕗","/40"),("50 min 🕙","/50"),("60 min 🕛","/60")],
        [(f"{R_START} Back", "/backoptions")]
    ])
    if callmsg == "/offtime":
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} Please Select Wich Time you Want to After that Secretary Enabled {R_END}", reply_markup=offtime_menu)
    
    elif callmsg != "/offtime":
        if callmsg == "/5":
            callmsg = "5"
            await helper.send_message(sudo, f"offtime {callmsg}")
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} **Monshi Enable Time** Setted to {callmsg} Minutes {R_END}", reply_markup=backoptions_button)
        else:
            await helper.send_message(sudo, f"offtime {callmsg[1:3]}")
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} **Monshi Enable Time** Setted to {callmsg[1:3]} Minutes {R_END}", reply_markup=backoptions_button)
        

enemy_menu = ikb(
    [
        [(f"{R_START} Add Enemy", "/addenemy"), (f"{R_START} Remove Enemy", "/remenemy")],
        [(f"{R_START} Close", "/shutupenemy")]
    ]
)

enemy_choose = ikb(
    [
        [(f"{R_START} All", "/all"), (f"{R_START} Pv", "/pv"), (f"{R_START} Groups", "/gps"), (f"{R_START} Here", "/here")],
        [(f"{R_START} Close", "/shutupenemy")]
    ]
)


@helper.on_inline_query()
def answer(helper, inline_query):
    global StartPm
    R_START = random.choice(StartPm)
    global emoji
    R_END = random.choice(emoji)
    #print(inline_query)
    inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="Self Panel",
                input_message_content=InputTextMessageContent(
                    f"{R_START}  Welcome To **Self Panel**"
                ),
                url="https://RexDesign.ir",
                description="وب سایت ما",
                thumb_url="https://Rexdesign.ir/wp-content/uploads/2021/08/47866422e33448aa9306810cdc1eecad.png",
                reply_markup=helperkeyboard
            ),
            InlineQueryResultArticle(
                title="Self Panel",
                input_message_content=InputTextMessageContent(
                    f"{R_START}  Welcome To **Self Panel**"
                ),
                url="https://RexDesign.ir",
                description="وب سایت ما",
                thumb_url="https://Rexdesign.ir/wp-content/uploads/2021/08/47866422e33448aa9306810cdc1eecad.png",
                reply_markup=helpergpkeyboard
            ),
            InlineQueryResultArticle(
                title="Enemy Panel",
                input_message_content=InputTextMessageContent(
                    f"{R_START}  Welcome To **Enemy Panel**"
                ),
                url="https://RexDesign.ir",
                description="وب سایت ما",
                thumb_url="https://Rexdesign.ir/wp-content/uploads/2021/08/47866422e33448aa9306810cdc1eecad.png",
                reply_markup=enemy_menu
            ),
            InlineQueryResultArticle(
                title="User Panel",
                input_message_content=InputTextMessageContent(
                    f"{R_START} Welcome To **User Panel**"
                ),
                url="https://RexDesign.ir",
                description="وب سایت ما",
                thumb_url="https://Rexdesign.ir/wp-content/uploads/2021/08/47866422e33448aa9306810cdc1eecad.png",
                reply_markup=user_menu
            )
        ],
        cache_time=1
    )

@helper.on_callback_query(filters.user(sudo))
async def answer(helper, call):
    global StartPm
    R_START = random.choice(StartPm)
    global emoji
    R_END = random.choice(emoji)
    #print(call)
    with open("self.json", "r") as x:
        self = json.load(x)
    callmsg = call.data
    if callmsg == "/self" :
        await inline_selfstatus(helper, call)
    if callmsg == "/selfon" :
        await inline_selfstatus(helper, call)
    if callmsg == "/selfoff" :
        await inline_selfstatus(helper, call)
    if callmsg == "/options":
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} Please Select Wich Options you Want to Enable {R_END}", reply_markup=options_menu)
    elif callmsg == "/enemy":
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} Welcome To **Enemy Panel** {R_END}", reply_markup=enemy_menu)
    elif callmsg == "/friend":
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} Welcome To **Friend Panel** {R_END}", reply_markup=friend_menu)
    elif callmsg == "/reload":
        await reload(helper, call)
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} Welcome Again To **Self Panel** {R_END}", reply_markup=helperkeyboard)
    elif callmsg == "/ping":
        await call.answer(f"{R_START} Im Online allways {R_END}", show_alert=True)
    elif callmsg == "/funs" or callmsg == "/backfuns":
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} Please Select Wich Funs method you Want {R_END}", reply_markup=fun_menu)
    elif callmsg == "/profile":
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} Please Select What Changes you Want to Enable on your Account {R_END}", reply_markup=profile_menu)
    elif callmsg == "/fname":
        await helper.send_message(sudo, "/fname")
        await call.answer(f"{R_START} Please Send command in your Draft with New First Name you want to Enable {R_END}", show_alert=True)
    elif callmsg == "/lname":
        await helper.send_message(sudo, "/lname")
        await call.answer(f"{R_START} Please Send command in your Draft with New Last Name you want to Enable {R_END}", show_alert=True)
    elif callmsg == "/username":
        await helper.send_message(sudo, "/username")
        await call.answer(f"{R_START} Please Send command in your Draft with New Username you want to Enable {R_END}", show_alert=True)
    elif callmsg == "/bio":
        await helper.send_message(sudo, "/bio")
        await call.answer(f"{R_START} Please Send command in your Draft with New Bio you want to Enable {R_END}", show_alert=True)
    elif callmsg == "/group":
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} Please Select What Changes you Want to Enable on this Group {R_END}", reply_markup=group_menu)
    elif callmsg == "/gpname":
        await helper.send_message(sudo, "/gpname")
        await call.answer(f"{R_START} Please Send command in your Draft with New Group Name you want to Enable {R_END}", show_alert=True)
    elif callmsg == "/gpdesc":
        await helper.send_message(sudo, "/gpdesc")
        await call.answer(f"{R_START} Please Send command in your Draft and Reply to New Group Description you want to Set {R_END}", show_alert=True)
    elif callmsg == "/gpclean":
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} Please Select What Clean Method you Want to Run on this Group {R_END}", reply_markup=clean_menu)
    elif callmsg[:3] == "/cl":
        await helper.send_message(sudo, str(callmsg))
        if callmsg[3:] == "bots":
            cltext = f"{R_START} All Bots Successfully Banned from Group {R_END}"
        elif callmsg[3:] == "del":
            cltext = f"{R_START} All Deleted Accounts Successfully Banned from Group {R_END}"
        await helper.edit_inline_text(call.inline_message_id, cltext, reply_markup=backclean_button)
    elif callmsg == "/userprofile":
        with open("self.json", "r") as x:
            self = json.load(x)
        user_name = self["userprofile"]["name"]
        user_id = self["userprofile"]["id"]
        user_username = self["userprofile"]["username"]
        userprofile_menu = ikb([
            [(f"{R_START} Name: {user_name}","/")],
            [(f"{R_START} ID: {user_id}","/")],
            [(f"{R_START} UserName: {user_username}","/")],
            [(f"{R_START} Back","/backuser")],
        ])
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} User Info is here {R_END}", reply_markup=userprofile_menu)
    elif callmsg == "/backuser":
        await helper.edit_inline_text(call.inline_message_id, f"↬ Welcome To **User Panel**", reply_markup=user_menu)
    elif callmsg == "/backmain":
        with open("self.json", "r") as x:
            self = json.load(x)
        if "-100" in str(self["tempgp"]):
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} Welcome To **Self Panel** {R_END}", reply_markup=helpergpkeyboard)
        else:
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} Welcome To **Self Panel** {R_END}", reply_markup=helperkeyboard)
    elif callmsg == "/typing":
        await inline_typing(helper, call, "typing")
    elif callmsg == "/typingon":
        await inline_typing(helper, call, "typing")
    elif callmsg == "/typingoff":
        await inline_typing(helper, call, "typing")
    elif callmsg == "/poker":
        await inline_poker(helper, call, "poker")
    elif callmsg == "/pokeron":
        await inline_poker(helper, call, "poker")
    elif callmsg == "/pokeroff":
        await inline_poker(helper, call, "poker")
    elif callmsg == "/monshi":
        await inline_monshi(helper, call, "monshi")
    elif callmsg == "/monshion":
        await inline_monshi(helper, call, "monshi")
    elif callmsg == "/monshioff":
        await inline_monshi(helper, call, "monshi")
    elif callmsg == "/mute":
        with open("self.json", "r") as x:
            self = json.load(x)
        print(self["tempgp"])
        if "-" not in str(self["tempgp"]):
            await inline_mute(helper, call)
        else:
            await call.answer(f"{R_START} This Method Can be use only in Private Chats {R_END}", show_alert = False)
    elif callmsg == "/muteon":
        await inline_mute(helper, call)
    elif callmsg == "/muteoff":
        await inline_mute(helper, call)
    elif callmsg == "/font":
        await inline_font(helper, call, "font")
    elif callmsg == "/fonton":
        await inline_font(helper, call, "font")
    elif callmsg == "/fontoff":
        await inline_font(helper, call, "font")
    elif callmsg == "/bold":
        await inline_bold(helper, call, "bold")
    elif callmsg == "/boldon":
        await inline_bold(helper, call, "bold")
    elif callmsg == "/boldoff":
        await inline_bold(helper, call, "bold")
    elif callmsg == "/underline":
        await inline_underline(helper, call, "underline")
    elif callmsg == "/underlineon":
        await inline_underline(helper, call, "underline")
    elif callmsg == "/underlineoff":
        await inline_underline(helper, call, "underline")
    elif callmsg == "/inlinetext":
        await inline_inlinetext(helper, call, "inlinetext")
    elif callmsg == "/inlinetexton":
        await inline_inlinetext(helper, call, "inlinetext")
    elif callmsg == "/inlinetextoff":
        await inline_inlinetext(helper, call, "inlinetext")
    elif callmsg == "/mention":
        await inline_mention(helper, call, "mention")
    elif callmsg == "/mentionon":
        await inline_mention(helper, call, "mention")
    elif callmsg == "/mentionoff":
        await inline_mention(helper, call, "mention")
    elif callmsg == "/offtime":
        await inline_offtime(helper, call)
    elif callmsg == "/5":
        await inline_offtime(helper, call)
    elif callmsg == "/10":
        await inline_offtime(helper, call)
    elif callmsg == "/15":
        await inline_offtime(helper, call)
    elif callmsg == "/20":
        await inline_offtime(helper, call)
    elif callmsg == "/30":
        await inline_offtime(helper, call)
    elif callmsg == "/40":
        await inline_offtime(helper, call)
    elif callmsg == "/50":
        await inline_offtime(helper, call)
    elif callmsg == "/60":
        await inline_offtime(helper, call)
    elif callmsg == "/muteall":
        with open("self.json", "r") as x:
            self = json.load(x)
        print(self["tempgp"])
        if "-" in str(self["tempgp"]):
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} Please Select Wich Options you Want to Enable {R_END}", reply_markup=muteall_menu)
        else:
            await call.answer(f"{R_START} This Method Can't be used in Private Chats {R_END}", show_alert = False)
    elif callmsg == "/muteallon":
        await helper.send_message(sudo, "muteall")
        await sleep(1)
        with open("self.json", "r") as x:
            self = json.load(x)
        if self["muteallhelper"] == "mute_enable":
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} Group Muted now{R_END}", reply_markup=backgp_button)
        elif self["muteallhelper"] == "mute_admin":
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} im not Admin in this Group {R_END}", reply_markup=backgp_button)
        elif self["muteallhelper"] == "mute_enabled":
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} group muted allReady {R_END}", reply_markup=backgp_button)
    elif callmsg == "/mutealloff":
        await helper.send_message(sudo, "unmuteall")
        await sleep(1)
        with open("self.json", "r") as x:
            self = json.load(x)
        if self["muteallhelper"] == "unmute_enable":
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} Group UnMuted now{R_END}", reply_markup=backgp_button)
        elif self["muteallhelper"] == "unmute_admin":
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} im not Admin in this Group {R_END}", reply_markup=backgp_button)
        elif self["muteallhelper"] == "unmute_enabled":
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} Group UnMuted allReady {R_END}", reply_markup=backgp_button)
    elif callmsg == "/friendlist":
        with open("self.json", "r") as x:
            self = json.load(x)
        friendlist = [str(x) for x in self["friends"].keys()]
        results = []
        for x in range(len(friendlist)):
            results.append(InlineKeyboardButton(friendlist[x], url = f'tg://openmessage?user_id={self["friends"][friendlist[x]]}'))   
        results.append(InlineKeyboardButton(f"{R_START} Back", callback_data="/backoptions"))
        keyboard_elements = [[element] for element in results]
        friend_list = InlineKeyboardMarkup(inline_keyboard=keyboard_elements)    
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} **Here is your Friends List** {R_END}", reply_markup = friend_list)
    elif callmsg == "/enemylist":
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} **Enemys List in Global & Super Groups & Private Chats** {R_END}", reply_markup = enemylist_menu)
    elif callmsg == "/alllist":
        with open("self.json", "r") as x:
            self = json.load(x)
        enemyglobal = [str(x) for x in self["enemys"].keys()]
        results = []
        if len(enemyglobal) < 1:
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} List is Empty {R_END}", reply_markup = backoptions_button)
        else:
            for x in range(len(enemyglobal)):
                results.append(InlineKeyboardButton(enemyglobal[x], url = f'tg://openmessage?user_id={self["enemys"][enemyglobal[x]]}'))   
            results.append(InlineKeyboardButton(f"{R_START} Back", callback_data="/enemylist"))
            keyboard_elements = [[element] for element in results]
            enemy_list = InlineKeyboardMarkup(inline_keyboard=keyboard_elements)    
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} List of Global Enemys {R_END}", reply_markup = enemy_list)
    elif callmsg == "/pvlist":
        with open("self.json", "r") as x:
            self = json.load(x)
        enemypv = [str(x) for x in self["enemypv"].keys()]
        results = []
        if len(enemypv) < 1:
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} List is Empty {R_END}", reply_markup = backoptions_button)
        else:
            for x in range(len(enemypv)):
                results.append(InlineKeyboardButton(enemypv[x], url = f'tg://openmessage?user_id={self["enemypv"][enemypv[x]]}'))   
            results.append(InlineKeyboardButton(f"{R_START} Back", callback_data="/enemylist"))
            keyboard_elements = [[element] for element in results]
            enemypv_list = InlineKeyboardMarkup(inline_keyboard=keyboard_elements)    
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} List of Enemys in Private Chats {R_END}", reply_markup = enemypv_list)
    elif callmsg == "/gpslist":
        with open("self.json", "r") as x:
            self = json.load(x)
        enemygroup = [str(x) for x in self["enemygroup"].keys()]
        results = []
        if len(enemygroup) < 1:
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} List is Empty {R_END}", reply_markup = backoptions_button)
        else:
            for x in range(len(enemygroup)):
                results.append(InlineKeyboardButton(enemygroup[x], url = f'tg://openmessage?user_id={self["enemygroup"][enemygroup[x]]}'))   
            results.append(InlineKeyboardButton(f"{R_START} Back", callback_data="/enemylist"))
            keyboard_elements = [[element] for element in results]
            enemygp_list = InlineKeyboardMarkup(inline_keyboard=keyboard_elements)    
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} List of Enemys in Super Groups {R_END}", reply_markup = enemygp_list)
    elif callmsg == "/backoptions":
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} Please Select Wich Options you Want to Enable {R_END}", reply_markup=options_menu) 
    elif callmsg == "/dwnch":
        await helper.send_message(sudo, "dwnch")
        await call.answer(f"{R_START} Please Send command in your Draft with Channel post id for Download Post from Private Channel {R_END}", show_alert=True)
    elif callmsg == "/setchlock":
        await helper.send_message(sudo, "setchlock")
        await call.answer(f"{R_START} Please Send command in your Draft with Channel id or username for setting New Private Channel {R_END}", show_alert=True)
    elif callmsg == "/firstcm":
        await first_comment(helper, call)
    elif callmsg == "/addcm":
        await first_comment(helper, call)
    elif callmsg == "/removecm":
        await first_comment(helper, call)
    elif callmsg == "/cmtext":
        await first_comment(helper, call)
    elif callmsg == "/firstcmlist":
        await first_comment(helper, call)
    elif callmsg == "/firstcmon":
        await first_comment(helper, call)
    elif callmsg == "/firstcmoff":
        await first_comment(helper, call)

    elif callmsg == "/game":
        await helper.send_message(sudo, "game")
    elif callmsg == "/pic":
        await helper.send_message(sudo, "pic")
        await call.answer(f"{R_START} Please Send command in your Draft with keyword you want {R_END}", show_alert=True)
    elif callmsg == "/music":
        await helper.send_message(sudo, "music")
        await call.answer(f"{R_START} Please Send command in your Draft with keyword you want {R_END}", show_alert=True)
    elif callmsg == "/gif":
        await helper.send_message(sudo, "gif")
        await call.answer(f"{R_START} Please Send command in your Draft with keyword you want {R_END}", show_alert=True)
    elif callmsg == "/addfriend":
        with open("self.json", "r") as x:
            self = json.load(x)
        if self["userprofile"]["id"] in self["friends"].values():
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} User AllReady in Friend List {R_END}")
        else:
            addfriend = AddFriend(self["userprofile"]["name"], self["userprofile"]["id"], self["tempgp"])
            #await friend(helper, call, self["userprofile"]["name"], self["userprofile"]["id"], self["tempgp"])
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} user Become your Friend Now {R_END}", reply_markup=backuser_button)
    elif callmsg == "/removefriend":
        with open("self.json", "r") as x:
            self = json.load(x)
        if self["userprofile"]["id"] not in self["friends"].values():
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} User not in Friend List {R_END}")
        else:
            remfriend = RemoveFriend(self["userprofile"]["name"], self["userprofile"]["id"], self["tempgp"])
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} user Removed from your Friend List {R_END}", reply_markup=backuser_button)
            #await friend(helper, call, self["userprofile"]["name"], self["userprofile"]["id"], self["tempgp"])
    elif callmsg == "/addenemy":
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} Please Select Wich Enemy Mod you Want to Take on the User {R_END}", reply_markup=enemy_choose)
    elif callmsg == "/all":
        with open("self.json", "r") as x:
            self = json.load(x)
        if self["tempenemy_id"] in self["enemys"].values():
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} User AllReady is Enemy Globally {R_END}")
        else:
            await Enemy.SetEnemyall(self["tempenemy_name"], int(self["tempenemy_id"]))
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} User Become Enemy Globally {R_END}")
    elif callmsg == "/pv":
        with open("self.json", "r") as x:
            self = json.load(x)
        if self["tempenemy_id"] in self["enemypv"].values():
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} User AllReady is Enemy in Private Chat {R_END}")
        else:
            await Enemy.SetEnemyPrivate(self["tempenemy_name"], int(self["tempenemy_id"]))
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} User Become Enemy in Private Chat {R_END}")
    elif callmsg == "/gps":
        with open("self.json", "r") as x:
            self = json.load(x)
        if self["tempenemy_id"] in self["enemygroup"].values():
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} User AllReady is Enemy in all Common Groups {R_END}")
        else:
            await Enemy.SetEnemyGroup(self["tempenemy_name"], int(self["tempenemy_id"]))
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} User Become Enemy in all Common Groups {R_END}")
    elif callmsg == "/here":
        with open("self.json", "r") as x:
            self = json.load(x)
        print(self["tempgp"])
        print(self["tempenemy_id"])
        print(self["enemyspecial"])
        if str(self["tempenemy_id"]) in self["enemyspecial"]:
            print("ok")
            if self["tempgp"] in self["enemyspecial"][str(self["tempenemy_id"])]:
                await helper.edit_inline_text(call.inline_message_id, f"{R_START} User AllReady is Enemy here {R_END}")
            else:
                await Enemy.SetEnemySpecial(int(self["tempgp"]), int(self["tempenemy_id"]))
                await helper.edit_inline_text(call.inline_message_id, f"{R_START} User Become Enemy in here {R_END}")
        else:
            await Enemy.SetEnemySpecial(int(self["tempgp"]), int(self["tempenemy_id"]))
            await helper.edit_inline_text(call.inline_message_id, f"{R_START} User Become Enemy in here {R_END}")
    elif callmsg == "/remenemy":
        with open("self.json", "r") as x:
            self = json.load(x)
        await Enemy.RemEnemyByReply(self["tempgp"], self["tempenemy_name"], self["tempenemy_id"])
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} User Removed from all Enemy lists {R_END}")
    elif callmsg == "/shutup":
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} Self Panel Closed! {R_END}")
    elif callmsg == "/shutupenemy":
        await helper.edit_inline_text(call.inline_message_id, f"{R_START} Enemy Panel Closed! {R_END}")


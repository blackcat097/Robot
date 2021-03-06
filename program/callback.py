# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π§π΅πΆπ πΆπ ππ΅π² ππ‘πππ  πππ©...!**
βββββββββββββββββββ
β£Β» α΄α΄ α΄α΄κ±Ιͺα΄ α΄Κα΄Κα΄Κ Κα΄α΄. 
β£Β» ΚΙͺΙ’Κ Η«α΄α΄ΚΙͺα΄Κ α΄α΄κ±Ιͺα΄.
β£Β» α΄ Ιͺα΄α΄α΄ α΄Κα΄Κ κ±α΄α΄α΄α΄Κα΄α΄α΄.
β£Β» α΄α΄α΄ α΄Ι΄α΄α΄α΄ κ°α΄α΄α΄α΄Κα΄κ±.
β£Β» κ±α΄α΄α΄Κκ°α΄κ±α΄ κ±α΄α΄α΄α΄.
βββββββββββββββββββ
α΄α΄κ±ΙͺΙ’Ι΄α΄α΄ ΚΚ :**[ππ‘πππ  πππ©](https://t.me/The_cat_lover0)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("α΄α΄α΄α΄α΄Ι΄α΄ ΚΙͺκ±α΄", callback_data="cbcmds"),
                ],[
                    InlineKeyboardButton(
                        "κ±α΄α΄α΄α΄Κα΄", url=f"https://t.me/catmusicworld"
                    ),
                    InlineKeyboardButton(
                        "α΄α΄α΄α΄α΄α΄κ±", url=f"https://t.me/catmusicworld"
                    ),
                ],[
                    InlineKeyboardButton(
                        "π ππ‘πππ  πππ©π",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β **Basic Guide for using this bot:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

π **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

π‘ **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π ππ‘πππ  πππ©", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π **Κα΄ΚΚα΄α΄‘ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

Β» κ°α΄Κ α΄Ι΄α΄α΄‘ΙͺΙ΄Ι’ α΄ α΄α΄α΄α΄α΄Ι΄α΄ ΚΙͺκ±α΄ α΄ ΚΚα΄α΄α΄α΄α΄α΄ α΄Κα΄κ±κ± α΄Κα΄ Κα΄α΄α΄α΄Ι΄κ± Ι’Ιͺα΄ α΄Ι΄ Κα΄Κα΄α΄‘ α΄Ι΄α΄ Κα΄α΄α΄ α΄α΄α΄α΄α΄Ι΄α΄κ± α΄xα΄Κα΄Ι΄α΄α΄Ιͺα΄Ι΄.

** πππ‘ππ  πππ© ππ¨ ππ€π§ πͺ ππ.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("α΄α΄α΄ΙͺΙ΄ α΄α΄α΄", callback_data="cbadmin"),
                    InlineKeyboardButton("κ±α΄α΄α΄ α΄α΄α΄", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("Κα΄κ±Ιͺα΄ α΄α΄α΄", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("π α΄α΄α΄α΄‘ Κα΄α΄α΄", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""α΄α΄α΄α΄‘ Κα΄κ±Ιͺα΄ α΄α΄α΄α΄α΄Ι΄α΄κ± :

Β» /play [κ±α΄Ι΄Ι’ Ι΄α΄α΄α΄/ΚΙͺΙ΄α΄] - α΄Κα΄Κ α΄α΄κ±Ιͺα΄ α΄Ι΄ α΄ Ιͺα΄α΄α΄ α΄Κα΄α΄ 
Β» /stream [Qα΄α΄ΚΚ/ΚΙͺΙ΄α΄] - κ±α΄Κα΄α΄α΄ α΄Κα΄ Κα΄ ΚΙͺα΄ α΄/Κα΄α΄Ιͺα΄ ΚΙͺα΄ α΄ α΄α΄κ±Ιͺα΄ 
Β» /vplay [α΄ Ιͺα΄α΄α΄ Ι΄α΄α΄α΄/ΚΙͺΙ΄α΄] - α΄Κα΄Κ α΄ Ιͺα΄α΄α΄ α΄Ι΄ α΄ Ιͺα΄α΄α΄ α΄Κα΄α΄ 
Β» /vstream - α΄Κα΄Κ ΚΙͺα΄ α΄ α΄ Ιͺα΄α΄α΄ κ°Κα΄α΄ Κα΄ ΚΙͺα΄ α΄/α΄3α΄8 
Β» /playlist - κ±Κα΄α΄‘ Κα΄α΄ α΄Κα΄ α΄Κα΄ΚΚΙͺκ±α΄ 
Β» /video [Qα΄α΄ΚΚ] - α΄α΄α΄‘Ι΄Κα΄α΄α΄ α΄ Ιͺα΄α΄α΄ κ°Κα΄α΄ Κα΄α΄α΄α΄Κα΄ 
Β» /song [Qα΄α΄ΚΚ] - α΄α΄α΄‘Ι΄Κα΄α΄α΄ κ±α΄Ι΄Ι’ κ°Κα΄α΄ Κα΄α΄α΄α΄Κα΄ 
Β» /lyrics [Qα΄α΄ΚΚ] - κ±α΄Κα΄α΄ α΄Κα΄ κ±α΄Ι΄Ι’ ΚΚΚΙͺα΄ 
Β» /search [Qα΄α΄ΚΚ] - κ±α΄α΄Κα΄Κ α΄ Κα΄α΄α΄α΄Κα΄ α΄ Ιͺα΄α΄α΄ ΚΙͺΙ΄α΄  
Β» /ping - κ±Κα΄α΄‘ α΄Κα΄ Κα΄α΄ α΄ΙͺΙ΄Ι’ κ±α΄α΄α΄α΄κ± 
Β» /uptime - κ±Κα΄α΄‘ α΄Κα΄ Κα΄α΄ α΄α΄α΄Ιͺα΄α΄ κ±α΄α΄α΄α΄κ± 
Β» /alive - κ±Κα΄α΄‘ α΄Κα΄ Κα΄α΄ α΄ΚΙͺα΄ α΄ ΙͺΙ΄κ°α΄ [ΙͺΙ΄ Ι’Κα΄α΄α΄]

**ππ‘πππ  πππ©**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π α΄α΄α΄α΄‘ Κα΄α΄α΄", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ΚΚα΄α΄α΄Ι΄ α΄α΄α΄ΙͺΙ΄ α΄α΄α΄α΄α΄Ι΄α΄κ± :

Β» /pause - α΄α΄α΄κ±α΄ α΄Κα΄ κ±α΄Κα΄α΄α΄ 
Β» /resume - Κα΄κ±α΄α΄α΄ α΄Κα΄ κ±α΄Κα΄α΄α΄ 
Β» /skip - κ±α΄‘Ιͺα΄α΄Κ α΄α΄ Ι΄α΄xα΄ κ±α΄Κα΄α΄α΄ 
Β» /stop - κ±α΄α΄α΄ α΄Κα΄ κ±α΄Κα΄α΄α΄ΙͺΙ΄Ι’ 
Β» /vmute - α΄α΄α΄α΄ α΄Κα΄ α΄κ±α΄ΚΚα΄α΄ α΄Ι΄ α΄ α΄Ιͺα΄α΄ α΄Κα΄α΄ 
Β» /vunmute - α΄Ι΄α΄α΄α΄α΄ α΄Κα΄ α΄κ±α΄ΚΚα΄α΄ α΄Ι΄ α΄ α΄Ιͺα΄α΄ α΄Κα΄α΄ 
Β» /volume 1-200 - α΄α΄α΄α΄κ±α΄ α΄Κα΄ α΄ α΄Κα΄α΄α΄ α΄κ° α΄α΄κ±Ιͺα΄ (α΄κ±α΄ΚΚα΄α΄ α΄α΄κ±α΄ Κα΄ α΄α΄α΄ΙͺΙ΄) 
Β» /reload - Κα΄Κα΄α΄α΄ Κα΄α΄ α΄Ι΄α΄ Κα΄κ°Κα΄κ±Κ α΄Κα΄ α΄α΄α΄ΙͺΙ΄ α΄α΄α΄α΄ 
Β» /userbotjoin - ΙͺΙ΄α΄ Ιͺα΄α΄ α΄Κα΄ α΄κ±α΄ΚΚα΄α΄ α΄α΄ α΄α΄ΙͺΙ΄ Ι’Κα΄α΄α΄ 
Β» /userbotleave - α΄Κα΄α΄Κ α΄κ±α΄ΚΚα΄α΄ α΄α΄ Κα΄α΄α΄ α΄ κ°Κα΄α΄ Ι’Κα΄α΄α΄

**ππ‘πππ  πππ©.**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π α΄α΄α΄α΄‘ Κα΄α΄α΄", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""α΄α΄α΄α΄‘ κ±α΄α΄α΄ α΄α΄α΄α΄α΄Ι΄α΄κ± :

Β» /rmw - α΄Κα΄α΄Ι΄ α΄ΚΚ Κα΄α΄‘ κ°ΙͺΚα΄κ± 
Β» /rmd - α΄Κα΄α΄Ι΄ α΄ΚΚ α΄α΄α΄‘Ι΄Κα΄α΄α΄α΄α΄ κ°ΙͺΚα΄κ± 
Β» /sysinfo - κ±Κα΄α΄‘ α΄Κα΄ κ±Κκ±α΄α΄α΄ ΙͺΙ΄κ°α΄Κα΄α΄α΄Ιͺα΄Ι΄ 
Β» /update - α΄α΄α΄α΄α΄α΄ Κα΄α΄Κ Κα΄α΄ α΄α΄ Κα΄α΄α΄κ±α΄ α΄ α΄Κκ±Ιͺα΄Ι΄ 
Β» /restart - Κα΄κ±α΄α΄Κα΄ Κα΄α΄Κ Κα΄α΄ 
Β» /leaveall - α΄Κα΄α΄Κ α΄κ±α΄ΚΚα΄α΄ α΄α΄ Κα΄α΄α΄ α΄ κ°Κα΄α΄ α΄ΚΚ Ι’Κα΄α΄α΄

**ππ‘πππ  πππ© .**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π α΄α΄α΄α΄‘ Κα΄α΄α΄", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nΒ» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("π‘ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"βοΈ **α΄α΄α΄α΄‘ κ±α΄α΄α΄ΙͺΙ΄Ι’κ± κ°α΄Κ** {query.message.chat.title}\n\nβΈ : α΄α΄α΄α΄‘ α΄α΄α΄κ±α΄\nβΆοΈ : α΄α΄α΄α΄‘ Κα΄κ±α΄α΄α΄\nπ : α΄α΄α΄α΄‘ α΄α΄α΄α΄\nπ : α΄α΄α΄α΄‘ α΄Ι΄α΄α΄α΄α΄\nβΉ : α΄α΄α΄α΄‘ κ±α΄Κα΄α΄α΄ κ±α΄α΄α΄\n\nΒ© @catmusicworld",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("βΉ", callback_data="cbstop"),
                      InlineKeyboardButton("βΈ", callback_data="cbpause"),
                      InlineKeyboardButton("βΆοΈ", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("π", callback_data="cbmute"),
                      InlineKeyboardButton("π", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("π α΄α΄α΄α΄‘ α΄Κα΄κ±α΄", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("β nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("π‘ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()

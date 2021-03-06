from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""π **Hα΄α΄Κα΄ {message.from_user.mention()}**\n
π§π΅πΆπ πΆπ ππ΅π² π½π‘πππ  πππ©...!**
βββββββββββββββββββ
β£Β» α΄α΄ α΄α΄κ±Ιͺα΄ α΄Κα΄Κα΄Κ Κα΄α΄. 
β£Β» ΚΙͺΙ’Κ Η«α΄α΄ΚΙͺα΄Κ α΄α΄κ±Ιͺα΄.
β£Β» α΄ Ιͺα΄α΄α΄ α΄Κα΄Κ κ±α΄α΄α΄α΄Κα΄α΄α΄.
β£Β» α΄α΄α΄ α΄Ι΄α΄α΄α΄ κ°α΄α΄α΄α΄Κα΄κ±.
β£Β» κ±α΄α΄α΄Κκ°α΄κ±α΄ κ±α΄α΄α΄α΄.
βββββββββββββββββββ
α΄α΄κ±ΙͺΙ’Ι΄α΄α΄ ΚΚ :** [ππ‘πππ  πππ©](https://t.me/The_cat_lover0)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ΚΚα΄α΄α΄ α΄α΄α΄", callback_data="cbcmds"),
                ],[
                    InlineKeyboardButton(
                        "κ±α΄α΄α΄α΄Κα΄", url=f"https://t.me/catmusicworld"
                    ),
                    InlineKeyboardButton(
                        "α΄α΄α΄α΄α΄α΄κ±", url=f"https://t.me/catmusicworld"
                    ),
                ],[
                    InlineKeyboardButton(
                        "π ΚΚα΄α΄α΄ α΄α΄α΄ π",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("κ±α΄α΄α΄α΄Κα΄", url=f"https://t.me/catmusicworld"),
                InlineKeyboardButton(
                    "α΄α΄α΄α΄α΄α΄κ±", url=f"https://t.me/catmusicworld"
                ),
            ],[
                InlineKeyboardButton("α΄ΚΚ ΙͺΙ΄κ°α΄ Κα΄Κα΄", url=f"https://t.me/catmusicworld"),
            ]
        ]
    )

    alive = f"**Κα΄α΄Κα΄ {message.from_user.mention()}, α΄ΚΙͺκ± Ιͺκ± α΄Κα΄ ΚΚα΄α΄α΄ α΄α΄α΄.**\n\nΒ» α΄‘α΄Κα΄ΙͺΙ΄Ι’ Ι΄α΄Κα΄α΄ΚΚΚ\nΒ» α΄α΄ α΄α΄κ±α΄α΄Κ : [ππ‘πππ  πππ©](https://t.me/The_cat_lover0)\nΒ» Κα΄α΄ α΄ α΄Κκ±Ιͺα΄Ι΄ : `v{__version__}`\nΒ» α΄ΚΚα΄ α΄ α΄Κκ±Ιͺα΄Ι΄ : `{pyrover}`\nΒ» α΄Κα΄Κα΄Ι΄ α΄ α΄Κκ±Ιͺα΄Ι΄ : `{__python_version__}`\nΒ» α΄Κα΄Ι’α΄α΄ΚΚκ± : `{pytover.__version__}`\nΒ» α΄α΄α΄Ιͺα΄α΄ : `{uptime}`\n\n**α΄ΚΙͺκ± Ιͺκ± α΄Κα΄ α΄α΄ α΄α΄κ±Ιͺα΄ α΄Κα΄Κα΄Κ Κα΄α΄ α΄α΄κ±ΙͺΙ’Ι΄α΄α΄ α΄Ι΄α΄ α΄Κα΄α΄α΄α΄α΄ ΚΚ ΚΚα΄α΄α΄ α΄α΄α΄, α΄Κα΄Ι΄α΄α΄ α΄ α΄ΚΚ α΄α΄α΄Κ κ°α΄Κ α΄α΄α΄ΙͺΙ΄Ι’ Κα΄Κα΄..**\Ι΄\Ι΄Β© @The_cat_lover0"


    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("**Β» ΚΚα΄α΄α΄ α΄α΄α΄ α΄α΄Ι΄Ι’ κ°Κα΄α΄ ΚΚα΄α΄α΄ α΄α΄α΄ κ±α΄Κα΄ α΄Κ..**\n\nπ `PONG!!`\n" f"β‘οΈ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "**ΚΚα΄α΄α΄ α΄α΄α΄ α΄α΄ Κα΄α΄ κ±α΄α΄α΄α΄κ±.**\n\n"
        f"β’ **α΄α΄α΄Ιͺα΄α΄ :** `{uptime}`\n"
        f"β’ **κ±α΄α΄Κα΄ α΄α΄ :** `{START_TIME_ISO}`"
    )

@Client.on_message(filters.command("blackcat") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("**α΄ΚΙͺκ± Ιͺκ± α΄Κα΄ α΄α΄ Κα΄α΄ α΄‘ΚΙͺα΄Κ Ιͺκ± κ±α΄α΄α΄Ιͺκ°Ιͺα΄α΄ΚΚΚ α΄α΄κ±ΙͺΙ’Ι΄α΄α΄ ΚΚ ΚΚα΄α΄α΄ α΄α΄α΄.**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "α΄ΚΚ ΙͺΙ΄κ°α΄ Κα΄Κα΄", url="https://t.me/the_cat_lover0")
                ]
            ]
        )
   )

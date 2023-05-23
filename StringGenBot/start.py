from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID

def filter(cmd: str):

    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))

async def start(bot: Client, msg: Message):

    me2 = (await bot.get_me()).mention

    await bot.send_message(

        chat_id=msg.chat.id,

        text=f"""- اهـلا عـزيـزي العـضـو 

يـعـمل هـذا الـبوت لـمـساعـدتـك بـطـريقـة سـهله للـحصـول علـى كـود تـيـرمكس او كـود بـايـࢪوجـرام""",

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(text="بـدء الاسـتـخـراج", callback_data="generate")

                ],

                [

                    InlineKeyboardButton("الـمـطـور", url="https://t.me/F_V_3"),

                ]

            ]

        ),

        disable_web_page_preview=True,

    )

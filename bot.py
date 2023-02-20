# © All rights reserved by Mrvishal2k2
# Kangers dont f*ckin kang this !!!
# Should have to give credits 😏 else f***off 
# This is only for personal use Dont use this for ur bot channel business 😂
# Thanks to Mahesh Malekar for his Gplinks Bot !!

from os import environ
# Moved Back to asyncio-dev branch of pyrogram
from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup
import PyBypass as bypasser

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')

bot = Client('Shortlink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(Filters.command('start') & Filters.private)
async def start(bot, update):
    await update.reply(
        f"**Hello🌝 {update.chat.first_name}!**\n\n"
        "I'm A Bot To Unshorten The Link. I support many sites\n This is Still In Beta Testing @Crazy_Yadh")


@bot.on_message(Filters.regex(r'https?://[^\s]+') & Filters.private)
async def link_handler(bot, update):
    link = update.matches[0].group(0)
      def bypassed_link():
        bypassed_link = bypasser.bypass() 
        bypassed_link = bypasser.bypass(link)
        button = [[InlineKeyboardButton("ʙʏᴘᴀssᴇᴅ ʟɪɴᴋ", url=bypassed_link)]]
        markup = InlineKeyboardMarkup(button)
        await update.reply_text(text=f'Here is your shortlink \n`{bypassed_link}`', reply_markup=markup, quote=True)
        
      except Exception as e:
        await update.reply(f'Error: {e}', quote=True)

      

bot.run()

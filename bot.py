import os
import glob
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8758292937:AAEVpSPX8AL2Ag1SxHjFN1Ek6kUFYZlFdzQ"
FIRST_JOIN_LINK = "https://t.me/addlist/PepJQUTEoOQ4MzZk"
EXNESS_LINK = "https://one.exnessonelink.com/a/acjk8zdf2t"
VIP_CHANNEL_LINK = "https://t.me/+DcNTI-J8O-g1MjU0"
EXNESS_IMAGE_URL = "https://i.ibb.co/DDqS6rzP/IMG-20261001-001310-174.jpg"

WELCOME_PHOTOS = glob.glob("gold.*") + glob.glob("Gold.*")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    photo_sent = False
    if WELCOME_PHOTOS:
        try:
            with open(WELCOME_PHOTOS[0], 'rb') as photo:
                await context.bot.send_photo(
                    chat_id=chat_id,
                    photo=photo,
                    caption="👑 <b>Welcome to GoldProTrader VIP Hub!</b>",
                    parse_mode="HTML"
                )
                photo_sent = True
        except Exception as e:
            print(f"Welcome photo error: {e}")

    if not photo_sent:
        await context.bot.send_message(
            chat_id=chat_id,
            text="👑 <b>Welcome to GoldProTrader VIP Hub!</b>",
            parse_mode="HTML"
        )

    await asyncio.sleep(1)

    await context.bot.send_message(
        chat_id=chat_id,
        text="⏳ <b>Processing your access... Please wait a second!</b>",
        parse_mode="HTML"
    )

    await asyncio.sleep(1)

    welcome_text = (
        "👋 <b>𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗚𝗢𝗟𝗗 𝗣𝗥𝗢 𝗧𝗥𝗔𝗗𝗘𝗥</b>\n\n"
        "📈 If you've clicked on my ad, you're ready to explore Forex & Gold trading signals.\n\n"
        "🟡 <b>𝗫𝗔𝗨𝗨𝗦𝗗 𝗚𝗢𝗟𝗗 𝗦𝗜𝗚𝗡𝗔𝗟𝗦</b>\n"
        "💱 <b>𝗙𝗢𝗥𝗘𝗫 𝗦𝗜𝗚𝗡𝗔𝗟𝗦</b>\n"
        "🎯 Entry • TP • SL\n"
        "📊 Daily market analysis\n\n"
        "🚀 Join the channel to get the latest signals and market updates.\n\n"
        "⚠️ <i>Trading involves risk. Not financial advice.</i>"
    )
    keyboard1 = [[InlineKeyboardButton("🟢 JOIN CHANNEL 🟢", url=FIRST_JOIN_LINK)]]
    await context.bot.send_message(
        chat_id=chat_id,
        text=welcome_text,
        reply_markup=InlineKeyboardMarkup(keyboard1),
        parse_mode="HTML"
    )

    await asyncio.sleep(30)

    exness_text = (
        "💼 <b>CREATE YOUR TRADING ACCOUNT</b>\n\n"
        "To get free access to VIP signals, create your account on Exness and complete your deposit below! 👇"
    )
    keyboard2 = [[InlineKeyboardButton("🌐 REGISTER ON EXNESS 🌐", url=EXNESS_LINK)]]
    
    try:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=EXNESS_IMAGE_URL,
            caption=exness_text,
            reply_markup=InlineKeyboardMarkup(keyboard2),
            parse_mode="HTML"
        )
    except Exception as e:
        print(f"Exness photo error: {e}")
        await context.bot.send_message(
            chat_id=chat_id,
            text=exness_text,
            reply_markup=InlineKeyboardMarkup(keyboard2),
            parse_mode="HTML"
        )

    await asyncio.sleep(30)

    vip_request_text = (
        "🔒 <b>PRIVATE VIP CHANNEL ACCESS</b>\n\n"
        "After creating your Exness account, click the button below to send your join request!\n\n"
        "🔓 <b>UNLOCK VIP CONTENT NOW:</b>\n"
        "Contact Admin: @Jasonfx1e"
    )
    keyboard3 = [
        [InlineKeyboardButton("🔓 REQUEST VIP ACCESS 🔓", url=VIP_CHANNEL_LINK)],
        [InlineKeyboardButton("💬 CONTACT ADMIN (@Jasonfx1e)", url="https://t.me/Jasonfx1e")]
    ]
    await context.bot.send_message(
        chat_id=chat_id,
        text=vip_request_text,
        reply_markup=InlineKeyboardMarkup(keyboard3),
        parse_mode="HTML"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
  

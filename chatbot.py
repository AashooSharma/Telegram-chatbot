from telethon import TelegramClient, events
from dotenv import load_dotenv
import requests
import os

# Load API details from .env
load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

# 🔗 API Endpoint for smart reply
API_URL = "https://flask-chatbot-api.vercel.app/userMsg?msg="

# Create bot client
client = TelegramClient('chat_bot', api_id, api_hash).start(bot_token=bot_token)

# /start command
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    if event.sender.bot:  # ❌ Ignore messages from bots
        return

    await event.respond(
        "👋 Hello! I’m your Chat Bot girlfriend.\n"
        "Talk to me like you would to someone you love! ❤️\n\n"
        "Use /help for more info."
    )
    raise events.StopPropagation

# /help command
@client.on(events.NewMessage(pattern='/help'))
async def help_cmd(event):
    if event.sender.bot:  # ❌ Ignore messages from bots
        return

    await event.respond(
        "📖 *How to Use This Bot:*\n"
        "• /start – Get introduction\n"
        "• /help – Show this help\n"
        "• Just chat – I’ll talk with you sweetly 💌"
    )

# Chat replies using external API
@client.on(events.NewMessage)
async def chat(event):
    if event.sender.bot:  # ❌ Ignore messages from other bots
        return

    user_message = event.raw_text.strip()

    # Skip commands
    if user_message.startswith('/'):
        return

    try:
        # Call API for bot reply
        response = requests.get(API_URL + user_message)
        if response.status_code == 200:
            data = response.json()
            bot_reply = data.get("bot_reply")
            if bot_reply:
                await event.respond(bot_reply)
                return

        await event.respond("❌ I couldn't come up with a reply, love 😔")
    except Exception as e:
        print("Error:", e)
        await event.respond("⚠️ Something went wrong while fetching a reply.")

# Run the bot
async def main():
    me = await client.get_me()
    print(f"✅ Bot is running as: @{me.username}")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
      

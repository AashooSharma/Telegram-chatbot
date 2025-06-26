from telethon import TelegramClient, events
from dotenv import load_dotenv
import requests
import os

# Load API details from .env
load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

# Your GitHub JSON reply database
REPLY_DB_URL = "https://raw.githubusercontent.com/AashooSharma/My_reply_database/refs/heads/main/BigReplyDatabase.json"

def fetch_reply_database():
    try:
        res = requests.get(REPLY_DB_URL)
        if res.status_code == 200:
            return res.json().get("responses", [])
        else:
            print(f"❌ Failed to load reply database: {res.status_code}")
            return []
    except Exception as e:
        print("⚠️ Error fetching reply DB:", e)
        return []

reply_db = fetch_reply_database()

# Create the bot client
client = TelegramClient('chat_bot', api_id, api_hash).start(bot_token=bot_token)

# /start command
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond(
        "👋 Hello! I’m your Chat Bot girlfriend.\n"
        "Talk to me like you would to someone you love! ❤️\n\n"
        "Use /help for more info."
    )
    raise events.StopPropagation

# /help command
@client.on(events.NewMessage(pattern='/help'))
async def help_cmd(event):
    await event.respond(
        "📖 *How to Use This Bot:*\n"
        "• /start – Introduction\n"
        "• /help – Help info\n"
        "• Type things like: hi, i miss you, good morning, etc."
    )

# Smart reply from GitHub JSON
@client.on(events.NewMessage)
async def chat(event):
    user_text = event.raw_text.strip().lower()

    # Look for a matching input in reply_db
    reply = None
    for item in reply_db:
        if item["input"].lower() == user_text:
            reply = item["reply"]
            break

    if reply:
        await event.respond(reply)
    else:
        await event.respond("❌ I don't understand that yet, love. Try something else. 💬")

# Start bot
async def main():
    me = await client.get_me()
    print(f"✅ Bot is running as: @{me.username}")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
          

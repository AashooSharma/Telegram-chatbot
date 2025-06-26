# 🤖 Telegram ChatBot — Romantic AI Girlfriend Style

A sweet & smart Telegram chatbot built using **[Telethon](https://github.com/LonamiWebs/Telethon)** that replies based on romantic chat responses from an external **chat API**.

> 💌 "Hey love! I'm here to talk to you anytime, anywhere..."

---

### ✨ Features

* 🧠 **AI-style responses** from public API
* 🔐 Secure config using `.env` file
* 📩 Commands: `/start`, `/help`
* 🚫 Ignores other bots
* ✅ 24/7 ready for conversation

---

### 🛠️ Setup Instructions

#### 1. Clone the repository

```bash
git clone https://github.com/AashooSharma/Telegram-chatbot/
cd Telegram-chatbot
```

#### 2. Install requirements

```bash
pip install -r requirements.txt
```

#### 3. Create `.env` file

Create a file named `.env` and paste your bot details:

```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
```

> Get your API credentials from [my.telegram.org](https://my.telegram.org)

#### 4. Run the bot

```bash
python bot.py
```

---

### 🧠 API Used for Replies

Your bot sends messages to this API:

```
GET https://flask-chatbot-api.vercel.app/userMsg?msg=<your-message>
```

It returns a romantic reply like:

```json
{
  "user_message": "hello",
  "bot_reply": "Hey there, sweetheart! How's your day going? ☺️"
}
```

---

### 🔐 File Structure

```
.
├── bot.py              # Main bot logic
├── .env                # Secrets (not committed)
├── requirements.txt    # Dependencies
└── README.md           # You're here
```

---

### 🧪 Example

```
User: hi  
Bot: Hi, love! I missed you. What are you up to? ❤️
```

---

### ❌ Ignores:

* Messages from other bots
* Command messages like `/start`, `/help` are handled separately

---

### 📌 Credits

* API hosted by [@AashooSharma](https://github.com/AashooSharma)
* Built using [Telethon](https://github.com/LonamiWebs/Telethon)

---

### 🚀 Coming Soon

* OpenAI GPT fallback
* Voice message to text
* Memory/log of user chats
* Web dashboard to update replies

---

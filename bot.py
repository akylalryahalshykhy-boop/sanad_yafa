from pyrogram import Client
import config

app = Client(
    "Sanad_Yafa_Bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="handlers") # يخبر البوت أن الأوامر موجودة في مجلد handlers
)

print("سناد يافا يعمل الآن..")
app.run()

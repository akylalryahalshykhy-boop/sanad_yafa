from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config

app = Client(
    "Sanad_Yafa_Bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# معرف القناة (بدون الرابط، فقط الاسم بعد @)
CHANNEL_USERNAME = "@Yaffa_Digital_World" 

@app.on_message(filters.command("start"))
async def start(client, message):
    try:
        # فحص هل المستخدم مشترك في القناة
        member = await client.get_chat_member(CHANNEL_USERNAME, message.from_user.id)
        
        # إذا كان مشتركاً، رحب به
        await message.reply_text("أهلاً بك في بوت عالم يافا | YAFFA World!\nالبوت يعمل الآن بنجاح.")
        
    except:
        # إذا لم يكن مشتركاً، أرسل زر الاشتراك
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("اشترك في عالم يافا 📢", url="https://t.me/Yaffa_Digital_World")]
        ])
        await message.reply_text("عذراً، يجب عليك الاشتراك في قناة عالم يافا لاستخدام البوت:", reply_markup=keyboard)

print("البوت يعمل الآن مع حماية الاشتراك..")
app.run()

from telegram.ext import ApplicationBuilder, MessageHandler, filters

from config import settings
from bot import handlers



app = ApplicationBuilder().token(settings.BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.text_handler))
app.add_handler(MessageHandler(filters.VOICE, handlers.voice_handler))

app.run_polling()
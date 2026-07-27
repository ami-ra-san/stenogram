from telegram import Update, Voice
from telegram.ext import ContextTypes


async def voice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    voice_message: Voice = update.message.voice
    voice_file = await voice_message.get_file()
    await voice_file.download_to_drive(f'temp/{voice_file.file_unique_id}.ogg')

    print(f'{voice_message.duration}\n{voice_message.file_size}\n{voice_message.mime_type}')

    await update.message.reply_text(f'Saved as {voice_file.file_unique_id}.ogg')



async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("I'm blind. Send me voices.")

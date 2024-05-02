from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler
from food_recognition.recognition import FoodRecognition

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_id = update.message.photo[-1].file_id
    new_file = await context.bot.get_file(file_id)

    PATH = "assets/images/photo.jpg"

    file_d = await new_file.download_to_drive(PATH)

    food_name = model.eval(PATH)[0]
    

    await update.message.reply_text(food_name)

model = FoodRecognition()

def main():

    token = "token"

    app = ApplicationBuilder().token(token).build()

    app.add_handler(MessageHandler(filters.PHOTO, handle_image))

    app.run_polling()

if __name__ == "__main__":
    main()
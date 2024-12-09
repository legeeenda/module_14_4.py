from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import initiate_db, get_all_products
import asyncio

API_TOKEN = '7787493433:AAGBdEiUhUvCcydfXXxFbbS_F_T_Ca5Tfbk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Рассчитать"), KeyboardButton(text="Информация")],
        [KeyboardButton(text="Купить")]
    ],
    resize_keyboard=True
)


inline_product_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Купить", callback_data="product_buying")]
    ]
)

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=keyboard)

@dp.message(lambda message: message.text == "Купить")
async def get_buying_list(message: types.Message):

    products = get_all_products()
    
    if not products:
        await message.answer("В базе данных нет продуктов.")
        return
    

    for product in products:
        product_id, title, description, price, image_url = product
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=image_url,
            caption=f"Название: {title} | Описание: {description} | Цена: {price} рублей."
        )
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_product_keyboard)


@dp.callback_query(lambda call: call.data == "product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")

async def main():

    initiate_db()
    
    print("Bot is running...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

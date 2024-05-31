from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keboard.keyboards import get_keyboard_1, get_keyboard_2
from keboard.key_inline import get_keyboard_inline
from database.database import initialize_db, add_user, get_user

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_db()

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description= 'Команда для того чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того чтобы ПОМОГИТЕ'),
        types.BotCommand(command='/dont_help', description='Команда для того чтобы НЕ ПОМОГИТЕ'),
        types.BotCommand(command='/say_gex', description='Команда для того чтобы SAY GEX'),
        types.BotCommand(command='/sesbian_lex', description='Команда для того чтобы SESBIAN LEX')
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username,message.from_user.last_name, message.from_user.last_name)
        await message.answer('SESBIAN LEX', reply_markup=get_keyboard_1())
    else:
        await message.answer('SESBIAN LEX', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'ОТПРАВЬ ФОТО ТОКАРНОГО СТАНКА OPTIturn TU 2304')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://blog.florianuhlemann.de/wp-content/uploads/2015/04/DSC_0002.jpg', caption= 'НЫА НЫА ДЕРЖИ НЫА НЫА👊👊👊', reply_markup= get_keyboard_inline())

@dp.message_handler(lambda message: message.text == 'УЙТИ К ДРУГОЙ КЛАВЕ(НЕ УХОДИ ПРОШУ ПРОШУ ПРОШУ🙏🙏🙏🙏')
async def button_2_click(message: types.Message):
    await message.answer('НУ ЛАДНО', reply_markup=get_keyboard_2())


@dp.message_handler(lambda message: message.text == 'ОТПРАВЬ МНЕ ФОТО ИГОРЯ')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://cstor.nn2.ru/forum/data/forum/images/2023-12/262607362-izobrazenie_2023-12-07_000017775.png', caption= 'НЫА НЫА ДЕРЖИ НЫА НЫА👊👊👊')


@dp.message_handler(lambda message: message.text == 'ВЕРНУТЬСЯ К ПРОШЛОЙ КЛАВЕ(УХОДИ ПРОШУ ПРОШУ ПРОШУ🙏🙏🙏🙏')
async def button_4_click(message: types.Message):
    await message.answer('НУ ЛАДНО', reply_markup=get_keyboard_1())


@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('let him cook🗣️🗣️🗣️🔥🔥🔥')

@dp.message_handler(commands= 'dont help')
async def dont_help(message: types.Message):
    await message.reply('AAAAH HELL️🔥🔥🔥')

@dp.message_handler(commands= 'say gex')
async def say_gex(message: types.Message):
    await message.reply('SAY GEX')

@dp.message_handler(commands= 'sesbian lex')
async def sesbian_lex(message: types.Message):
    await message.reply('SESBIAN LEX')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
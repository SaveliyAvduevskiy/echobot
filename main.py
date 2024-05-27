from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

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
    await message.answer('SESBIAN LEX')

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
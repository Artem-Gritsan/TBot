from aiogram import types, Dispatcher
from create_bot import dp
from keyboards import keyboards_menu
from  aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import wikipedia, re


wikipedia.set_lang('ru')

class FSMWiki(StatesGroup):
    word = State()


async def wiki_command(message: types.Message):
    await  FSMWiki.word.set()
    await message.answer('Отправьте мне любое слово, и я найду его значение на Wikipedia')


async def wiki_cansel(message:types.Message, state:FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Ок', reply_markup=keyboards_menu.main_menu)


async def word(message: types.Message):
    try:
        ny = wikipedia.page(message.text)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        await message.answer(wikitext2, reply_markup=keyboards_menu.back_menu)
    except Exception as e:
        await message.answer('В энциклопедии нет информации об этом', reply_markup=keyboards_menu.back_menu)



def register_handler_wiki(dp: Dispatcher):
    dp.register_message_handler(wiki_command, commands='Wikipedia', state=None)
    dp.register_message_handler(wiki_command, Text(equals='Википедия', ignore_case=True), state=None)
    dp.register_message_handler(wiki_cansel, commands='back', state="*")
    dp.register_message_handler(wiki_cansel, Text(equals='Назад', ignore_case=True), state="*")
    dp.register_message_handler(word, state=FSMWiki.word)





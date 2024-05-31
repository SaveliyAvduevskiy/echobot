from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть',url='https://mir-stankov.ru/catalog/tokarnye_stanki_po_metallu/?utm_source=yandex&utm_medium=cpc&utm_campaign=mir_stankov_tokarnye_tgo_search&utm_content=SRC:none_SRCT:search_CAMP:98572676_GR:5311326914_B:15206359577_KW:%D1%82%D0%BE%D0%BA%D0%B0%D1%80%D0%BD%D1%8B%D0%B9%20%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%BA_KWID:47899526775_RE:47899526775&utm_geo=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&utm_term=%D1%82%D0%BE%D0%BA%D0%B0%D1%80%D0%BD%D1%8B%D0%B9%20%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%BA&yclid=13418322763469291519')
    but_inline2 = InlineKeyboardButton('Посмотреть',url='https://www.vekpro.ru/catalog/mekhanicheskaya-obrabotka-metalla/tokarnye-stanki/nastolnye-tokarnye-stanki/nastolnjy-tokarniy-optiturn-tu-2506v/')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline
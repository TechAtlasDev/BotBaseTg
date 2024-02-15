from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from moduls.utils import utils

def keymakers(list_text:str, list_postdata:str):
    buttons = InlineKeyboardMarkup([[InlineKeyboardButton(str(text), callback_data=str(postdata)) for text, postdata in zip(list_text, list_postdata)]])
    return buttons
# -*- coding: utf-8 -*-

import telebot
from telebot import types
token = "543978938:AAGeQZlSkbHZ1BfkWFSkVp_eaA1Mx8RzJqg"
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на наш сайт", url="https://fishgoldrezerv.ru/")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Хочешь рыбку?", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="ю")
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="!")
    elif call.inline_message_id:
        if call.data == "test":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="?")


@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="test"))
    results = []
    single_msg = types.InlineQueryResultArticle(
        id="1", title="Press me",
        input_message_content=types.InputTextMessageContent(message_text="Я"),
        reply_markup=kb
    )
    results.append(single_msg)
    bot.answer_inline_query(query.id, results)


if __name__ == '__main__':
    bot.polling(none_stop=True)

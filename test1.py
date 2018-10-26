import telebot
token = "656849369:AAFdYukcDyzriNbZIHOIwCgWdikUByrFaDQ"
bot = telebot.TeleBot(token)
#bot.send_message(205830986, "425345")

def log(message, answer):
    print("_________________")
    from datetime import datetime
    print(datetime.now())
    print ("Сообщение от {0} {1}. (id = {2}\n Text - {3}" . format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)


@bot.message_handler(commands=['start'])
def handle_text(message):


    bot.send_message(message.chat.id,
                     "Здаров.")
    bot.send_message(message.chat.id,
                     "Я Петягов.")
    bot.send_message(message.chat.id,
                     " Мой IQ-122. Одной рукой я могу собрать головоломку, другой выбиваю 999 в автоматы.")
    bot.send_message(message.chat.id,
                     "Короче, я ахуенен.")
    bot.send_message(message.chat.id,
                     "А ты ахуенен как я? Проверим?")
    bot.send_message(message.chat.id,
                     "Слабо пройти мой Петяговский тест?")
    bot.send_message(message.chat.id,
                     "Если да, то вот тебе первый вопрос.")
    bot.send_message(message.chat.id,
                     "Для чего необходимо идти на пенсионный митинг 9 сентября?")
    bot.send_message(message.chat.id,
                     "1. Потому что Урепление народовластия и осознание идентичности.")
    bot.send_message(message.chat.id,
                     "2. Потому что Путин вор.")
    bot.send_message(message.chat.id,
                     "3. Потому что иди нах.")
    log(message, answer)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Твой IQ слишком слабый, попробуй еще раз, когда поумнеешь."
    if message.text == "1":
        bot.send_message(message.chat.id, "А ты шаришь. Тогда следующий вопрос.")
        bot.send_message(message.chat.id, "Навальный няша? да или нет?")
        answer = "111"
        log(message, answer)
    elif message.text == "2":
        bot.send_message(message.chat.id, "Навльный, ты что ли? Уди... Иди видео снимай.")
        answer = "222"
        log(message, answer)
    elif message.text == "3":
        bot.send_message(message.chat.id, "Сам иди.")
        answer = "222"
        log(message, answer)
    elif message.text == "да":
        bot.send_message(message.chat.id, "Конечно он няша. Ты прав.")
        bot.send_message(message.chat.id, "а ну ка... Тест на память. Мой iq 120, 122 или 120,2?")
        answer = "222"
        log(message, answer)
    elif message.text == "нет":
        bot.send_message(message.chat.id, "Ты чо. Он же няшка! Уди Путинский ватник.")
        answer = "222"
        log(message, answer)
    elif message.text == "122":
        bot.send_message(message.chat.id, "Ты прошел этот тест. Я нарекаю тебя Петяговым. Неси этот титул достойно!")
        log(message, answer)
    elif message.text == "120":
        bot.send_message(message.chat.id, "Иди память лечи!")
        log(message, answer)
    elif message.text == "120,2":
        bot.send_message(message.chat.id, "Иди память лечи!")
        log(message, answer)
    else:
            bot.send_message(message.chat.id, answer)




bot.polling(none_stop=True, interval=0)
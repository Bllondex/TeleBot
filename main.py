import telebot
from telebot import types
import time
import config

bot = telebot.TeleBot(config.TOKEN)

timeSmoke = 2400
cigaretteCounter = 0
#Создаём команду старт
@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    answerYes = types.InlineKeyboardButton('Да давай начнём!')
    answerNo = types.InlineKeyboardButton('Нет, не в этот раз')
    markup.add(answerNo, answerYes)
    mess = "Привет, " + message.from_user.first_name + ", я SmokBot и я помогу тебе бросить курить! Давай начнём?"
    bot.send_message(message.chat.id, mess, reply_markup=markup)
# ОТКАЗ от начала эксперемента
@bot.message_handler(regexp = "Нет, не в этот раз")
def get_user_test(message):
    markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    Button_start = types.KeyboardButton('/start')
    markup_1.add(Button_start)
    bot.send_message(message.chat.id, "Как скажешь, если вдруг решишся на этот шаг пиши /start и мы попробуем ещё раз!", reply_markup=markup_1)
#Принятие на начало эксперимента и постановка таймеров
@bot.message_handler(regexp="Да давай начнём!")
def get_user_test(message):
    markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    timesmoking_1 = types.KeyboardButton('40 минут')
    timesmoking_2 = types.KeyboardButton('1 час')
    timesmoking_3 = types.KeyboardButton('1.5 часа')
    timesmoking_4 = types.KeyboardButton('2 часа')
    timesmoking_5 = types.KeyboardButton('2.5 часа')
    timesmoking_6 = types.KeyboardButton('3 часа')
    timesmoking_7 = types.KeyboardButton('3.5 часа')
    timesmoking_8 = types.KeyboardButton('4 часа')
    timesmoking_9 = types.KeyboardButton('5 часов')
    markup_1.add(timesmoking_1,timesmoking_2,timesmoking_3,timesmoking_4,timesmoking_5,timesmoking_6,timesmoking_7,timesmoking_8,timesmoking_9)
    bot.send_message(message.chat.id, "Прекрасно! Давай определимся через какой промежуток времени ты будешь курить? Начинай с небольшого промежутка и повышай его как будешь готов!  ", reply_markup=markup_1)
#Человек покурил прибавился счётчик сигарет и запустился таймер
@bot.message_handler(regexp="Покурить")
def get_user_test(message):
    markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    Button_smoke = types.KeyboardButton('Покурить')
    Button_smokeAndSleep = types.KeyboardButton('Последний покур перед сном')
    Button_amountSigar = types.KeyboardButton('Сколько сигарет выкурено за сегодня')
    Button_changeTime = types.KeyboardButton('Изменить время без сигарет')
    markup_1.add(Button_smoke, Button_smokeAndSleep, Button_amountSigar, Button_changeTime)
    bot.send_message(message.chat.id, f"Приятного мой друг, я тебе сообщу когда снова можно будет покурить, а именно через {timeSmoke // 60} минут")
    global cigaretteCounter
    cigaretteCounter = cigaretteCounter + 1
    time.sleep(timeSmoke)
    bot.send_message(message.chat.id, "Перекур вновь доступен!", reply_markup=markup_1)
#То же что и Перекур, но без таймера, показывает кол во сигарет за день
@bot.message_handler(regexp="Последний покур перед сном")
def get_user_test(message):
    markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    Button_smoke = types.KeyboardButton('Покурить')
    Button_smokeAndSleep = types.KeyboardButton('Последний покур перед сном')
    Button_amountSigar = types.KeyboardButton('Сколько сигарет выкурено за сегодня')
    Button_changeTime = types.KeyboardButton('Изменить время без сигарет')
    markup_1.add(Button_smoke, Button_smokeAndSleep, Button_amountSigar, Button_changeTime)
    global cigaretteCounter
    bot.send_message(message.chat.id, f"За весь день ты выкурил {cigaretteCounter} сигарет, неплохо!", reply_markup=markup_1)
    cigaretteCounter = 0
    bot.send_message(message.chat.id, "Спокойной ночи, мой друг", reply_markup=markup_1)
#Показывает кол во выкуреных сигарет за день
@bot.message_handler(regexp="Сколько сигарет выкурено за сегодня")
def get_user_test(message):
    markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    Button_smoke = types.KeyboardButton('Покурить')
    Button_smokeAndSleep = types.KeyboardButton('Последний покур перед сном')
    Button_amountSigar = types.KeyboardButton('Сколько сигарет выкурено за сегодня')
    Button_changeTime = types.KeyboardButton('Изменить время без сигарет')
    markup_1.add(Button_smoke, Button_smokeAndSleep, Button_amountSigar, Button_changeTime)
    bot.send_message(message.chat.id, f"За сегодня ты выкурил всего ничего {cigaretteCounter} сигарет", reply_markup=markup_1)
#Изменение таймера
@bot.message_handler(regexp="Изменить время без сигарет")
def get_user_test(message):
    markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    timesmoking_1 = types.KeyboardButton('40 минут')
    timesmoking_2 = types.KeyboardButton('1 час')
    timesmoking_3 = types.KeyboardButton('1.5 часа')
    timesmoking_4 = types.KeyboardButton('2 часа')
    timesmoking_5 = types.KeyboardButton('2.5 часа')
    timesmoking_6 = types.KeyboardButton('3 часа')
    timesmoking_7 = types.KeyboardButton('3.5 часа')
    timesmoking_8 = types.KeyboardButton('4 часа')
    timesmoking_9 = types.KeyboardButton('5 часов')
    markup_1.add(timesmoking_1, timesmoking_2, timesmoking_3, timesmoking_4, timesmoking_5, timesmoking_6, timesmoking_7, timesmoking_8, timesmoking_9)
    bot.send_message(message.chat.id, "Какое время поставить на этот раз?", reply_markup=markup_1)
# Принимает и изменяет таймеры и прочие команды
@bot.message_handler()
def rekTime(message):
    markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    Button_smoke = types.KeyboardButton('Покурить')
    Button_smokeAndSleep = types.KeyboardButton('Последний покур перед сном')
    Button_amountSigar = types.KeyboardButton('Сколько сигарет выкурено за сегодня')
    Button_changeTime = types.KeyboardButton('Изменить время без сигарет')
    markup_1.add(Button_smoke, Button_smokeAndSleep, Button_amountSigar, Button_changeTime)
    if message.text == "40 минут":
        bot.send_message(message.chat.id, "Промежуток между перекурами теперь 40 минут")
        global timeSmoke
        timeSmoke = 2400
        bot.send_message(message.chat.id, "Отлично! Давай же начнём, как покуришь дай мне знать", reply_markup=markup_1)
    elif message.text == "1 час":
        bot.send_message(message.chat.id, "Промежуток между перекурами теперь 1 час")

        timeSmoke = 3600
        bot.send_message(message.chat.id, "Отлично! Давай же начнём, как покуришь дай мне знать", reply_markup=markup_1)
    elif message.text == "1.5 часа":
        bot.send_message(message.chat.id, "Промежуток между перекурами теперь 1.5 часа")
        timeSmoke = 5400
        bot.send_message(message.chat.id, "Отлично! Давай же начнём, как покуришь дай мне знать", reply_markup=markup_1)
    elif message.text == "2 часа":
        bot.send_message(message.chat.id, "Промежуток между перекурами теперь 2 часа")
        timeSmoke = 7200
        bot.send_message(message.chat.id, "Отлично! Давай же начнём, как покуришь дай мне знать", reply_markup=markup_1)
    elif message.text == "2.5 часа":
        bot.send_message(message.chat.id, "Промежуток между перекурами теперь 2.5 часа")
        timeSmoke = 9000
        bot.send_message(message.chat.id, "Отлично! Давай же начнём, как покуришь дай мне знать", reply_markup=markup_1)
    elif message.text == "3 часа":
        bot.send_message(message.chat.id, "Промежуток между перекурами теперь 3 часа")
        timeSmoke = 10800
        bot.send_message(message.chat.id, "Отлично! Давай же начнём, как покуришь дай мне знать", reply_markup=markup_1)
    elif message.text == "3.5 часа":
        bot.send_message(message.chat.id, "Промежуток между перекурами теперь 3.5 час")
        timeSmoke = 12600
        bot.send_message(message.chat.id, "Отлично! Давай же начнём, как покуришь дай мне знать", reply_markup=markup_1)
    elif message.text == "4 часа":
        bot.send_message(message.chat.id, "Промежуток между перекурами теперь 4 часа")
        timeSmoke = 14400
        bot.send_message(message.chat.id, "Отлично! Давай же начнём, как покуришь дай мне знать", reply_markup=markup_1)
    elif message.text == "5 часов":
        bot.send_message(message.chat.id, "Промежуток между перекурами теперь 5 часов")
        timeSmoke = 18000
        bot.send_message(message.chat.id, "Отлично! Давай же начнём, как покуришь дай мне знать", reply_markup=markup_1)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю")
bot.polling(none_stop = True)






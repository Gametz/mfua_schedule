# -*- coding: utf-8 -*-
import telebot
import json
import datetime

weekcolor = 0

bot = telebot.TeleBot("2086370566:AAGijx-i2CsJOE751UDXvHFLCqq3sPSdmj0")


def writejson():
    x = {"white": ["*Понедельник | Белая*\n\n"
                   "1 пара - 9:00-10:30 | 6.7 Иностранный язык\n"
                   "2 пара - 10:40-12:10 | 6.7 Иностранный язык\n"
                   "3 пара - 12:40-14:10 | 11.52 Технологиия разработки и защиты баз данных\n"
                   "4 пара - 14:40-16:10 | 11.52 Инфрокоммуникационные системы и сети\n"
                   "5 пара - 16:20-17:50 | 11.52 Инфрокоммуникационные системы и сети\n",

                   "\n*Вторник | Белая* | Teams\n\n"
                   "5 пара - 16:20-17:50 | Информационные технологии\n"
                   "6 пара - 18:00-19:30 | Информационные технологии\n",

                   "\n*Среда | Белая*\n\n"
                   "1 пара - 9:00-10:30 | 9.11 Информационные технологии\n"
                   "2 пара - 10:40-12:10 | 11.52 Технологиия разработы и защиты баз данных\n"
                   "3 пара - 12:40-14:10 | Физическая культура\n"
                   "4 пара - 14:40-16:10 | 10.47 Технические средства информации\n",

                   "\n*Четверг | Белая* | Teams\n\n"
                   "4 пара - 14:40-16:10 | Инфрокоммуникационные системы и сети\n"
                   "5 пара - 16:20-17:50 | Технологиия разработы и защиты баз данных\n"
                   "6 пара - 18:00-19:30 | Выполнение работ по профессии\n",

                   "\n*Пятница | Белая*\n\n"
                   "2 пара - 10:40-12:10 | 9.6 Выполнение работ по профессии\n"
                   "3 пара - 12:40-14:10 | 9.6 Выполнение работ по профессии\n"
                   "4 пара - 14:40-16:10 | 9.10 Технические средства информации\n"
                   "5 пара - 16:20-17:50 | 9.10 Технические средства информации\n"],

         "green": ["*Понедельник | Зеленая*\n\n"
                   "3 пара - 12:40-14:10 | 11.52 Технологиия разработы и защиты баз данных\n"
                   "4 пара - 14:40-16:10 | 11.52 Инфрокоммуникационные системы и сети\n"
                   "5 пара - 16:20-17:50 | 11.52 Инфрокоммуникационные системы и сети\n",

                   "\n*Вторник | Зеленая* | Teams\n\n"
                   "5 пара - 16:20-17:50 | Информационные технологии\n"
                   "6 пара - 18:00-19:30 | Информационные технологии\n",

                   "\n*Среда | Зеленая*\n\n"
                   "1 пара - 9:00-10:30 | 9.11 Информационные технологии\n"
                   "2 пара - 10:40-12:10 | 11.52 Технологиия разработы и защиты баз данных\n"
                   "4 пара - 14:40-16:10 | 11.52 Инфрокоммуникационные системы и сети\n"
                   "5 пара - 16:20-17:50 | Физическая культура\n",

                   "\n*Четверг | Зеленая* | Teams\n\n"
                   "4 пара - 14:40-16:10 | Инфрокоммуникационные системы и сети\n"
                   "5 пара - 16:20-17:50 | Технологиия разработы и защиты баз данных\n"
                   "6 пара - 18:00-19:30 | Выполнение раьот по профессии\n",

                   "\n*Пятница | Зеленая*\n\n"
                   "2 пара - 10:40-12:10 | 9.6 Выполнение раьот по профессии\n"
                   "3 пара - 12:40-14:10 | 9.6 Выполнение раьот по профессии\n"
                   "4 пара - 14:40-16:10 | 9.10 Технические средства информации\n"
                   "5 пара - 16:20-17:50 | 9.10 Технические средства информации\n"]}

    with open('schedule.json', 'w') as f:
        f.write(json.dumps(x))
        return


@bot.message_handler(commands=['changeweek'])
def cng_week(message):
    global weekcolor
    if message.from_user.id == 627782619 or message.from_user.id == 895100929:
        if weekcolor == 1:
            weekcolor = 0
        else:
            weekcolor = 1
        if weekcolor == 1:
            wc = "зелёную"
        else:
            wc = "белую"
        bot.send_message(message.chat.id, f"Неделя успешна сменена на {wc}", parse_mode='Markdown')


@bot.message_handler(commands=['start'])
def hi_msg(message):
    bot.send_message(message.chat.id,
                     f"*{message.from_user.first_name}*, Добро пожаловать в бота для просмотра расписания\n\n/help "
                     f"для просмотра команд",
                     parse_mode='Markdown')


@bot.message_handler(commands=['help'])
def help_msg(message):
    helpmsg = "/help - отобразить это сообщение\n" \
              "/white - расписание на белую неделю\n" \
              "/green - расписание на зелёную неделю\n" \
              "/today - расписание на сегодня\n" \
              "/tomorrow - расписание на завтра"
    bot.send_message(message.chat.id, f"{helpmsg}", parse_mode='Markdown')


def white():
    with open('schedule.json') as f:
        ff = json.loads(f.read())
        return '========================='.join(ff["white"])


def green():
    with open('schedule.json') as f:
        ff = json.loads(f.read())
        return '========================='.join(ff["green"])


@bot.message_handler(commands=['white'])
def whiterasp(message):
    f = white()
    bot.send_message(message.chat.id, f, parse_mode='Markdown')


@bot.message_handler(commands=['green'])
def greenrasp(message):
    f = green()
    bot.send_message(message.chat.id, f, parse_mode='Markdown')


@bot.message_handler(commands=['today'])
def today(message):
    with open('schedule.json') as f:
        ff = json.loads(f.read())

    d = (datetime.date.today()).strftime('%d.%m')
    w = datetime.datetime.today().isoweekday()
    if w == 6 or w == 7:
        f = f"*Сегодня выходной!*"
    else:
        if weekcolor == 0:
            f = ff["white"][w - 1]
        else:
            f = ff["green"][w - 1]
    bot.send_message(message.chat.id, f"*Расписание на сегодня ({d}):*\n\n{f}", parse_mode='Markdown')


@bot.message_handler(commands=['tomorrow'])
def today(message):
    with open('schedule.json') as f:
        ff = json.loads(f.read())
    d = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d.%m')
    w = datetime.datetime.today().isoweekday()
    try:
        if w == 7:
            if weekcolor == 0:
                f = ff["white"][0]
            else:
                f = ff["green"][0]
        else:
            if weekcolor == 0:
                f = ff["white"][w + 1]
            else:
                f = ff["green"][w + 1]
    except:
        f = f"*Завтра выходной!*"
    bot.send_message(message.chat.id, f"*Расписание на завтра ({d}):*\n\n{f}", parse_mode='Markdown')


if __name__ == '__main__':
    print("Bot started\n")
    bot.infinity_polling()

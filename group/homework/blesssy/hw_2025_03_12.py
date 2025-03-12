import telebot
import schedule
import time
import threading
from datetime import datetime
import locale
from pytz import timezone

# Установка часового пояса
moscow_tz = timezone('Europe/Moscow')

# Токен бота
TOKEN = "7846915608:AAF6_J_TyAHN3gipvktD8S-3NCudZIzYUqE"
bot = telebot.TeleBot(TOKEN)

# ID чата и темы
chat_id = "-1002127365711"
topic_id = 3091  

# Варианты ответа в опросе
options = [
    "я молодец (в вузе)",
    "скип (ув - в лс)",
    "скип (неув)",
    "приду не к первой (в лс)"
]

def send_poll_in_topic(topic_id):
    """Отправка опроса в нужную тему"""
    current_date = (f'{datetime.now():%d %B %Y}')  # Текущая дата
    poll_title = f"{current_date}"  # Заголовок опроса
    
    bot.send_poll(chat_id, poll_title, options, is_anonymous=False, message_thread_id=topic_id)

def send_poll():
    """Функция для отправки опроса"""
    # Устанавка локализации на ру
    locale.setlocale(locale.LC_TIME, 'ru_RU')

    # Заголовок для опроса (дата)
    current_date = datetime.now().strftime('%d %B')
    poll_title = f"{current_date}"

    # Отправляем сообщение с опросом
    bot.send_message(chat_id, "*тык в опросе*", message_thread_id=topic_id, parse_mode="Markdown")

    # Отправляем опрос в тему группы
    bot.send_poll(chat_id, poll_title, options, is_anonymous=False, message_thread_id=topic_id)

def job():
    """Запуск задачи каждый день, кроме среды и воскресенья"""
    now = datetime.now(moscow_tz)
    if now.weekday() not in (2, 6):  # Проверка на ср\вскр
        send_poll()

@bot.message_handler(commands=['poll'])

def manual_poll(message):
    """Команда для ручного вызова опроса"""
    if hasattr(message, 'message_thread_id') and message.message_thread_id: # проверка на тему, в которой вызван бот
        send_poll_in_topic(message.message_thread_id)
        if message.reply_to_message:
            bot.reply_to(message, "Тык в опросе")  # Текст ответа на команду
        else:
            bot.send_message(message.chat.id, "Тык в опросе")  # Если нет сообщения-команды
    else:
        bot.reply_to(message, 'Эту команду нужно отправлять в тему "Учёт посещаемости"!')

# Планируем отправку
schedule.every().day.at("12:00").do(job)

def schedule_checker():
    """Запуск `schedule` в отдельном потоке"""
    while True:
        schedule.run_pending()
        time.sleep(60)  # Проверяет задачи каждую минуту

# Запуск бота с учётом возможной остановки кода
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as error:
        print(f"Ошибка: {error}. Перезапуск...")
        time.sleep(5)

# Запуск планировщика в фоновом потоке
threading.Thread(target=schedule_checker, daemon=True).start()

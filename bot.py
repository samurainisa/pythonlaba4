
#подключение библиотеки телеграм
import telebot
#логгируем токен и используем библиотеку через нашу переменную, например а
a = telebot.TeleBot("5034505520:AAFRY-k0rwylohiq1IkkcpE2JTjSo10E4Wg")
#делается своего рода флажок для использования в дальнейшем
keyboard_test = telebot.types.ReplyKeyboardMarkup(True)
#Прописываем кнопки в строчку
keyboard_test.row("Java", "Kotlin", "JavaEE")
#простыми словами, если бот перехватил команду /start, то начинает запускать функцию, которая следует после декоратора (@) в этой же функции мы можем как-по своему обработать ответ бота на сообщение пользователя

@a.message_handler(commands=['start'])
def startWork(message):
  #в этом пример tid = айди сообщения, параметр, который следует использовать в сигнатуре функции send_message, если надо отправить под именем бота сообщение пользователю
  tid = message.chat.id
  #отправка пользователю сообщение, два параметра = айди, текст и параметр reply_markup для установки клавиатуры на этом этапе
  a.send_message(tid, "start work!", reply_markup = keyboard_test)
#простыми словами, если бот перехватил команду любой текст, который отправил пользователь боту, то начинает запускать функцию, которая следует после декоратора (@) в этой же функции мы можем как-по своему обработать ответ бота на сообщение пользователя
@a.message_handler(content_types=['text'])
def sendYourMessage(message):
  mid = message.chat.id
  #если пользователь написал Привет, то бот ответ в соответвии с тем, что ему предписано
  if message.text == "Java":
    a.send_message(mid, "Информация о Java")
    a.send_message(mid, "https://metanit.com/java/tutorial/")
    a.send_message(mid, "https://www.java.com/ru/")
  elif message.text =="Kotlin":
    a.send_message(mid, "Информация о Kotlin")
    a.send_message(mid, "https://metanit.com/kotlin/tutorial/")
    a.send_message(mid, "https://kotlinlang.org/")
  elif message.text =="JavaEE":
    a.send_message(mid, "Информация о JavaEE")
    a.send_message(mid, "https://metanit.com/java/javaee/1.1.php")
    a.send_message(mid, "https://javarush.ru/groups/posts/2637-vvedenie-v-java-ee")
  else:
  #если пользователь написал сообщение, которое у бота никак выше не обрабатывается
    a.send_message(mid, "Не понимаю тебя что ты хочеш")
#polling нужен для того, чтобы бот не переставал перехватывать сообщения, работал в режиме ожидания от пользователя действий
a.polling()
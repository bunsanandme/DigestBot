import telebot
import digest
import pickle

bot = telebot.TeleBot('1582208841:AAHHiRepm69az6FjbqVv48Yp3q0AGIALVSw')


@bot.message_handler(commands=['view'])
def view_post_message(message):
    view = digest.view_posts()
    bot.send_message(message.chat.id,
                     "*Постов по вашим хабам: {}".format(len(view)) + '*\n' + "\n".join(view), parse_mode="Markdown")
    digest.clear_posts()


@bot.message_handler(commands=['hubs'])
def view_hubs(message):
    hubs = digest.view_hubs()
    if hubs == "Error!" or hubs.__len__() == 0:
        bot.send_message(message.chat.id, "У вас пока нет отслеживаемых хабов. Самое время их добавить!")
    else:
        bot.send_message(message.chat.id, "Ваши хабы: " + '\n' + "\n".join(hubs))


@bot.message_handler(commands=['add_hub'])
def adding(message):
    m = message.text
    hub = str(m[9:])
    digest.add_hubs(hub)
    bot.send_message(message.chat.id, 'Хаб {} добавлен в отслеживаемые!'.format("*"+hub+"*"), parse_mode="Markdown")


@bot.message_handler(commands=['delete_hub'])
def deleting(message):
    m = message.text
    hub = str(m[12:])
    hubs = digest.delete_hub(hub)
    if hubs == "Error!":
        bot.send_message(message.chat.id, "Такого хаба нет в отслеживаемых")
    else:
        bot.send_message(message.chat.id, 'Хаб {} удален из отслеживаемых!'.format("*"+hub+"*"), parse_mode="Markdown")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, это ДайджестБот! Посмотрим, что есть номого?')


bot.polling()

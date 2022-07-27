import telebot
from config import currency_map, TOKEN
from extentions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите комманду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\n\
Увидеть список всех доступных валют - /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for currency in currency_map.keys():
        text = '\n'.join((text, currency, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException('Неверное количество параметров. ')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
        if total_base is None:
            raise APIException('В данный момент не существует курса для данных валют')
    except APIException as e:
        bot.reply_to(message, f'Ошибка ввода\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()


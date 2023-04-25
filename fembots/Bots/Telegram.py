

import typing
import os
import telebot

from .Bot import Bot

bot = telebot.TeleBot("6231441217:AAFEroDDtxUjmuh-IWwcKD2OZ2neaxFX6pI")


class Telegram(Bot):
    """A bot to communicate over telegram"""

    name = "telegram"

    def __init__(self, config: typing.Dict[str, str]) -> None:
        super().__init__(config)

    @bot.message_handler(func=lambda msg: True)
    def echo_all(message):
        """Sends a reply to the user who sent the message"""
        bot.reply_to(message, message)
    def start(self):
        
        try:
            bot.polling()
            return True
        except:
            return False

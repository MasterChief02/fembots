import typing

import telebot

from .Bot import Bot


class Telegram(Bot):
    """A bot to communicate over telegram"""

    name = "telegram"

    def __init__(self, config: typing.Dict[str, str]) -> None:
        super().__init__(config)

        self.api_key = config.get("API_KEY", "")
        self.bot = telebot.TeleBot(self.api_key)

        @self.bot.message_handler(func=lambda m: True)
        def respond_NLP_engine(self, message):
            self.bot.reply_to(message, message.text)

    def start(self):
        self.bot.infinity_polling()

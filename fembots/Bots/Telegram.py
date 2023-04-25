import typing

import telebot

from .Bot import Bot


class Telegram(Bot):
    """A bot to communicate over telegram"""

    name = "telegram"

    def __init__(self, config: typing.Dict[str, str]) -> None:
        super().__init__(config)

        self.api_key = config.get("API_KEY", "")
        self.command = config.get("command", "")
        self.bot = telebot.TeleBot(self.api_key)

    def start(self):
        try:
            start_dict = dict(
                function=lambda msg, obj=self: obj.start_handler(msg),
                filters=dict(commands=[self.command]),
            )
            self.bot.add_message_handler(start_dict)
            self.bot.infinity_polling()
            return True

        except:
            return False

    def start_handler(self, message):
        response = self.get_response_from_NLP(message.text)
        print(response)
        self.bot.reply_to(message, response)

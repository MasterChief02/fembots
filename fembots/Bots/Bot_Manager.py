import typing

import configparser

from .Bot import Bot
from .Telegram import Telegram


class Bot_Manager:
    """A class to manage all possible bots."""

    # List of available bots.
    # Add your custom bot here.
    available_bots: typing.List[typing.Any] = [
        Telegram,
    ]

    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.bots: typing.List[Bot] = list()

        # Loading configurations
        self.config.read("fembots/bot.ini")

        # Set API endpoint for NLP engine
        Bot.api_endpoint = self.config["DEFAULT"].get("api_endpoint", "127.0.0.1")

        # Initializing bots
        for bot in Bot_Manager.available_bots:
            config_attr = f"enable_{bot.name}_bot"
            use_bot = self.config["DEFAULT"].get(config_attr, "no")

            if use_bot == "yes":
                print("Telegram")
                bot_config_attr = bot.name.upper()
                config = self.config[bot_config_attr]
                _bot = bot(config)
                self.bots.append(_bot)

    def start(self) -> bool:
        """
        Function to start the all the bots enabled.

        Parameters
        ----------
        None

        Return
        ------
        bool: Returns true if started successfully, false otherwise.
        """
        try:
            for _bot in self.bots:
                _bot.start()
            return True
        except:
            return False

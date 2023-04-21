import typing

import configparser
import os

from .Bot import Bot
from .Telegram import Telegram


class Bot_Manager:
    """A class to manage all possible bots."""

    # List of available bots.
    # Add your custom bot here.
    available_bots: typing.List[Bot] = [
        Telegram,
    ]

    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.bots: typing.List[Bot] = list()

        # Loading configurations
        self.config.read("fembots/bot.ini")

        # Initializing bots
        for bot in Bot_Manager.available_bots:
            config_attr = f"enable_{bot.name}_bot"
            use_bot = self.config["DEFAULT"].get(config_attr, "no")
            if use_bot == "yes":
                print(f"Using {bot.name} bot")
            else:
                print(f"Not using {bot.name} bot")

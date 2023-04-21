import typing

from .Bot import Bot


class Telegram(Bot):
    """A bot to communicate over telegram"""

    name = "telegram"

    def __init__(self, config: typing.Dict[str, str]) -> None:
        super().__init__(config)

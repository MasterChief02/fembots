import typing


class Bot:
    """Parent class for all kind of bots."""

    name = ""
    api_endpoint = ""

    def __init__(self, config: typing.Dict[str, str]) -> None:
        pass


    def start(self) -> bool:
        """Starts a bot to receive message.

        Params: self

        Return: Boolean
        """
        pass

    def response(self) -> None:
        """Sends response of the message
        
        Params: self
        
        Return: None
        """
        pass

    def close(self) -> None:
        """Closes the bot.

        Params: self
        
        Return: None
        """
        pass


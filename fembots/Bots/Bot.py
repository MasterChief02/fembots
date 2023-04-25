import typing


class Bot:
    """Parent class for all kind of bots."""

    # Attribute to be used get section from configuration file.
    name = ""

    # API endpoint to bes used to communicate with NLP engine.
    api_endpoint = ""

    def __init__(self, config: typing.Dict[str, str]) -> None:
        """
        Initializes the bot.

        Parameters
        ----------
        config: Dict[str, str]
            Contains all the key value pairs stored in configuration file.

        Return
        ------
        None
        """
        pass

    def start(self) -> bool:
        """
        Function to start the bot.

        Parameters
        ----------
        None

        Return
        ------
        bool: Returns true if started successfully, false otherwise.
        """
        return True

    def stop(self) -> None:
        """
        Function to stop the bot and do necessary memory clean ups.

        Parameters
        ----------
        None

        Return
        ------
        None
        """
        pass

    def get_response_from_NLP(self, message: str) -> str:
        """
        Function to retrieve response from NLP engine for a given message.

        Parameters
        ----------
        message: str
            Message for which the response is to be fetched.

        Return
        ------
        str: Response message from NLP engine.
        """
        return message

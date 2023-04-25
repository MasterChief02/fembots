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

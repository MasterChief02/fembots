import typing


class Engine:
    """A template for dynamically loadable engine class."""

    def __init__(self) -> None:
        pass

    def process_message(self, message: str) -> typing.Tuple[int, typing.Dict[str, str]]:
        """
        A function to analyze the message and return the API number to be used in
        nlp_engine.ini, and the parameters that will be supplied with the API call.

        Parameters
        ----------
        message:str
            Message sent by the user.

        Return
        ------
            typing.Tuple[int,typing.Dict[str,str]]: API call number and its
            parameters.
        """
        print(message)
        return (1, {"message": "message"})

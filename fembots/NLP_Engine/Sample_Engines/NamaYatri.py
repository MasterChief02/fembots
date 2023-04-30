import typing

import nltk
from rake_nltk import Rake

from .Template import Engine


class NamaYatri(Engine):
    def __init__(self) -> None:
        self.rake = Rake()

        nltk.download("punkt")
        nltk.download("stopwords")

    def process_message(self, message: str) -> typing.Tuple[int, typing.Dict[str, str]]:
        code = 100
        data = dict()

        # Processing message
        message = message.lower()
        self.rake.extract_keywords_from_text(message)
        keywords = self.rake.get_ranked_phrases()
        keywords_with_book = [k for k in keywords if "book" in k.lower()]
        keywords_with_pay = [k for k in keywords if "pay" in k.lower()]

        # For booking
        if len(keywords_with_book) > 0:
            code = 0
            data = {
                "mode": "car",
                "start": "",
                "end": "",
            }

            if "bike" in message:
                data["mode"] = "bike"
            elif "auto" in message:
                data["mode"] = "auto"

            data["end"] = message.split("to")[-1]
            data["start"] = message.split("from")[-1].split("to")[0]

        # For payment
        if len(keywords_with_pay) > 0:
            code = 1
            data = {
                "mode": "online",
            }

            if "offline" in message:
                data["mode"] = "offline"

        return (code, data)

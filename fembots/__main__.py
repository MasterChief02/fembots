# type: ignore[attr-defined]

import argparse

from . import Bots, NLP_Engine


def app():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["bot", "nlp_engine"], default="bot")
    args = parser.parse_args()

    mode = args.mode
    print(mode)
    if mode == "bot":
        Bots.Bot_Manager().start()
    else:
        NLP_Engine.NLP_Engine_Manager().start()


if __name__ == "__main__":
    print("Hello")

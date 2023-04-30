import typing

import configparser
import json

import requests
from flask import Flask, request

from .Sample_Engines import Engine


class NLP_Engine_Manager:
    """A class to manage the NLP engine"""

    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.app = Flask(__name__)

        # Loading configurations
        self.config.read("fembots/nlp_engine.ini")

        # Loading API configurations
        self.host = self.config["DEFAULT"].get("host", "0.0.0.0")
        self.port = int(self.config["DEFAULT"].get("port", "5000"))
        self.endpoint = self.config["DEFAULT"].get("endpoint", "/")
        print(self.endpoint)

        # Loading NLP engine
        class_name = self.config["DEFAULT"].get("engine", "Engine")
        print(class_name)
        self.engine = Engine()

        # Loading API endpoints
        self.number_of_api_endpoints = int(
            self.config["BACKEND"].get("number_of_api_endpoints", "0")
        )
        self.api_endpoints = list()
        for i in range(self.number_of_api_endpoints):
            endpoint = self.config["BACKEND"].get(f"api_endpoint_{i}", "0")
            self.api_endpoints.append(endpoint)

        # Handling requests from bots
        @self.app.post(self.endpoint)
        def handle_bot_request():
            try:
                data = dict(request.get_json())

                # Retrieving API number and parameters
                message = data.get("message", "")
                code, data = self.engine.process_message(message)

                # Forwarding response from the API
                endpoint = self.api_endpoints[code]
                headers = {"Content-Type": "application/json"}
                response = requests.post(endpoint, json.dumps(data), headers=headers)
                return response.json(), 201
            except:
                return {"message": "Sorry something went wrong"}, 415

    def start(self) -> bool:
        """
        Function to start the NLP Engine API server.

        Parameters
        ----------
        None

        Return
        ------
        bool: Returns true if started successfully, false otherwise.
        """
        try:
            self.app.run(self.host, self.port)
            return True
        except:
            return False

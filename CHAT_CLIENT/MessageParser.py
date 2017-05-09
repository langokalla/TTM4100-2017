import json


class MessageParser():
    def __init__(self, client):

        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            'message': self.parse_message,
            'history': self.parse_history,
            'names': self.parse_names
        }

        self.client = client

    def parse(self, payload):
        payload = json.loads(payload.decode())
        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            print("You’ve met with a terrible fate, haven’t you?")

    def parse_error(self, payload):
        timestamp = payload["timestamp"]
        message = payload["content"]
        sender = payload["sender"]
        print("Sender:\t" + sender + "\t" + timestamp)
        print(message)

    def parse_info(self, payload):
        timestamp = payload["timestamp"]
        message = payload["content"]
        sender = payload["sender"]
        print("Sender:\t" + sender + "\t" + timestamp)
        print(message)
        print()

    def parse_message(self, payload):
        timestamp = payload["timestamp"]
        message = payload["content"]
        sender = payload["sender"]
        print("Sender:\t" + sender + "\t" + timestamp)
        print(message)
        print()

    def parse_history(self, payload):
        self.parse_message(payload)

    def parse_names(self, payload):
        timestamp = payload["timestamp"]
        message = payload["content"]
        sender = payload["sender"]
        print("Sender:\t" + sender + "\t" + timestamp)
        print(message)
        print()
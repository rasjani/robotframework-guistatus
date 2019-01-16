from requests import post
import json
ROBOT_LISTENER_API_VERSION = 2

class GuiStatusListener(object):
    ROBOT_LISTENER_API_VERSION = 2

    def _POST(self, payload):
        res = post(self.endpoint, json=json.dumps(payload))

    def __init__(self, endpoint="http://127.0.0.1:31337"):
        self.endpoint = endpoint

    def start_suite(self, name, attrs):
        self._POST({"suite_text": f"Running {name}" })

    def end_suite(self, name, attrs):
        self._POST({"suite_text": f"Done {name}" })

    def start_test(self, name, attrs):
        self._POST({"task_text": f"Running {name}" })

    def end_test(self, name, attrs):
        self._POST({"task_text": f"Running {name}" })

    def start_keyword(self, name, attrs):
        self._POST({"keyword_text": f"Running {name}" })

    def end_keyword(self, name, attrs):
        self._POST({"keyword_text": f"Done {name}" })

    def log_message(self, message):
        self._POST({"log_text": f"{message['message']}" })

    def close(self):
        pass

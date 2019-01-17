from salabsutils import DynamicRobotApiClass
from robot.api import logger
from robot.api.deco import keyword
import sys
import os
import requests
import socket
import errno
from furl import furl
from time import time as now
from time import sleep
from subprocess import Popen, DEVNULL


class GuiStatusKeywords(DynamicRobotApiClass):
    def __init__(self, host="http://127.0.0.1:31337"):
        self.host = host
        self.status_ui_process = None
        self.status_ui_app_script = os.path.join(os.path.dirname(os.path.realpath(__file__)), "GuiStatusApplication.py")

    @keyword
    def start_status_ui(self):
        self.status_ui_process = Popen([sys.executable, self.status_ui_app_script], stdout=DEVNULL, stderr=DEVNULL)
        self.endpoint_running = self._wait_for_status_endpoint()
        return self.endpoint_running

    @keyword
    def stop_status_ui(self):
        if self.status_ui_process is not None:
            self.status_ui_process.terminate()
            self.status_ui_process = None

    def _wait_for_status_endpoint(self, timeout=60, retries = 5):
        # TODO: This is shit, rewrite
        url_data = furl(self.host)
        s = socket.socket()
        if timeout:
            end = now() + timeout

        while True:
            if retries == 0:
                return False
            s = socket.socket()
            try:
                if timeout:
                    next_timeout = end - now()
                    if next_timeout < 0:
                        return False
                    else:
                        s.settimeout(next_timeout)

                s.connect((url_data.host, url_data.port))
            except socket.timeout as err:
                if timeout:
                    return False
            except ConnectionRefusedError as err:
                pass
            except socket.error as err:
                if type(err.args) != tuple or err[0] != errno.ETIMEDOUT:
                    raise
            else:
                s.close()
                return True
            finally:
                retries -= 1
                sleep(0.5)
                s.close()

    @keyword
    def status_ui_progressbar(self, steps):
        ret = requests.post(self.host, json={"action": "progressbar", "payload": int(steps)})

    @keyword
    def status_ui_action(self, action):
        field = "action"
        ret = requests.post(self.host, json={field: action})

    @keyword
    def status_ui_log(self, message, endpoint="status"):
        field = f"{endpoint}_text"
        ret = requests.post(self.host, json={field: message})

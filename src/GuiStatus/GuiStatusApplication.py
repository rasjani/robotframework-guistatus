#!/usr/bin/env python
from GuiStatusUI import GuiStatusUI
from GuiStatusServer import GuiStatusServer
import threading
import logging
from gevent.pywsgi import WSGIServer
import flask
import flask_restful

if __name__ == "__main__":
    log = logging.getLogger("werkzeug")
    log.disabled = True
    remote_interface = flask.Flask(__name__)
    remote_interface.logger.disabled = True
    remote_api = flask_restful.Api(remote_interface)
    gui_app = GuiStatusUI()
    remote_api.add_resource(GuiStatusServer, "/", resource_class_kwargs={"ui": gui_app})

    def flask_main():
        http_server = WSGIServer(("", 31337), remote_interface, log=None)
        http_server.serve_forever()

    flask_process = threading.Thread(target=flask_main)
    flask_process.daemon = True
    flask_process.start()
    gui_app.mainloop()

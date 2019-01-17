#!/usr/bin/env python
import flask
import flask_restful
import json

class GuiStatusServer(flask_restful.Resource):
    def __init__(self, **kwargs):
        self.ui = kwargs['ui']
        self.counter = 0

    def post(self):
        # TODO: this is funky, sometimes flask.request.json is string,
        # sometimes note. Most likely due to some content-type headers?
        try:
            json_data = json.loads(flask.request.json)
        except:
            json_data = flask.request.json

        self.ui.sb.step()
        if 'status_text' in json_data:
            self.ui.status_text.set(json_data['status_text'])
        if 'suite_text' in json_data:
            self.ui.suite_text.set(json_data['suite_text'])

        if 'action' in json_data:
            if json_data["action"] == "shutdown":
                self.ui.sb.stop()
                self.ui.pb.stop()
                self.ui.master.quit()
            if json_data["action"] == "reset":
                self.ui.clear_text()
            if json_data["action"] == "step":
                self.ui.pb.step()
            if json_data["action"] == "progressbar":
                self.ui.add_progressbar(int(json_data["payload"]))

        return {'status': 'ok'}

    def get(self):
        return {'status': 'ok'}

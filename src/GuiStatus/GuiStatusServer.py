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

        if 'status_text' in json_data:
            self.ui.status_text.set(json_data['status_text'])
        if 'keyword_text' in json_data:
            self.ui.keyword_text.set(json_data['keyword_text'])
        if 'suite_text' in json_data:
            self.ui.suite_text.set(json_data['suite_text'])
        if 'task_text' in json_data:
            self.ui.task_text.set(json_data['task_text'])
        if 'log_text' in json_data:
            self.ui.log_text.set(json_data['log_text'])

        if 'action' in json_data:
            if json_data["action"] == "shutdown":
                self.ui.master.quit()
            if json_data["action"] == "reset":
                self.ui.clear_text()
            if json_data["action"] == "step":
                self.ui.pb.step()

        return {'status': 'ok'}

    def get(self):
        return {'status': 'ok'}

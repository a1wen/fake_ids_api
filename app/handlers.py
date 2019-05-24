from tornado.web import RequestHandler
from tornado import escape

from settings import GOOD_CLIENT_STORAGE, BAD_CLIENT_STORAGE, html_template, response_template


class ByPassportData(RequestHandler):
    def get(self):
        uid = self.get_argument('id')

        if uid is None:
            self.render_string('error', error_code=6, error_reason='Not found')
            return

        self.render_embed_js('alert("It is works")')

    def post(self):
        data = escape.json_decode(self.request.body)


class ByMSISDN(RequestHandler):
    def get(self):
        uid = self.get_argument('id')

        if uid is None:
            self.render_string('error', error_code=6, error_reason='Not found')
            return

        self.render(html_template.format('It is works'))

    def post(self):
        request = self.request
        request_body = escape.json_decode(self.request.body)

        if request is None:
            self.set_status(404)
            self.finish('Action not found')

        gc = GOOD_CLIENT_STORAGE.get(request_body['msisdn'])
        bc = BAD_CLIENT_STORAGE.get(request_body['msisdn'])

        response = response_template

        if gc is not None:
            response['code'] = 0
            self.set_status(200)
            self.finish(response)
        elif bc is not None:
            response['code'] = 9
            response['description'] = 'хуц'
            self.set_status(200)
            self.finish(response)


class SimpleCheck(RequestHandler):
    def get(self):
        uid = self.get_argument('id')

        if uid is None:
            self.render_string('error', error_code=6, error_reason='Not found')
            return

        self.render_embed_js('alert("It is works")')

    def post(self):
        data = escape.json_decode(self.request.body)

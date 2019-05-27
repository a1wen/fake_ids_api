import jsonschema
from tornado.web import RequestHandler
from tornado import escape

from utils.response_templates import *
from settings import GOOD_CLIENT_STORAGE, BAD_CLIENT_STORAGE
from utils.schema_validator import schema_validation


class ByPassportData(RequestHandler):
    def post(self):
        blacklist = ['first_name', 'surname', 'birth_date', 'series', 'number', 'issue_date']
        request = self.request
        request_body = escape.json_decode(self.request.body)

        if request is None:
            self.set_status(404)
            self.finish('Action not found')

        response = BY_PASSPORT_TEMPLATE

        try:
            schema_validation('by_passport_resp_schema.json', request_body)
        except jsonschema.exceptions.ValidationError as e:
            self.set_status(400)
            response['code'] = 9
            response['description'] = e.message
            self.finish(response)

        if [k for k, v in request_body.items() if not v and k in blacklist]:
            response['code'] = 1
            response['description'] = 'Request has empty fields.'
            self.set_status(400)
            self.finish(response)
        else:
            gc = GOOD_CLIENT_STORAGE.get_msisdn(request_body['msisdn'])
            bc = BAD_CLIENT_STORAGE.get_msisdn(request_body['msisdn'])

        if gc is not None:
            response['code'] = 0
            self.set_status(200)
            self.finish(response)
        elif bc is not None:
            response['code'] = 11
            response['description'] = 'Person in a terrorist list'
            response['is_person_in_terror_list'] = True
            response['is_person_in_white_list'] = False
            self.set_status(200)
            self.finish(response)


class ByMSISDN(RequestHandler):
    def post(self):
        blacklist = ['first_name', 'surname', 'birth_date', 'msisdn']
        request = self.request
        request_body = escape.json_decode(self.request.body)

        if request is None:
            self.set_status(404)
            self.finish('Action not found')

        response = BY_MSISDN_TEMPLATE

        try:
            schema_validation('by_msisdn_resp_schema.json', request_body)
        except jsonschema.exceptions.ValidationError as e:
            self.set_status(400)
            response['code'] = 9
            response['description'] = e.message
            self.finish(response)

        if [k for k, v in request_body.items() if not v and k in blacklist]:
            response['code'] = 1
            response['description'] = 'Request has empty fields.'
            self.set_status(400)
            self.finish(response)
        else:
            gc = GOOD_CLIENT_STORAGE.get_msisdn(request_body['msisdn'])
            bc = BAD_CLIENT_STORAGE.get_msisdn(request_body['msisdn'])

        if gc is not None:
            response['code'] = 0
            self.set_status(200)
            self.finish(response)
        elif bc is not None:
            response['code'] = 11
            response['description'] = 'Person in a terrorist list'
            response['is_person_in_terror_list'] = True
            response['is_person_in_white_list'] = False
            self.set_status(200)
            self.finish(response)


class SimpleCheck(RequestHandler):
    def post(self):
        blacklist = []
        request = self.request
        request_body = escape.json_decode(self.request.body)

        if request is None:
            self.set_status(404)
            self.finish('Action not found')

        response = SIMPLE_CHECK_TEMPLATE

        try:
            schema_validation('simple_check_schema.json', request_body)
        except jsonschema.exceptions.ValidationError as e:
            self.set_status(400)
            response['code'] = 9
            response['description'] = e.message
            self.finish(response)

        if [k for k, v in request_body.items() if not v and k in blacklist]:
            response['code'] = 1
            response['description'] = 'Request has empty fields.'
            self.set_status(400)
            self.finish(response)
        else:
            gc = GOOD_CLIENT_STORAGE.get_msisdn(request_body['msisdn'])
            bc = BAD_CLIENT_STORAGE.get_msisdn(request_body['msisdn'])

        if gc is not None:
            response['code'] = 0
            self.set_status(200)
            self.finish(response)
        elif bc is not None:
            response['code'] = 11
            response['description'] = 'Person in a terrorist list'
            response['is_person_in_terror_list'] = True
            response['is_person_in_white_list'] = False
            self.set_status(200)
            self.finish(response)


class SimpleCheckLazy(RequestHandler):
    def post(self):
        blacklist = []
        request = self.request
        request_body = escape.json_decode(self.request.body)

        if request is None:
            self.set_status(404)
            self.finish('Action not found')

        response = SIMPLE_CHECK_LAZY_TEMPLATE

        try:
            schema_validation('simple_check_lazy_schema.json', request_body)
        except jsonschema.exceptions.ValidationError as e:
            self.set_status(400)
            response['code'] = 9
            response['description'] = e.message
            self.finish(response)

        if [k for k, v in request_body.items() if not v and k in blacklist]:
            response['code'] = 1
            response['description'] = 'Request has empty fields.'
            self.set_status(400)
            self.finish(response)
        else:
            gc = GOOD_CLIENT_STORAGE.get_msisdn(request_body['msisdn'])
            bc = BAD_CLIENT_STORAGE.get_msisdn(request_body['msisdn'])

        if gc is not None:
            response['code'] = 0
            self.set_status(200)
            self.finish(response)
        elif bc is not None:
            response['code'] = 11
            response['description'] = 'Person in a terrorist list'
            response['is_person_in_terror_list'] = True
            response['is_person_in_white_list'] = False
            self.set_status(200)
            self.finish(response)


class FullCheck(RequestHandler):
    def post(self):
        blacklist = []
        request = self.request
        request_body = escape.json_decode(self.request.body)

        if request is None:
            self.set_status(404)
            self.finish('Action not found')

        response = FULL_CHECK_TEMPLATE

        try:
            schema_validation('full_check_schema.json', request_body)
        except jsonschema.exceptions.ValidationError as e:
            self.set_status(400)
            response['code'] = 9
            response['description'] = e.message
            self.finish(response)

        if [k for k, v in request_body.items() if not v and k in blacklist]:
            response['code'] = 1
            response['description'] = 'Request has empty fields.'
            self.set_status(400)
            self.finish(response)
        else:
            gc = GOOD_CLIENT_STORAGE.get_msisdn(request_body['msisdn'])
            bc = BAD_CLIENT_STORAGE.get_msisdn(request_body['msisdn'])

        if gc is not None:
            response['code'] = 0
            self.set_status(200)
            self.finish(response)
        elif bc is not None:
            response['code'] = 11
            response['description'] = 'Person in a terrorist list'
            response['is_person_in_terror_list'] = True
            response['is_person_in_white_list'] = False
            self.set_status(200)
            self.finish(response)


class FullCheckLazy(RequestHandler):
    def post(self):
        blacklist = []
        request = self.request
        request_body = escape.json_decode(self.request.body)

        if request is None:
            self.set_status(404)
            self.finish('Action not found')

        response = FULL_CHECK_LAZY_TEMPLATE

        try:
            schema_validation('full_check_lazy_schema.json', request_body)
        except jsonschema.exceptions.ValidationError as e:
            self.set_status(400)
            response['code'] = 9
            response['description'] = e.message
            self.finish(response)

        if [k for k, v in request_body.items() if not v and k in blacklist]:
            response['code'] = 1
            response['description'] = 'Request has empty fields.'
            self.set_status(400)
            self.finish(response)
        else:
            gc = GOOD_CLIENT_STORAGE.get_msisdn(request_body['msisdn'])
            bc = BAD_CLIENT_STORAGE.get_msisdn(request_body['msisdn'])

        if gc is not None:
            response['code'] = 0
            self.set_status(200)
            self.finish(response)
        elif bc is not None:
            response['code'] = 11
            response['description'] = 'Person in a terrorist list'
            response['is_person_in_terror_list'] = True
            response['is_person_in_white_list'] = False
            self.set_status(200)
            self.finish(response)

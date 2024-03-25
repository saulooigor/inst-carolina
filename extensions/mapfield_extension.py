from flask import request

def field_value(field):
        return request.form.get(field)
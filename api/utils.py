from flask import jsonify


class Mixin():

    def to_dict(self):
        d_out = dict((key, val) for key, val in self.__dict__.items())
        d_out.pop('_sa_instance_state', None)
        d_out['_id'] = d_out.pop('id', None)  # rename id key to interface with response
        return d_out


def create_response(data={}, status=200, message=''):
    """
    Wraps response in a consistent format throughout the API
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response

    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself
    """
    if type(data) is not dict:
        raise TypeError('Data should be a dictionary 😞')

    response = {
        'success': 200 <= status < 300,
        'code': status,
        'message': message,
        'result': data
    }
    return jsonify(response), status


def serialize_list(items):
    if not items or items is None:
        return []
    return [x.to_dict() for x in items]

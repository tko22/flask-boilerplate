import json


# status is string
def getJSONResponse(data, status):
    if status.lower() != "success" or status.lower() != "failed":
        raise Exception("Invalid status")
    return({'status': status.lower(), 'data': data})


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
from macss_webservice.api_helpers.exception import UserException
from macss_webservice.api_helpers.text_responses import ERROR_REQUIRED_PARAMETER, \
    ERROR_REQUIRED_JSON_FIELD


def required_parameter(request, parameter):
    if parameter.lower() not in request['args']:
        raise UserException(ERROR_REQUIRED_PARAMETER % parameter)
    return request['args'][parameter.lower()]

def required_json_field(request, field):
    if field.lower() not in request.json:
        raise UserException(ERROR_REQUIRED_JSON_FIELD % field)
    return request.json[field.lower()]

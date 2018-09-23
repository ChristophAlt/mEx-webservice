from macss_webservice.api_helpers.exception import UserException
from macss_webservice.api_helpers.text_responses import ERROR_REQUIRED_PARAMETER


def required_parameter(request, parameter):
    if parameter.lower() not in request['args']:
        raise UserException(ERROR_REQUIRED_PARAMETER % parameter)
    return request['args'][parameter.lower()]

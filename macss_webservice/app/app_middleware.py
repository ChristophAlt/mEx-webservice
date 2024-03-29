import json
from functools import wraps

from sanic.response import json as jsonify
from sanic.exceptions import SanicException
from macss_webservice.api_helpers.headers import generate_cors_headers


def respond_with_json(decorated):
    @wraps(decorated)
    def wrapper(request, *args, **kw):
        try:
            status = 200
            result = decorated(request, *args, **kw)
            if 'success' not in result:
                result = {'success': True, 'result': result}
        except SanicException as e:
            status = getattr(e, 'status_code', 500)
            result = {'success': False, 'message': str(e)}
        
        return jsonify(result, status=status, headers=generate_cors_headers(request))

    return wrapper

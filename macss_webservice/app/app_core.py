import json
import os
import time

from macss_webservice.app.app_settings import URL_BASE
from macss_webservice.app.app_settings import app_endpoints
from macss_webservice.app.app_middleware import respond_with_json
from macss_webservice.api_helpers.exception import UserException
from macss_webservice.webservice_settings import CONFIG_SERVER, HOSTNAME
from macss_webservice.api_helpers.input import required_parameter
from macss_medical_ie.macss_medical_ie_pipeline import MedicalIEPipeline
from macss_medical_ie.utils.document_helper import doc_to_brat


_endpoint_route = lambda x: app_endpoints.route(URL_BASE + x, methods=['GET', 'POST'])


@_endpoint_route('/test')
@respond_with_json
def _test(request):
    return {'worker': os.getpid(), 'hostname': HOSTNAME, 'port': CONFIG_SERVER['port']}


@_endpoint_route('/annotate')
@respond_with_json
def _annotate(request):
    text = request.json['text']
    doc = MedicalIEPipeline.get_annotated_document(text)
    return doc_to_brat(doc)


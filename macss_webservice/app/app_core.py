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
from macss_medical_ie.pipeline.normalization import normalize_text
from macss_medical_ie.utils.document_helper import doc_to_brat


_endpoint_route = lambda x: app_endpoints.route(URL_BASE + x, methods=['GET', 'POST'])


@_endpoint_route('/test')
@respond_with_json
def _test(request):
    return {'worker': os.getpid(), 'hostname': HOSTNAME, 'port': CONFIG_SERVER['port']}


@_endpoint_route('/annotate')
@respond_with_json
def _annotate(request):
    text = normalize_text(request.json['text'])
    doc = MedicalIEPipeline.get_annotated_document(text)
    return doc_to_brat(doc)


@_endpoint_route('/pipeline')
@respond_with_json
def _pipeline(request):
    def get_component_info(name, component):
        component_info = {}
        if name == 'ner':
            available_tags = component.tagger.tag_dictionary.get_items()
            available_tags = [tag.split('-')[-1].lower() for tag in available_tags]
            available_tags = [tag for tag in available_tags if tag not in ['<unk>', 'o', '<start>', '<stop>']]
            component_info['available_tags'] = list(set(available_tags))

        elif name == 'relation_extraction':
            available_tags = component.clf.label_dictionary.get_items()
            available_tags = [tag[:-7].lower() for tag in available_tags]
            component_info['available_tags'] = list(set(available_tags))

        return component_info

    p = MedicalIEPipeline.get_pipeline()

    pipeline_info = dict(components={name: get_component_info(name, component) for name, component in p.pipeline})

    return pipeline_info

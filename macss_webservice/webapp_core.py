from typing import Union
from sanic import Sanic
from logging import info, debug
from macss_webservice import webservice_settings
from macss_webservice.app.app_core import app_endpoints
from macss_medical_ie.macss_medical_ie_pipeline import MedicalIEPipeline


app = Sanic(__name__)
app.blueprint(app_endpoints)

app.config.update(webservice_settings.CONFIG_WEBAPP)

info(f"List of active endpoints { app.router.routes_all.keys() }")


def run(port: Union[None, int] = None):
    if port is not None:
        webservice_settings.CONFIG_SERVER['port'] = int(port)
    info(f"Using port: { webservice_settings.CONFIG_SERVER['port'] }")
    info(f'Pipeline: { MedicalIEPipeline.get_pipeline().pipe_names }')
    app.config.LOGO = None
    app.run(**webservice_settings.CONFIG_SERVER)

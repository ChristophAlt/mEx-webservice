from typing import Union
from sanic import Sanic
from logging import info
from macss_webservice import webservice_settings
from macss_webservice.app.app_core import app_endpoints


app = Sanic(__name__)
app.blueprint(app_endpoints)

app.config.update(webservice_settings.WEBAPP_CONFIG)

info(f"List of active endpoints { app.router.routes_all.keys() }")


def run(port: Union[None, int] = None):
    if port is not None:
        webservice_settings.CONFIG_SERVER['port'] = int(port)
    info("Using port: %d", webservice_settings.CONFIG_SERVER['port'])
    app.config.LOGO = None
    app.run(**webservice_settings.CONFIG_SERVER)

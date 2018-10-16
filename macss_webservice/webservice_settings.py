import os
import sys
import logging

from sanic.log import LOGGING_CONFIG_DEFAULTS


# LOGGER = logging.getLogger('stream_logger')
HANDLER = 'logging.StreamHandler'
FORMATTER = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

LOGGING = dict(LOGGING_CONFIG_DEFAULTS)

LOGGING["formatters"]['stream_formatter'] = {
    'format': FORMATTER,
    'datefmt': '%Y-%m-%d %H:%M:%S',
}
LOGGING['handlers']['stream_handler'] = {
    'class': HANDLER,
    'formatter': 'stream_formatter',
    'stream': sys.stderr
}

LOGGING['loggers']['root'] = {'level': os.environ.get("LOGLEVEL", "INFO").upper(),
                              'handlers': ['stream_handler']}


def envint(varname: str, default: int) -> int:
    return int(os.getenv(varname, default))


def envbool(varname: str, default: bool) -> bool:
    var = os.getenv(varname, default)
    if isinstance(var, str):
        var = var.lower() in ['true', 'yes', '1', 't', 'y']
    return var


# SERVER configuration
CONFIG_SERVER = dict(
    host=os.getenv("MACSS_WEBSERVICE_HOST", "0.0.0.0"),
    port=envint("MACSS_WEBSERVICE_PORT", 5050),
    debug=envbool("MACSS_WEBSERVICE_DEBUG", False),
    workers=envint("MACSS_WEBSERVICE_WORKERS", 1),
    log_config=LOGGING,
)

# WEBAPP configuration
CONFIG_WEBAPP = dict(
    REQUEST_MAX_SIZE=envint("MACSS_WEBSERVICE_REQUEST_MAX_SIZE", int(100 * 1e6)),  # 100 megabytes
    REQUEST_TIMEOUT=envint("MACSS_WEBSERVICE_REQUEST_TIMEOUT", 600),  # 10 min
    KEEP_ALIVE=True,
    GRACEFUL_SHUTDOWN_TIMEOUT=envint("MACSS_WEBSERVICE_GRACEFUL_SHUTDOWN_TIMEOUT", 3),  # 3 sec
    WEBSOCKET_MAX_SIZE=envint("MACSS_WEBSERVICE_WEBSOCKET_MAX_SIZE", int(1e6)),  # 1 megabyte
    WEBSOCKET_MAX_QUEUE=envint("MACSS_WEBSERVICE_WEBSOCKET_MAX_QUEUE", 32)
)

HOSTNAME = os.getenv('MACSS_HOSTNAME', "DEV_SERVER")

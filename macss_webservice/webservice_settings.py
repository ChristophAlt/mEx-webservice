import os
import sys
import logging

from sanic.log import LOGGING_CONFIG_DEFAULTS


# LOGGER = logging.getLogger('stream_logger')
HANDLER = 'logging.StreamHandler'
FORMATTER = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

LOGGING = dict(LOGGING_CONFIG_DEFAULTS)

# # Remove file and syslog logging, handled from stdout
# LOGGING['handlers'].pop('errorTimedRotatingFile', None)
# LOGGING['handlers'].pop('accessTimedRotatingFile', None)
# LOGGING['handlers'].pop('accessSysLog', None)
# LOGGING['handlers'].pop('errorSysLog', None)

# # Handled by the root logger
# LOGGING['loggers'].pop('sanic', None)

LOGGING["formatters"]['stream_formatter'] = {
    'format': FORMATTER,
    'datefmt': '%Y-%m-%d %H:%M:%S',
}
LOGGING['handlers']['stream_handler'] = {
    'class': HANDLER,
    'formatter': 'stream_formatter',
    'stream': sys.stderr
}

# LOGGING['loggers']['network']['handlers'] = ['accessStream']

LOGGING['loggers']['root'] = {'level': os.environ.get("LOGLEVEL", "INFO").upper(),
                              'handlers': ['stream_handler']}


def envint(varname: str, default: int) -> int:
    return int(os.getenv(varname, default))


# SERVER configuration
CONFIG_SERVER = dict(
    host=os.getenv("MACSS_WEBSERVICE_HOST", "0.0.0.0"),
    port=envint("MACSS_WEBSERVICE_PORT", 5050), debug=True, workers=1, log_config=LOGGING,
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

import socket

from config import *

HOST = socket.gethostbyname(socket.gethostname())
ENDPOINT = '{0}:{1}'.format(HOST, PORT)
SWAGGER.update({'host': ENDPOINT})
# Temporary host

DEBUG = False

MONGODB_SETTINGS = {
    'db': SERVICE_NAME,
    'host': 'localhost',
}

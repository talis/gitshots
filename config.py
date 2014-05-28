import os

DEBUG = True

if os.environ.get('MONGOHQ_URL'):
    MONGO_URI = os.environ.get('MONGOHQ_URL')

MONGO_DBNAME = os.environ.get('MONGO_DB', 'gitshots')
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', None)
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', None)

AUTH_USERNAME = os.environ.get('AUTH_USERNAME', None)
AUTH_PASSWORD = os.environ.get('AUTH_PASSWORD', None)

OAUTH_ENDPOINT = os.environ.get('OAUTH_ENDPOINT','https://users.talis.com/oauth/tokens')
OAUTH_CLIENT_ID = os.environ.get('OAUTH_CLIENT_ID', None)
OAUTH_CLIENT_SECRET = os.environ.get('OAUTH_CLIENT_SECRET', None)

BABEL_ENDPOINT = os.environ.get('BABEL_ENDPOINT', 'https://feeds.talis.com')

CACHE_TYPE = 'filesystem'
CACHE_DIR = 'static/imgs'

MAX_CONTENT_LENGTH = 4 * 1024 * 1024  # No more than 10MB per file system

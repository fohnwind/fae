__author__ = 'fohnwind'

class DefaultConfig(object):
    DEBUG = True
    TESTING = False

    # Auth
    LOGIN_VIEW = 'auth.login'

    # Security
    SECRET_KEY = 'valar morghulis'

    SITE_NAME = "fae.com"
    # URL Prefixes
    USER_URL_PREFIX = "/u"
    AUTH_URL_PREFIX = "/a"
    PROJECT_URL_PREFIX = "/p"
    CONTAINER_URL_PREFIX = "/c"
    HOMEPAGE_URL_REFIX = ""

    # DB
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1/fae'
    SQLALCHEMY_ECHO = False

    # UPLOAD
    UPLOAD_FOLDER = '/home/fohnwind/fae/html/fae/uploads'
    ALLOWED_EXTENSIONS = {'zip', 'tar.gz', 'tar.bz2', 'php', 'py'}

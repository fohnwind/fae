__author__ = 'fohnwind'

class DefaultConfig(object):
    DEBUG = True
    TESTING = False

    # Auth
    LOGIN_VIEW = 'auth.login'

    # Security
    SECRET_KEY = 'fohnwind@78'

    SITE_NAME = "fae.com"
    # URL Prefixes
    USER_URL_PREFIX = "/u"
    AUTH_URL_PREFIX = "/a"
    PROJECT_URL_PREFIX = "/p"
    HOMEPAGE_URL_REFIX = ""

    # DB
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1/fae'
    SQLALCHEMY_ECHO = False

    # UPLOAD
    UPLOAD_FOLDER = '/home/fohnwind/fae/html/fae/uploads'
    ALLOWED_EXTENSIONS = {'zip', 'tar.gz', 'tar.bz2', 'php', 'py'}
__author__ = 'fohnwind'

class DefaultConfig(object):
    DEBUG = True
    TESTING = False

    # Auth
    LOGIN_VIEW = 'views.auth.login'

    # Security
    SECRET_KEY = 'fohnwind@78'


    # URL Prefixes
    USER_URL_PREFIX = "/u"
    AUTH_URL_PREFIX = "/a"
    PROJECT_URL_PREFIX = "/p"
    HOMEPAGE_URL_REFIX = ""

    # DB
    SQLALCHEMY_DATABASES_URI = 'mysql://fohnwind:fohnwind@localhost/fae'
    SQLALCHEMY_ECHO = False

    # UPLOAD
    UPLOAD_FOLDER = '/home/fohnwind/fae/html/fae/uploads'
    ALLOWED_EXTENSIONS = {'zip', 'tar.gz', 'tar.bz2', 'php', 'py'}
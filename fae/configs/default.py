__author__ = 'fohnwind'

class DefaultConfig(object):
    DEBUG = True
    TESTING = False

    # Auth
    LOGIN_VIEW = 'views.login.login'

    # Security
    SECRET_KEY = 'fohnwind@78'


    # URL Prefixes
    USER_URL_PREFIX = "/u"
    AUTH_URL_PREFIX = "/auth"
    APP_URL_PREFIX = "/a"
    HOMEPAGE_URL_REFIX = ""

    # DB
    SQLALCHEMY_DATABASES_URI = 'mysql://'
    SQLALCHEMY_ECHO = False
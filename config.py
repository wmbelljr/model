class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "Tenaj71611940AveG23pyTkinter20@#"

    DB_NAME = 'debase_pdtn'
    DB_USERNAME = 'root'
    DB_PASSWORD = '23pyTkinter20#@'

    UPLOADS = '/static/images/uploads'

    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = 'dbase_dev'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'password'

    UPLOADS = 'home/static/images/uploads'

    SESSION_COOKIE_SECURE = False



class TestingConfig(Config):
    TESTING = True

    DB_NAME = 'dbase_dev'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'password'

    SESSION_COOKIE_SECURE = False


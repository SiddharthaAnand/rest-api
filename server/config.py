
class Development(object):
    """
    Development environment configuration.
    """
    DEBUG = True
    TESTING = False


class Production(object):
    """
    Production environment configuration.
    """
    DEBUG = False
    TESTING = False


class Testing(object):
    """
    Development environment configuration.
    """
    TESTING = True


app_config = {
    'testing': Testing,
    'production': Production,
    'development': Development
}
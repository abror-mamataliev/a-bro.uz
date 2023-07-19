from decouple import config


class Config:

    BASE_URL = config('BASE_URL', default="0.0.0.0")

    HOST = config('HOST', default="0.0.0.0")
    PORT = config('PORT', cast=int, default=5000)


class DevConfig(Config):

    DEBUG = True


class ProdConfig(Config):

    pass

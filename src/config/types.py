from decouple import config


class Config:

    BASE_URL = config('BASE_URL', default="http://127.0.0.1:5000")

    HOST = config('HOST', default="0.0.0.0")
    PORT = config('PORT', cast=int, default=5000)

    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')


class DevConfig(Config):

    DEBUG = True


class ProdConfig(Config):

    pass

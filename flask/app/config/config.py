import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))


def create_sqlite_uri(db_name):
    return "sqlite:///" + os.path.join(basedir, db_name)


class BaseConfig:  # 基本配置
    SECRET_KEY = 'CHANGE THIS KEY'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=14)

    JWT_SECRET_KEY = 'CHANGE THIS JWT KEY'
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=30)


class DevelopmentConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:tokio328@IP:3306/youbike'


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = create_sqlite_uri("test.db")
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
    'base': BaseConfig
}

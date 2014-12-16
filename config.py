import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',     
        'sqlite:///' + os.path.join(basedir, 'app.db'))
SECRET_KEY =              os.getenv('SECRET_KEY',       '')


CSRF_ENABLED = True
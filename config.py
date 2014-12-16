import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',     
        'sqlite:///' + os.path.join(basedir, 'app.db'))
SECRET_KEY =              os.getenv('SECRET_KEY',       '\xc4\xc2\xcfB0\xd7A\xf4A\xe8\xf4\xd5|x\xc1Q\xb32\x05\xde\x13\x10\xe1h')


CSRF_ENABLED = True
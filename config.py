import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


CSRF_ENABLED = True
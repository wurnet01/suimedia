import os
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy instance
db = SQLAlchemy()

def init_db(app):
    # Allow overriding the database URI via environment variable (useful on hosts)
    database_uri = os.environ.get('DATABASE_URL') or 'sqlite:///instance/social_platform.db'

    # If using a relative sqlite path, convert it to an absolute path to avoid
    # "unable to open database file" errors on Windows and hosted environments.
    if database_uri.startswith('sqlite:///'):
        sqlite_path = database_uri[len('sqlite:///'):]
        if not os.path.isabs(sqlite_path):
            base_dir = os.path.dirname(os.path.abspath(__file__))
            abs_path = os.path.abspath(os.path.join(base_dir, sqlite_path))
            # Normalize to forward slashes for SQLAlchemy on Windows
            abs_path = abs_path.replace('\\', '/')
            database_uri = f'sqlite:///{abs_path}'

    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the app
    db.init_app(app)

    # Ensure instance folder exists for SQLite file and uploads
    try:
        instance_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
        os.makedirs(instance_path, exist_ok=True)
    except Exception:
        pass

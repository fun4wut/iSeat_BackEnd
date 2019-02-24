import os
from app import db, create_app
from flask_migrate import Migrate
from app.models import User, Area, Table

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)
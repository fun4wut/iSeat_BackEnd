import os
from app import db, create_app
from app.models import User, Seat

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
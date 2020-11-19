from flask import Flask
from flask_migrate import Migrate
from .models import db
from .routes import *
from .config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
# app.register_blueprint(home.bp)

db.init_app(app)
Migrate(app, db)

@app.route('/')
def main():
    return '<h1>Hello World</h1>'

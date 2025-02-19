#!/usr/bin/env python3

from flask import Flask
from models import db
from flask_migrate import Migrate

app = Flask(__name__)
# configuring database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# configuring migration
migrate = Migrate(app, db)

# app initialization for use with our db configuration
db.init_app(app)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

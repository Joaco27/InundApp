from flask import Flask
from .models import db, Usuario

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)
    
    with app.app_context():
        db.create_all()  # Crea las tablas si no existen

    return app

from flask_bootstrap import Bootstrap
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

def create_app ():
    app = Flask(__name__)
    Bootstrap(app) 

    app.config['SQLALCHEMY_DATABSE_URI'] = 'postgresql://username:password@localhost/airplane-data'

    from pages import si_su, main
    app.register_blueprint(si_su)
    app.register_blueprint(main)
    
    return app


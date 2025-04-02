from flask import Flask
import os

def create_app():
    app = Flask(__name__, template_folder='website/templates') 
    app.config['SECRET_KEY'] = 'testWebsite!'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

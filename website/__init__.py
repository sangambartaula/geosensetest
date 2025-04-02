from flask import Flask
import os

def create_app():
    # Correct the path to templates, relative to the website folder
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
    app.config['SECRET_KEY'] = 'testWebsite!'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

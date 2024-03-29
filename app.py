"""
  Created by Yaser Ahmed on 18/03/2024.
"""
import os
from flask import Flask
from extentions import db
from public.routes import root_bp
from auth.routes import auth_bp
from dashboard.routes import dashboard_bp

def create_app():
    # flask app creation
    app = Flask(__name__)
    app.config.from_prefixed_env()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('FLASK_SQLALCHEMY_DATABASE_URI')
    """

      Register blueprints
      @root_bp: for public information
      @auth_pb: authentication and authorzation for the app and manage access
      @dashboard_bp: dashboard for the admin

    """
    app.register_blueprint(root_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    db.init_app(app)

    return app
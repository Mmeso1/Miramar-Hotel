from flask import Flask, render_template
from .config.variables import SECRET_KEY
import os

def create_app():
  app = Flask(__name__) 
  

  # CONFIGS
  app.config["SECRET_KEY"] = SECRET_KEY


  # BLUEPRINT
  from .views.user import user
  app.register_blueprint(user, url_prefix="/")

  

  return app
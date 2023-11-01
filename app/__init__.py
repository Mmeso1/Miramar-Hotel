from flask import Flask, request, render_template
from .config.variables import SECRET_KEY, EMAIL_PASSWORD 
from flask_mail import Mail, Message 
import os 


def create_app():
  app = Flask(__name__) 
  mail = Mail(app)

  # CONFIGS
  app.config["SECRET_KEY"] = SECRET_KEY
  app.config['MAIL_PASSWORD'] = EMAIL_PASSWORD
  
  # mail configs 
  app.config['MAIL_SERVER'] = 'smtp.gmail.com'
  app.config['MAIL_PORT'] = 465
  app.config['MAIL_USE_TLS'] = False
  app.config['MAIL_USE_SSL'] = True
  app.config['MAIL_USERNAME'] = 'testingweb3phoenix@gmail.com'
  


  
  # BLUEPRINT
  from .views.user import user
  from .views.admin import admin

  app.register_blueprint(user, url_prefix="/")
  app.register_blueprint(admin, url_prefix="/admin")

  
  # ERROR 404
  @app.errorhandler(404)
  def page_not_found(error):
    print("404 ERROR:", str(error))
    return render_template("error_404.html")
  

  # ERROR 500
  @app.errorhandler(Exception)
  def server_error(error):
    print("500 ERROR:", str(error))
    return render_template("error_500.html")
  


  return app
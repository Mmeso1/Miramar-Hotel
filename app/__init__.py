from flask import Flask, render_template
from .config.variables import SECRET_KEY
from .config.database import db
from flask_jwt_extended import JWTManager
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def create_app():
  app = Flask(__name__) 
  

  # CONFIGS
  app.config["SECRET_KEY"] = SECRET_KEY
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
  app.config["UPLOAD_PATH"] = os.path.join(BASE_DIR, "user_uploads/")

  # BLUEPRINT
  from .views.user import user
  from .views.admin import admin
  from .views.auth import auth
  from .views.rooms import room

  app.register_blueprint(user, url_prefix="/")
  app.register_blueprint(admin, url_prefix="/admin")
  app.register_blueprint(auth, url_prefix="/")
  app.register_blueprint(room, url_prefix="/")

  # MIDDLEWARES 
  JWTManager(app)

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
    

  db.init_app(app)
  with app.app_context():
      db.create_all()
  return app

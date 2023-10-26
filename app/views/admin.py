from flask import Blueprint, render_template

admin = Blueprint("admin", __name__) 

# In the init.py I prefixed the admin's route with /admin, so when you want to render a page's view, if the current route you named is /dashboard, you'll now type /admin/dashboard in the browser
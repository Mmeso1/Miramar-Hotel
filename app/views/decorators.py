from functools import wraps
from flask import request, redirect, session, url_for, flash
from flask_jwt_extended import get_jwt_identity
from flask_login import current_user
from datetime import datetime
from ..models import Token

# Cheecks if it is an admin, if the admin is authenticated and also if their token has expired
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # Check if the user is logged in and has the 'role' session variable
        if 'user_id' not in session or 'role' not in session:
            flash("You need to log in to access this page", "error")
            return redirect(url_for("user.landing_page"))

        # Check if the user's role is 'admin'
        if session['role'] != "admin":
            flash("You don't have permission to access this page", "error")
            return redirect(url_for("user.landing_page"))

        return fn(*args, **kwargs)

    return wrapper

# Updated user session check function, checks if a user is authenticated and session has not expired
def user_logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_token" not in session:
            return redirect(url_for("user.register_page"))  # Redirect to sign-up page
        return f(*args, **kwargs)

    return decorated_function

def user_exists_required(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        user_id = session.get("user_id")

        if user_id is None:
            flash("User does not exist", "error")
            return redirect(url_for("user.register_page"))

        return view_function(*args, **kwargs)

    return decorated_function

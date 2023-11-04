from functools import wraps
from flask import request, redirect, session, url_for, flash
from flask_login import current_user
from datetime import datetime

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

# Checks if the user's token has expired
def token_expired(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("You need to sign in to access this page", "error")
            return redirect(url_for("user.register_page"))

        # Check if the user's token is not expired (assuming you're using JWT)
        if current_user.token_expiration < datetime.utcnow():
            flash("Your session has expired. Please log in again.", "error")
            return redirect(url_for("user.login_page"))

        return fn(*args, **kwargs)

    return wrapper

def user_exists_required(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        user_id = session.get("user_id")

        if user_id is None:
            flash("User does not exist", "error")
            return redirect(url_for("user.register_page"))

        return view_function(*args, **kwargs)

    return decorated_function

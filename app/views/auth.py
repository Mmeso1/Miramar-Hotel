from datetime import timedelta, datetime
import  secrets, string
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from app.models.Token import PasswordResetToken
from ..config.database import db
from ..models import User, Room, Booking
from .decorators import user_exists_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    # Get user input from the request
    email = request.form.get("email").strip()
    username = request.form.get("username").strip()
    password = request.form.get("password").strip()
    session["original_url"] = request.referrer  # the current route

    # Check if any required field is empty
    if not email or not username or not password:
        flash("Please provide all required information", "error")
        return redirect(url_for("user.register_page"))
    
    valid, message = check_detail_authenticity(email, password)
    if not valid:
        flash(message, "error")
        return redirect(url_for("user.register_page"))
    
    # Check if the user already exists
    user = User.query.filter_by(email=email).first()
    if user:
        flash("Email already exists", "error")
        return redirect(url_for("user.login_page"))
 
    # For regular user registration
    user = User(
        username=username,
        email=email,
        password=password,
        role="user"
    )
    db.session.add(user)
    db.session.commit()
    
    session['user_id'] = user.id #store user id
    session['registration_success'] = True
    # Generate a token for the user and store it in a session
    expiry_time = timedelta(days=30)  # Set your desired token expiration time
    token = create_access_token(identity=user.id, expires_delta=expiry_time)
    session["user_token"] = token  # Store the token in the session
    print("Token stored in session")

    # After registration
    return redirect(url_for("user.landing_page"))

    
# Checks the viability of the input details
def check_detail_authenticity(email, password):
    if '@' not in email:
        return False, "Incorrect email"

    if len(password) < 8:
        return False, "Password length should be at least 8 characters"

    return True, "Valid details"

# The login route handling logic
@auth.route("/login", methods=["POST"])
@user_exists_required
def login():
    email = request.form.get("email").strip()
    password = request.form.get("password").strip()
    print(session.get('role'))

    # Check for empty inputs
    if not email or not password:
        flash("Please provide both email and password", "error")
        return redirect(url_for("user.login_page"))

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash("Invalid email or password", "error")
        return redirect(url_for("user.login_page"))
    
    # Handle token generation if needed
    expiry_time = timedelta(days=30)
    token = create_access_token(identity=user.id, expires_delta=expiry_time)

    # Store user deets in session
    session["role"] = user.role
    session["user_id"] = user.id
    session["user_token"] = token
    session['login_success'] = True

    if user.role == "admin":
        # Handle admin access
        flash("Admin login successful", "success")
        return redirect(url_for("admin.home_page"))
    else:
        return redirect(url_for("user.landing_page"))

# To render template to reset password
@auth.route("/password-reset-request")
def request_password_reset():
    # Retrieve the user's email from the request
    user_id = session.get('user_id')
    
    # Generate a unique token
    token = token = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(32))

    # Set the token's expiration (e.g., one hour from now)
    expiration = datetime.utcnow() + timedelta(hours=1)

    # Store the token and user email in the database
    password_reset_token = PasswordResetToken(user_id, token=token, expiration=expiration)
    if not user_id:
        flash("Login to access this page", "error")
        return redirect(url_for('user.login_page'))
    db.session.add(password_reset_token)
    db.session.commit()

    print(password_reset_token)
    # Allow the user to reset their password locally
    return render_template("password_reset.html", token=token)

# To authenticate the password reset
@auth.post("/password-reset/<token>")
def reset_password(token):
    user_id = session.get('user_id')
    # Look up the token in the database
    password_reset_token = PasswordResetToken.query.filter_by(token=token).first()
    print(f"User id: {user_id}")
    if password_reset_token and datetime.utcnow() <= password_reset_token.expiration:
        # Token is valid
        # Get the user associated with the token
        user = User.query.filter_by(id=user_id).first()

        if user:
            # Update the user's password (you'll need to implement a function to update the password)
            new_password = request.form.get("password")
            user.password = generate_password_hash(new_password)

            # Remove the token from the database
            db.session.delete(password_reset_token)
            db.session.commit()

            # Flash a success message
            flash("Password reset successfully. You can now log in with your new password.", "success")

            # Redirect the user to the login page
            return redirect(url_for("user.login_page"))
        else:
            flash("Invalid user.", "error")
    else:
        # Invalid or expired token; inform the user
        flash("Invalid or expired token.", "error")
        return redirect(url_for("auth.request_password_reset"))


# To logout user
@auth.route("/logout")
def logout():
    user_id = session.get("user_id")  # Store the user_id before clearing the session
    session.clear()  # Clear the entire session
    session["user_id"] = user_id  # Restore the user_id to the session

    # Redirect the user to the landing page or any other desired page
    return redirect(url_for("user.landing_page"))


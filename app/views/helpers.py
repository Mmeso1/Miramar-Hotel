# import secrets
# import string

# def generate_unique_token(token_length=32):
#     token = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(token_length))
#     return token


# def send_password_reset_email(email, token):
#     Create the password reset email message
#     msg = Message("Password Reset", recipients=[email])
#     msg.html = f"Click the link below to reset your password: <a href='https://example.com/reset-password?token={token}'>Reset Password</a>"

#     # Send the email
#     mail.send(msg)

# THE CONTENT OF THIS FILE IS TO STORE WHAT IT WOULD HAVE LOOKED LIKE IF I HAD HOSTED IT AND WANTED TO USE TOKENS FOR RESET PASSWORD
from dotenv import dotenv_values

ENV = dotenv_values()

# ENV VARIABLES
SECRET_KEY = ENV['SECRET_KEY']
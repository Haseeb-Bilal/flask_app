import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_hard_to_guess_string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://flaskhaseeb:123abc@localhost/haseebflaskdb2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


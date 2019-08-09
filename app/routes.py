from app import app
import os

check_value = os.environ.get('TYPE')


@app.route('/')
def index():
    return check_value
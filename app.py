from flask import Flask
from flask_login import LoginManager
from flask_pymongo import PyMongo

from models.user import User
from routes.auth import auth_blueprint
from routes.main import main_blueprint

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['MONGO_URI'] = 'your_mongodb_uri'
mongo = PyMongo(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # tbd
    return User.get(user_id)

app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

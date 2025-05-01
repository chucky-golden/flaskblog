from flask import Flask
from routes.basic import basic_route
from routes.auth import auth_route
from middlewares.dbconfig import init_mysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET")

# Initialize MySQL database with config
init_mysql(app)

# Set upload folder path
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Register blueprints
app.register_blueprint(basic_route, url_prefix="/")
app.register_blueprint(auth_route, url_prefix="/auth")


# start server
app.run(host='127.0.0.1', port=5100, debug=True)
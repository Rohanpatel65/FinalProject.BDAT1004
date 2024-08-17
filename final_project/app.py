from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from config.config import FIREBASE_CREDENTIALS, FIREBASE_DATABASE_URL
from api.routes import api_bp

app = Flask(__name__)

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CREDENTIALS)
    firebase_admin.initialize_app(cred, {
        'databaseURL': FIREBASE_DATABASE_URL
    })

# Register the API blueprint
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, jsonify, request
import requests
import firebase_admin
from config.config import FIREBASE_CREDENTIALS, FIREBASE_DATABASE_URL
from firebase_admin import db, credentials

api_bp = Blueprint('api', __name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate(FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred, {
        'databaseURL': FIREBASE_DATABASE_URL
    })

# Firebase DB reference
ref = db.reference('/covid_data')

# Endpoint to fetch and store data
@api_bp.route('/fetch_and_store', methods=['GET'])
def fetch_and_store_data():
    response = requests.get('https://disease.sh/v3/covid-19/countries/IN,UK,US,CA,AU')
    if response.status_code == 200:
        covid_data = response.json()
        ref.set(covid_data)  # Storing the data in Firebase
        return jsonify({'message': 'Data fetched and stored successfully'}), 200
    else:
        return jsonify({'error': 'Failed to fetch data'}), 500

# Get all stored data
@api_bp.route('/covid_data', methods=['GET'])
def get_covid_data():
    data = ref.get()
    return jsonify(data)
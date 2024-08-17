import requests
import firebase_admin
from firebase_admin import credentials, db
from config.config import FIREBASE_CREDENTIALS, FIREBASE_DATABASE_URL

# Initialize Firebase Admin SDK
cred = credentials.Certificate(FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred, {
    'databaseURL': FIREBASE_DATABASE_URL
})

def fetch_and_store_data():
    url = 'https://disease.sh/v3/covid-19/countries/IN,UK,US,CA,AU'
    response = requests.get(url)
    covid_data = response.json()

    ref = db.reference('covid_data')
    ref.set(covid_data)  

if __name__ == '__main__':
    fetch_and_store_data()
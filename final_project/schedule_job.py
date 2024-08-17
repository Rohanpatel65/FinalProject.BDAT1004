import schedule
import time
from fetch_data import fetch_and_store_data

def job():
    fetch_and_store_data()

schedule.every(24).hours.do(job)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
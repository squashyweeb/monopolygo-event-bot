import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from sinchsms import SinchSMS

# Sinch stuff
servicePlanId = 'your_sinch_service_plan_id'
apiToken = 'your_sinch_api_token'
sinch_phone_number = 'your_sinch_phone_number'

# send SMS using sinch
def send_sms(to_number, message):
    # Code for sending SMS using Sinch
    pass

# get events content
def get_events_content(url):
    # Code for getting events content from a URL
    pass

# save processed date
def save_processed_date(date):
    with open('processed_dates.txt', 'a') as file:
        file.write(date.strftime('%Y-%m-%d') + '\n')

# check if date is processed
def is_date_processed(date):
    with open('processed_dates.txt', 'r') as file:
        processed_dates = [line.strip() for line in file.readlines()]
    return date.strftime('%Y-%m-%d') in processed_dates

webhook_url = 'your_discord_webhook_url'

# Main date for check
main_date = datetime(2023, 12, 29).date()
current_date = main_date

while True:
    current_url = f'https://monopolygo.wiki/todays-events-{current_date.strftime("%b-%d-%Y").lower()}/'
    print(f"Checking {current_url}")

    if is_date_processed(current_date):
        print(f"Already processed {current_date}. Skipping.")
    else:
        try:
            response = requests.get(current_url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Page not found. Going back to the main date and waiting for 2 seconds.")
                current_date = main_date
                time.sleep(2)
                continue
            else:
                print(f"HTTP error: {e}")
                break

        new_events_content = get_events_content(current_url)
        if new_events_content:
            print(f'New events data for {current_date.strftime("%b %d, %Y")}:')
            for event in new_events_content:
                print(event)

            message_content = f'New events data for {current_date.strftime("%b %d, %Y")}:\n```\n' + ''.join([f"{event},\n" for event in new_events_content]) + '```'
            print("Payload to be sent:")
            print(message_content)

            # Sending SMS needs to be fixed
            to_numbers = 'your_phone_number'
            response = send_sms(to_numbers, message_content)

            if 'id' in response:
                print("Event data sent to Sinch successfully.")
            else:
                print(f"Failed to send event data. Response: {response}")

            save_processed_date(current_date)
        else:
            print(f"No event data found on {current_date}.")

    current_date += timedelta(days=1)
    time.sleep(2)

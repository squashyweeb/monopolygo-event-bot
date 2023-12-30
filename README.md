# monopolygo-event-bot

This Python script checks a website for daily events and sends notifications via SMS using Sinch and Discord webhooks. If new events are found, it notifies the user through SMS and Discord webhooks.

## Prerequisites

- Python 3. x
- `requests` library (`pip install requests`)
- `selenium` library (`pip install selenium`)
- `beautifulsoup4` library (`pip install beautifulsoup4`)
- `sinchsms` library (Install instructions can be found [here](https://www.sinch.com/docs/sms/rest/#install))

## Configuration

1. Replace the placeholder values in the script with your actual Sinch service plan ID, Sinch API token, Sinch phone number, Discord webhook URL, and phone number for SMS notifications.
2. Ensure the necessary Python libraries are installed.

## Usage

1. Run the script using the command: `python mgosms.py`.
2. The script will continuously check for new events, sending SMS notifications if any are found.
3. The processed dates are stored in `processed_dates.txt` to avoid duplicate notifications.

## Customization

Feel free to customize the script to suit your needs. You can adjust the main date, change the target website, or modify the notification method.

## License

This project is licensed under me :(

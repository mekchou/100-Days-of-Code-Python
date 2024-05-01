import requests
import smtplib

GMAIL_SMTP = "smtp.gmail.com"
GMAIL_PORT = 587

API_URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "387972c91279254a95ac4d8cbcd7108c"
MY_LAT = 43.653225
MY_LONG = -79.383186
FORECAST_COUNT = 24

with open ("credentials\email.txt") as email:
    my_email = email.readline()

with open ("credentials\pw.txt") as pw:
    my_password = pw.readline()

receiver = "mek.chou@outlook.com"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": FORECAST_COUNT,
}
result_dict = {}
will_rain = False

def check_forecast():
    response = requests.get(API_URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    weather_id_list = [data["list"][n]["weather"][0]["id"] for n in range(FORECAST_COUNT)]
    return weather_id_list

def check_result(weather_id_list):
    global will_rain
    result_dict = {index: item for index, item in enumerate(weather_id_list) if item < 700}
    if len(result_dict) == 0:
        content = "It won't rain in next 3 days"
    else:
        minimum_key = min(result_dict.keys())
        content = f"It'll start raining {(minimum_key + 1) * 3} hours from now"
        will_rain = True
    return content

def send_email(receiver, content):
    with smtplib.SMTP(host=GMAIL_SMTP, port=GMAIL_PORT) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email
            , to_addrs=receiver
            , msg=f"Subject: Weather Forecast\n\n{content}"
        )

def main():
    forecast = check_forecast()
    email_content = check_result(forecast)
    if will_rain:
        send_email(receiver=receiver, content=email_content)
    else:
        print(email_content)

if __name__ == "__main__":
    main()
    



# if any(item < 700 for item in weather_id_list):
    # print("Bring Umbrella")
# else:
    # print("All good")
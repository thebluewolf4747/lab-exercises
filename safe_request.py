import requests
import datetime

""" Exercise 6 """

# url = "https://official-joke-api.appspot.com/random_joke"

# try:
#     # ----------------------------------------
#     # DANGER ZONE: Code that might fail goes here
#     # ----------------------------------------

#     response = requests.get(url, timeout=5) # wait max 5 seconds
#     response.raise_for_status()     # Check for 404/500 errors automatically

#     data = response.json()
#     print(f"Success! The ID of this joke is: {data["id"]}")

# except requests.exceptions.ConnectionError:
#     print("ERROR: No internet connection.")

# except Exception as e:
#     print(f"ERROR: Something went wrong. {e}")

# print("Program finished.")

""" Exercise 7 """
url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true"

try:
    response = requests.get(url, timeout= 5)
    response.raise_for_status()

    data = response.json()
    
    temp = data["current_weather"]["temperature"]
    temp_unit = data["current_weather_units"]["temperature"]
    temp_str = f"{temp}, {temp_unit}"
    
    wind_speed = data["current_weather"]["windspeed"]
    wind_speed_unit = data["current_weather_units"]["windspeed"]
    wind_speed_str = f"{wind_speed}, {wind_speed_unit}"

    if temp < 10:
        print("It's cold, wear a coat.")
    elif temp >= 10:
        print("Nice weather.")
    
    date_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    
    with open(f"Text Files/weather_log_{date_str}.txt", "a") as f:
        f.write(f"{temp_str}\n")
        f.write(f"{wind_speed_str}\n")

except requests.exceptions.ConnectionError:
    print(f"ERROR: No internet connection.")

except Exception as e:
    print(f"ERROR: Something went wrong. {e}")

print("Program finished.")

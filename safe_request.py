""" Exercise 6 """
import requests

url = "https://official-joke-api.appspot.com/random_joke"

try:
    # ----------------------------------------
    # DANGER ZONE: Code that might fail goes here
    # ----------------------------------------

    response = requests.get(url, timeout=5) # wait max 5 seconds
    response.raise_for_status()     # Check for 404/500 errors automatically

    data = response.json()
    print(f"Success! The ID of this joke is: {data["id"]}")

except requests.exceptions.ConnectionError:
    print("ERROR: No internet connection.")

except Exception as e:
    print(f"ERROR: Something went wrong. {e}")

print("Program finished.")

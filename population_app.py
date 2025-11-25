import requests

# 1. Ask the user for input
country = input("Enter a country name (e.g. France, Japan): ")

# 2. Build the specific URL
# We use an f-string to insert the user's choice into the link.
url = f"https://restcountries.com/v3.1/name/{country}"

try:
    # 3. Send the request
    print("Searching for country")
    response = requests.get(url)

    # 4. Check if it worked
    if response.status_code == 200:
        data = response.json()

        # The API returns a list (because 'United' might match 'United Kingdom' and 'United States')
        # We will just take the first result: data[0]
        first_result = data[0]

        # Now dig into the dictionary
        official_name = first_result["name"]["common"]
        pop_count = first_result["population"]
        region = first_result["region"]

        print("-----------------------------")
        print(f"Country: {official_name}")
        print(f"Region: {region}")
        print(f"Population: {pop_count:,}")
        print("-----------------------------")
        
        
    else:
        print("Error: Country not found or connection failed.")

    with open("Text Files/search_history.txt", "a") as f:
        text_str = f"{official_name}: {pop_count:,}\n"
        f.write(text_str)

except requests.exceptions.HTTPError:
    print(f"Sorry, we couldn't find a country named {country}. Check your spelling.")

except requests.exceptions.ConnectionError:
    print("ERROR: No connection!")

except Exception as e:
    print("An unexpected error occurred. {e}")



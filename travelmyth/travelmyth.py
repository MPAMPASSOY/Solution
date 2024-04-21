import json
import requests
import os
import openai


response = openai.ChatCompletion.create(
  engine="gpt-35-turbo", # replace this value with the deployment name you chose when you deployed the associated model.
  messages = [{"role":"system","content":"You are an travel agency customer support agent whose primary goal is to help users with their filters. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to the filters."},{"role":"user","content":"What countries are in Europe?"},{"role":"assistant","content":"I apologize, but I do not have information about the prices of other gaming devices such as the PS5. My primary focus is to assist with issues regarding Xbox devices. Is there a specific issue you are having with your Xbox device that I may be able to help with?"},{"role":"user","content":"I am interested in buying an Xbox?"},{"role":"assistant","content":"Great! There are several Xbox models available in the market, including the Xbox Series X, Xbox Series S, and Xbox One. The Xbox Series X is the latest and most powerful console, while the Xbox Series S is a more affordable option that still offers great performance. The Xbox One is the previous generation console, but it still has a large library of games available to play.\n\nBefore purchasing an Xbox, you may want to consider factors such as your budget, the types of games you want to play, and whether you want to play games in 4K resolution. Once you have decided on a console, you can purchase it from a retailer or directly from the Xbox website. Let me know if you have any other questions or concerns!"},{"role":"user","content":"Which models are 4K?"},{"role":"assistant","content":"Both the Xbox Series X and Xbox One X support 4K resolution gaming. The Xbox Series S, on the other hand, supports up to 1440p resolution gaming, but it can upscale games to 4K. It's worth noting that in order to take advantage of 4K gaming, you'll need a 4K TV or monitor that supports HDR (High Dynamic Range) and HDMI 2.0 or higher."}],
  temperature=0,
  max_tokens=350,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

openai.api_type = "azure"
openai.api_base = "https://docs-test-001.openai.azure.com/"
openai.api_version = "2024-02-01"
openai.api_key = os.getenv("OPENAI_API_KEY")
#User's Search
url = "https://www.travelmyth.gr/api_chat_makeathon.php"
params = {
    "destination": "austria",
    "lang": "en",
    "categories": "ski,luxury",
    "apiKey": "myTeam",
    "weather": "snowy"
}
headers = {"content-type": "application/json"}

# Load data from JSON file
with open('hotels.json', 'r') as file:
    hotels = json.load(file)
thecategories = {"categories": [
    "infinity_pool",
    "heated_pool",
    "indoor_pool",
    "rooftop_pool",
    "wave_pool",
    "children_pool",
    "panoramic_view_pool",
    "pool_swim_up_bar",
    "pool_water_slide",
    "pool_lap_lanes",
    "water_park",
    "lazy_river",
    "private_pool",
    "dog_play_area",
    "dog_sitting",
    "dogs_stay_free",
    "outdoor_pool",
    "health_and_safety",
    "treehouse",
    "haunted",
    "overwater_bungalows",
    "three_star",
    "skyscraper",
    "four_star",
    "five_star",
    "yoga",
    "tennis",
    "small",
    "adult_only",
    "gym",
    "accessible",
    "cheap",
    "parking",
    "business",
    "free_wifi",
    "pool",
    "nightlife",
    "romantic",
    "dog_friendly",
    "family",
    "spa",
    "casino",
    "honeymoon",
    "eco_friendly",
    "beach",
    "beachfront",
    "ski",
    "ski_in_ski_out",
    "historic",
    "unusual",
    "vineyard",
    "monastery",
    "castle",
    "golf",
    "luxury",
    "boutique",
    "ev_charging",
    "jacuzzi_hot_tub",
    "fireplace",
    "all_inclusive",
    "sunny",
    "cloudy",
    "partly cloudy",
    "rainy",
    "stormy",
    "snowy",
    "foggy",
    "windy",
    "hazy",
    "misty"
]
}
weather = {"weather": ["sunny",
                       "cloudy",
                       "partly cloudy",
                       "rainy",
                       "stormy",
                       "snowy",
                       "foggy",
                       "windy",
                       "hazy",
                       "misty"]
           }
# Separate data into categories
category1_data = hotels['country_name']
category2_data = hotels['country_code']
category3_data = hotels['categories']
category4_data = hotels['apiKey']
category5_data = hotels['weather']


# Category Deletion
if category5_data == 'ski':
    weather_temp = []
    if weather_temp == 'snowy':
        weather_temp = {"weather": ["snowy"]}
###################################################################################
print("Category 1 Data:")
for item in category1_data:
    print(item)

print("\nCategory 2 Data:")
for item in category2_data:
    print(item)


response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Process the JSON data here
else:

    print("Error:", response.status_code)

# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
api_key = '50248ae2f8f46469417519997a737c9a'

# The city is the destination of travelmyth
city = 'params=params.destination'

# API endpoint URL
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# Send GET request to the API
response = requests.get(url)

# Check if request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    # Extract relevant weather information
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']

    # Print the weather information
    print(f'Temperature: {temperature} K')
    print(f'Humidity: {humidity}%')
    print(f'Weather Description: {weather_description}')
else:
    print('Failed to retrieve weather data')

# URL for the API endpoint
url = "https://api.openai.com/v1/chat/completions"

# Headers including the Content-Type and Authorization with the Bearer token
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

# JSON payload to be sent with the request
data = {
    "model": "gpt-3.5-turbo-0125",
    "temperature": 0,
    "top_p": 1,
    "max_tokens": 1200,
    "n": 1,
    "messages": [{"role": "user", "content": "Hello, how are you?"}]
}

# Making the POST request
response = requests.post(url, headers=headers, json=data)

# Printing the response text (or you can handle it as needed)
print(response.text)

def fetch_data_from_api(url, headers=None):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Example API endpoint
url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m'

# Example authentication headers (if required)
headers = {'Authorization': 'Bearer YOUR_API_KEY'}

# Fetch data from the API
api_data = fetch_data_from_api(url, headers)

if api_data:
    # Save data to JSON file
    save_to_json(api_data, 'api_data.json')
    print("Data saved to api_data.json")
else:
    print("Failed to fetch data from the API")



# tha traviksoyme ta dedomena apo ta weather api's.Tha paroyme kai ta dedomena apo to site toy travelmyth.Tha
# prosthesoyme cookies  gia na ginei kalytera h taksinomisi tha orisoyme kai mia eksarthmenes pithanotites gia
# kapoies drasthriotites

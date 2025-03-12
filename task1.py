import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Your OpenWeather API key
API_KEY = '33bada5fc0173bd5a4c2fc2c0be5faf5'
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
CITY = "London"  # You can change this to any city you want

# Function to fetch weather data from OpenWeather API
def get_weather_data(city, api_key):
    # API parameters
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # Get temperature in Celsius
    }
    
    try:
        # Make API request
        response = requests.get(BASE_URL, params=params)
        
        # Check for errors in the request
        if response.status_code != 200:
            print(f"Error: Unable to fetch data. HTTP Status Code: {response.status_code}")
            print(response.json())  # Print the error message returned by OpenWeather
            return None
        
        # Parse response JSON
        data = response.json()
        
        # Extract relevant data from the response
        weather_data = {
            "City": city,
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Pressure": data["main"]["pressure"],
            "Weather": data["weather"][0]["description"],
            "Wind Speed": data["wind"]["speed"]
        }
        return weather_data
    except Exception as e:
        print(f"Error: {e}")
        return None

# Fetch the weather data for the city
weather_data = get_weather_data(CITY, API_KEY)

if weather_data:
    # Create a pandas DataFrame to store the weather data
    df = pd.DataFrame([weather_data])

    # Print the DataFrame (optional step to see the data)
    print(df)

    # Visualize the weather data using matplotlib and seaborn
    plt.figure(figsize=(10, 6))

    # Set Seaborn style for cleaner plots
    sns.set(style="whitegrid")

    # Create a bar plot for Temperature, Humidity, and Wind Speed
    data_for_plot = df[['Temperature', 'Humidity', 'Wind Speed']]
    data_for_plot.plot(kind='bar', ax=plt.gca())

    # Title and labels
    plt.title(f"Weather Data for {CITY}")
    plt.ylabel("Values")
    plt.xlabel("Attributes")
    plt.xticks([0], [CITY], rotation=0)  # Display city as x-axis label

    # Show the plot
    plt.show()

else:
    print("No data fetched due to errors.")

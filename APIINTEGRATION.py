import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


API_KEY = "2f7495ab73384df82e764a62ac8a5e93"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant weather data
        weather_info = {
            'City': city,
            'Temperature (C)': data['main']['temp'],
            'Humidity (%)': data['main']['humidity'],
            'Wind Speed (m/s)': data['wind']['speed']
        }
        return weather_info
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Function to visualize the data
def visualize_weather_data(weather_data):
    df = pd.DataFrame(weather_data)

    # Set up the seaborn style
    sns.set(style="whitegrid")
    
    # Create subplots to visualize multiple parameters
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    
    # Temperature Plot
    sns.barplot(x='City', y='Temperature (C)', data=df, ax=ax[0], palette="coolwarm")
    ax[0].set_title('Temperature (°C)')
    
    # Humidity Plot
    sns.barplot(x='City', y='Humidity (%)', data=df, ax=ax[1], palette="Blues")
    ax[1].set_title('Humidity (%)')
    
    # Wind Speed Plot
    sns.barplot(x='City', y='Wind Speed (m/s)', data=df, ax=ax[2], palette="viridis")
    ax[2].set_title('Wind Speed (m/s)')
    
    plt.tight_layout()
    plt.show()

# Main function
def main():
    # List of cities to fetch weather data for
    cities = ['London', 'New York', 'Tokyo', 'Mumbai', 'Sydney']

    weather_data = []

    # Fetch data for each city
    for city in cities:
        data = get_weather_data(city)
        if data:
            weather_data.append(data)

    # Visualize the collected weather data
    if weather_data:
        visualize_weather_data(weather_data)


if __name__ == "__main__":
    main()

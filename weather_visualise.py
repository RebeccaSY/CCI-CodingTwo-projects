import requests
import matplotlib.pyplot as plt
import math

import time
from matplotlib.colors import LinearSegmentedColormap 

def temperature_bar():
    # My OpenWeatherMap API key 
    api_key = "3905fbad650e10ba349d5e6707db4ad7"

    # Top 5 cities with the largest population in each country are chosen
    # Source from https://worldpopulationreview.com/world-cities
    # This is not really flexible, it could be improved

    # linking city with country is necessary for extracting data
    cities = {
        "UK": ["London", "Birmingham", "Glasgow", "Liverpool", "Leeds"],
        "France": ["Paris", "Marseille", "Lyon", "Toulouse", "Nice"],
        "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"],
        "Germany": ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt"]
    }

    # Part of URL for the request
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = "http://api.openweathermap.org/data/2.5/weather"

    # To be dynamic? 
    #while(1):

    # plot of 2*2
    fig,axs = plt.subplots(2, 2, figsize=(9, 6), sharey=True)
    # fig.set_facecolor('#a0605040')


    # For each country, each city, extract the current temperature data
    temperatures = {}
    places = {}
    k = 0   # iteration count of loop

    for country, country_cities in cities.items():
        country_temperatures = []
        country_places = []
        
        for city in country_cities:
            # change the url to request data for each item
            para = {"q": city + "," + country, "units": "metric", "appid": api_key}
            response = requests.get(url, params = para)
            
            data = response.json()
            #print(data)
            temperature = data['main']['temp']
            country_temperatures.append(temperature)
            country_places.append(city)

        temperatures[country] = country_temperatures
        places[country] = country_places
        
        
        # Plot the temperature

        # Set colours based on temperature: the higher temperature, the warmer colour
        my_colourmap = LinearSegmentedColormap.from_list("", ["#476ADD","#FFA7B4","#FFA447"])
        #min_temperature = min(country_temperatures)
        #max_temperature = max(country_temperatures)
        my_colours = []
        for i in country_temperatures:
            my_colours.append(my_colourmap((i + 1) / 37))   # this could be modified to be more flexible


        #plt.figure(figsize=(26,16)) 
        row = k // 2    # to determine where we are on this 2*2 figure
        column = k % 2
        axs[row, column].bar(places[country], country_temperatures, width=0.4, color=my_colours)
        axs[row, column].set_title("Temperature of the Cities in " + country, fontsize=11)
        axs[row, column].set_xlabel("City")
        axs[row, column].set_ylabel("Temperature (Celsius)") 
        axs[row, column].set_ylim(0.00, +38.00)
        axs[row, column].spines['right'].set_visible(False)
        axs[row, column].spines['top'].set_visible(False)

        # Add values on top of bars
        for x,y in zip(country_cities, country_temperatures):
            axs[row, column].text(x, y, '%.2f'%y, ha='center', va='bottom', fontsize=7)
        
        for item in (axs[row, column].get_xticklabels() + axs[row, column].get_yticklabels()):
            item.set_fontsize(7)
        
        for item in (axs[row, column].xaxis.label, axs[row, column].yaxis.label):
            item.set_fontsize(9)
        
        k = k + 1



    fig.suptitle("Real-Time Temperature of Cities with Largest Population in four countries", fontsize=15)
    fig.tight_layout()

    plt.show()

    #time.sleep(3)

temperature_bar()
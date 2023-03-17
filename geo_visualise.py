import requests
import matplotlib.pyplot as plt
import numpy as np

from adjustText import adjust_text
from matplotlib.colors import LinearSegmentedColormap 

import functools
import os

from matplotlib import gridspec
import tensorflow as tf
import tensorflow_hub as hub

# This function from https://github.com/ual-cci/MSc-Coding-2/blob/master/Week-7-notebooks/tf2_arbitrary_image_stylization.ipynb
def load_image(image_url, image_size=(256, 256), preserve_aspect_ratio=True):
    """Loads and preprocesses images."""
    # Cache image file locally.
    image_path = tf.keras.utils.get_file(os.path.basename(image_url)[-128:], image_url)
    # Load and convert to float32 numpy array, add batch dimension, and normalize to range [0, 1].
    img = plt.imread(image_path).astype(np.float32)[np.newaxis, ...]
    if img.max() > 1.0:
        img = img / 255.
    if len(img.shape) == 3:
        img = tf.stack([img, img, img], axis=-1)
    shape = img.shape
    new_shape = min(shape[1], shape[2])
    offset_y = max(shape[1] - shape[2], 0) // 2
    offset_x = max(shape[2] - shape[1], 0) // 2
    imge = tf.image.crop_to_bounding_box(
        img, offset_y, offset_x, new_shape, new_shape)
    img = tf.image.resize(img, image_size, preserve_aspect_ratio=True)
    return img

def scatter_map():

    # My OpenWeatherMap API key 
    api_key = "3905fbad650e10ba349d5e6707db4ad7"

    # The top 40 cities of largest population in the world are chosen
    # Source from https://worldpopulationreview.com/world-cities
    cities = ["Tokyo", "Delhi", "Shanghai", "Dhaka", "São Paulo", "Mexico City", "Cairo", "Beijing", "Mumbai", "Osaka", 
            "Chongqing", "Karachi", "Kinshasa", "Lagos", "Istanbul", "Buenos Aires", "Kolkata", "Manila", "Guangzhou",
            "Tianjin", "Lahore", "Rio De Janeiro", "Bangalore", "Shenzhen", "Moscow", "Chennai", "Bogota", "Jakarta", 
            "Paris", "Lima", "Bangkok", "Hyderabad", "Seoul", "Nanjing", "Chengdu", "London", "Nagoya", "Tehran", "Ho Chi Minh City", "Luanda"]
        # It can be modified to be flexible

    # Part of URL for the request
    url = "https://api.openweathermap.org/data/2.5/weather"


    temperatures = []
    latitudes = []
    longitudes = []
    labels = []

    # Loop through each city to get the temperature, latitude, and longitude
    for city in cities:
        # determine the para of request
        para = {"q": city, "units": "metric", "appid": api_key}

        # use the complete request to get data
        response = requests.get(url, params=para)
        data = response.json()
        #print(data)

        # Store the required temperature, latitude, and longitude from json data
        temperature = data["main"]["temp"]
        latitude = data["coord"]["lat"]
        longitude = data["coord"]["lon"]
        
        temperatures.append(temperature)
        latitudes.append(latitude)
        longitudes.append(longitude)

        labels.append(city)


    # Scatter plot, with X-axis being longitudes and Y-axis being latitudes
    my_colourmap = LinearSegmentedColormap.from_list("", ["#476ADD","#FFA7B4","#FFA447"])
    plt.figure(figsize=(26, 8))
    scatter = plt.scatter(longitudes, latitudes, c=temperatures, cmap=my_colourmap, alpha=0.85)

    plt.title("Real-time Temperature of the World's 40 Cities with Largest Population")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.xlim(-180,180)  # make it look more like on world map
    plt.ylim(-90,90)

    # Add labels for cities
    texts = []
    for i, label in enumerate(labels):
        x = longitudes[i]
        y = latitudes[i]
        texts.append(plt.text(x, y, label, fontsize=5))
        plt.plot([x, x], [y, y], color=scatter.to_rgba(temperatures[i]), alpha=0.6, linewidth=0.5)
    adjust_text(texts, arrowprops = dict(arrowstyle="-", color='k', lw=0.5))      # avoid overlap

    # Add the color bar
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=7)
    cb.set_label('Temperature (Celsius)', fontsize=9)
    cb.outline.set_visible(False)

    # Add a image of world map as background
    # Source: https://en.wikipedia.org/wiki/File:World_location_map_(equirectangular_180).svg    
    curr_image = plt.imread('images/world_map.png')
    
    '''
    # ---------------------------------------------------------------------------------------------------
    # The following section took reference from https://github.com/ual-cci/MSc-Coding-2/blob/master/Week-7-notebooks/tf2_arbitrary_image_stylization.ipynb
    
    # The style of Auguste Renoir is used here
    style_image_url = 'https://upload.wikimedia.org/wikipedia/commons/e/e8/Villeneuve_les_Avignon_%281901%29_-_Auguste_Renoir.jpg'

    #content_image = load_image(content_image_url, (900, 500))
    content_img = plt.imread('images/world_map.png').astype(np.float32)[np.newaxis, ...]
    if content_img.max() > 1.0:
        content_img = content_img / 255.
    if len(content_img.shape) == 3:
        content_img = tf.stack([content_img, content_img, content_img], axis=-1)
      
    style_image = load_image(style_image_url, (256, 256))
    
    style_image = tf.nn.avg_pool(style_image, ksize=[3,3], strides=[1,1], padding='SAME')
    
    # Load TF-Hub module.
    hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
    hub_module = hub.load(hub_handle)

    # Stylize content image with given style image.
    # This is pretty fast within a few milliseconds on a GPU.

    outputs = hub_module(tf.constant(curr_image), tf.constant(style_image))
    stylized_image = outputs[0]
    
    # ---------------------------------------------------------------------------------------------------
    
    plt.imshow(stylized_image, extent=[-180, 180, -90, 90], aspect='auto', alpha=0.5)
'''

    plt.imshow(curr_image, extent=[-180, 180, -90, 90], aspect='auto', alpha=0.5)

    # The spines don't look good here, remove them
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)

    #plt.xticks([])
    #plt.yticks([])

    plt.xticks([-180, -120, -60, 0, 60, 120, 180], fontsize=8)
    plt.yticks([-90, -60, -30, 0, 30, 60, 90], fontsize=8)

    plt.show()

scatter_map()
import os

from geo_visualise import scatter_map
from weather_visualise import temperature_bar

# The style of Auguste Renoir - Villeneuve_les_Avignon is used here
style_image_url = 'https://upload.wikimedia.org/wikipedia/commons/e/e8/Villeneuve_les_Avignon_%281901%29_-_Auguste_Renoir.jpg'
scatter_map(style_image_url)

# The style of Monet - Impression SUnrise is used here
style_image_url = 'https://upload.wikimedia.org/wikipedia/commons/5/59/Monet_-_Impression%2C_Sunrise.jpg'
scatter_map(style_image_url)

# The style of Juan Gris - Portrait of Pablo Picasso is used here
style_image_url = 'https://upload.wikimedia.org/wikipedia/commons/1/18/Juan_Gris_-_Portrait_of_Pablo_Picasso_-_Google_Art_Project.jpg'
scatter_map(style_image_url)

temperature_bar()

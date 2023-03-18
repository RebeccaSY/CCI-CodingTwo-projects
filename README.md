# CCI-CodingTwo-projects
This Project requests real-time data from the web as input, generates plots to visualise data. I combined the content from Coding Two with my previous data analysis experience.  

There are two main functions in this project. They both take real-time data from OpenWeatherMap with API key, request real-time weather data by city names, then visualise the data on figures.  

The geo_visualise.py takes real-time temperatrue data of 40 most populas cities around the world and uses a scatter plot to visulise them. The scaterplot uses longitude as X-axis and latitude as Y-axis, similar as the illustartion of a world map. The background is a world map image, which can be stylised by customised art style (Refer to https://github.com/ual-cci/MSc-Coding-2/blob/master/Week-7-notebooks/tf2_arbitrary_image_stylization.ipynb). The scatters visualise the real-time temperature of the exact cities on Earth. The colour of the scatter is determined by a customised colour map, where higher temperatures are represented by warmer colors and lower temperatures by cooler colors.  

![Image text](https://github.com/RebeccaSY/CCI-CodingTwo-projects/blob/main/images/output1.png)  

**The following figures have background image stylised with artworks from online resources**  

Stylisation with Auguste Renoir - Villeneuve_les_Avignon:  
![Image text](https://github.com/RebeccaSY/CCI-CodingTwo-projects/blob/main/images/output1b.png)  

Stylisation with Monet - Impression Sunrise:  
![Image text](https://github.com/RebeccaSY/CCI-CodingTwo-projects/blob/main/images/output1c.png)  

Stylisation with Juan Gris - Portrait of Pablo Picasso:  
![Image text](https://github.com/RebeccaSY/CCI-CodingTwo-projects/blob/main/images/output1d.png)  

The weather_visualise.py creates bar chart of the top 5 populas cities from four countries. The data source is also real-time data extracted from OpenWeatherMap. The colour of tha bar is determined by the temperature value. The graphs are modified in a more clear way, with unnecessary outlines removed.  

![Image text](https://github.com/RebeccaSY/CCI-CodingTwo-projects/blob/main/images/output2.png)  

This project can be further improved as a data pipeline, taking input on selection of cities and generating visualisation. 

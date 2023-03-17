# CCI-CodingTwo-projects
This Project requests real-time data from the web as input, generates plots to visulise data.  
.  
There are two main functions in this project. They both take input from OpenWeatherMap with API key, request real-time weather data by city names, then visualise the data on plots.  
.  
The geo_visualise.py takes real-time temperatrue data of 40 most populas cities around the world and uses a scatter plot to visulise them. The scaterplot uses longitude as X-axis and latitude as Y-axis, similar as the illustartion of a world map. The background is a world map image. The scatters visualise the real-time temperature of the exact cities on Earth. The colour of the scatter is determined by a customised colour map, where higher temperatures are represented by warmer colors and lower temperatures by cooler colors.  
.  
The weather_visualise.py creates bar chart of the top 5 populas cities from four countries. The data source is also real-time data extracted from OpenWeatherMap. The colour of tha bar is determined by the temperature value. The graphs are modified in a more clear way, with unnecessary outlines removed.  
.  
This project can be further improved as a data pipeline, taking input on selection of cities and generating visualisation. 

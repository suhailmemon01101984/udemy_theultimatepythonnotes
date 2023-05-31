In this example, we're using the requests library to make a GET request to the OpenWeatherMap API. You'll need to replace YOUR_API_KEY_HERE with your actual API key, 
which you can obtain by signing up for a free account on the OpenWeatherMap website.

We're also specifying the city we want to fetch weather data for (in this case, New York), as well as the units we want the data to be returned in (imperial).


If the API request is successful (i.e. the response status code is 200), we extract the relevant weather data (temperature, humidity, and description) from the JSON response and print it to the console.
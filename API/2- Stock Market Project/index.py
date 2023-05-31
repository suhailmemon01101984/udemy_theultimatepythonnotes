import requests
import pandas as pd
import matplotlib.pyplot as plt

# Define the API endpoint and parameters
api_endpoint = 'https://www.alphavantage.co/query'
params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': 'AAPL',
    'apikey': 'YOUR_API_KEY_HERE'
}

# Send the request to the API
response = requests.get(api_endpoint, params=params)

# Parse the JSON response and convert it to a Pandas DataFrame
data = pd.DataFrame.from_dict(response.json()['Time Series (Daily)'], orient='index')
data = data.astype(float)

# Plot the closing prices
plt.plot(data['4. close'])
plt.title('AAPL Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

import requests
import pandas as pd
import matplotlib.pyplot as plt

function="TIME_SERIES_DAILY_ADJUSTED"
symbol="AAPL"
apikey="80QMYFRTXCVPRYBK_suhail"

# Define the API endpoint and parameters
api_url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={apikey}'

# Send the request to the API
response = requests.get(api_url)

print(response.json())



# Parse the JSON response and convert it to a Pandas DataFrame
data = pd.DataFrame.from_dict(response.json()['Time Series (Daily)'], orient='index')
data = data.astype(float)

# Plot the closing prices
plt.plot(data['4. close'])
plt.title('AAPL Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

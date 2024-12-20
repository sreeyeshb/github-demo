import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


# List of stock symbols (example)
stocks = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS']

# Fetching data
data = yf.download(stocks, start='2024-01-01', end='2024-12-01')

# Selecting 'Close' price
daily_returns = data['Close'].pct_change()

# Calculating cumulative returns
cumulative_returns = (1 + daily_returns).cumprod() - 1

# Plot cumulative returns
cumulative_returns.plot(figsize=(10, 5))
plt.title('Cumulative Returns of Portfolio')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.show()





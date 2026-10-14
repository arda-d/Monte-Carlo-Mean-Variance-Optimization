import numpy as np
import pandas as pd
import data_loader as sd

# sd.download_stock_data()

# Load historical prices from local storage
data = pd.read_csv("stocks_prices.csv", index_col=0, parse_dates=True)

# Compute daily percentage changes and drop missing values
daily_changes = data.pct_change().ffill().dropna()

# Annualize expected returns and covariance matrix (252 trading days)
portfolio_data = daily_changes[sd.stocks]
yearly_return = portfolio_data.mean() * 252
yearly_covariance = portfolio_data.cov() * 252

# Calculate annualized return and risk for the benchmark index
bist_return = daily_changes[sd.benchmark].mean() * 252
bist_risk = daily_changes[sd.benchmark].std() * np.sqrt(252)
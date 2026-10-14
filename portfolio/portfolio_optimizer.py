import numpy as np
import data_processor as rc
import data_loader as sd
from numpy import random as rnd

# Simulation parameters
numberOf_Portfolios = 100000
risk_free_rate = 0.39
stock_number = len(sd.stocks)

# Set seed for reproducible results
rnd.seed(257)

# Generate random portfolio weights normalized to sum up to 1
weights = rnd.random((numberOf_Portfolios, stock_number))
weights /= np.sum(weights, axis=1, keepdims=True)

# Calculate annual return and risk metrics via matrix multiplication
portfolio_Return = np.dot(weights, rc.yearly_return)

# Calculate the annual risk for every portfolio using the covariance matrix
portfolio_Risk = np.sqrt(
    np.sum(np.dot(weights, rc.yearly_covariance) * weights, axis=1)
)

# Compute Sharpe ratio for each portfolio
rate = (portfolio_Return - risk_free_rate) / portfolio_Risk

# Identify Optimal Portfolio (Max Sharpe Ratio)
best_index = np.argmax(rate)
opt_return = portfolio_Return[best_index]
opt_risk = portfolio_Risk[best_index]
opt_weights = weights[best_index]

# Identify Minimum Risk Portfolio (Min Volatility)
min_risk_index = np.argmin(portfolio_Risk)
min_risk_return = portfolio_Return[min_risk_index]
min_risk_val = portfolio_Risk[min_risk_index]
min_risk_weights = weights[min_risk_index]
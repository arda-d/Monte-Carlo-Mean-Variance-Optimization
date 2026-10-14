import os
import yfinance as yf

# Target assets and benchmark definition
stocks = [
    "THYAO.IS", "GARAN.IS", "KCHOL.IS", "ASELS.IS", "TUPRS.IS",
    "AKBNK.IS", "SAHOL.IS", "EREGL.IS", "SISE.IS", "FROTO.IS",
    "BIMAS.IS", "TCELL.IS", "ISCTR.IS", "PGSUS.IS", "MGROS.IS"
]
benchmark = "XU100.IS"
all_stocks = stocks + [benchmark]

# Fetch historical data if local CSV is missing
if not os.path.exists("stocks_prices.csv"):
  data = yf.download(all_stocks, start="2024-10-1", end="2026-10-1")["Close"]
  try:
    data.to_csv("stocks_prices.csv")
    print("The CSV file has been created successfully.")
  except:
    print("An error occurred while downloading the stock prices.")
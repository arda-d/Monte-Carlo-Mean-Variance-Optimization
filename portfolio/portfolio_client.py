import os
import requests
import pandas as pd
import yfinance as yf
import data_loader as dl
import portfolio_optimizer as mc


class PortfolioClient:
    def __init__(self, base_url="http://localhost:8080/api"):
        self.base_url = base_url
        self.stocks = dl.stocks
        self.benchmark = dl.benchmark
        self.all_stocks = dl.all_stocks

    def fetch(self, filename="stocks_prices.csv"):
        if not os.path.exists(filename):
            data = yf.download(self.all_stocks, start="2024-10-1", end="2026-10-1")["Close"]
            try:
                data.to_csv(filename)
                print("The CSV file has been created successfully.")
            except Exception as e:
                print(f"An error occurred while downloading stock prices: {e}")

    def sync(self, total_capital=100000.0):
        if not os.path.exists("stocks_prices.csv"):
            print("stocks_prices.csv cannot be found, please download it first!.")
            return

        df = pd.read_csv("stocks_prices.csv", index_col=0, parse_dates=True)

        initial_prices = df[self.stocks].iloc[0]
        latest_prices = df[self.stocks].iloc[-1]

        portfolio_payload = []
        for i, stock in enumerate(self.stocks):
            weight = mc.opt_weights[i]
            init_price = initial_prices[stock]
            curr_price = latest_prices[stock]

            allocated_money = total_capital * weight
            quantity = allocated_money / init_price

            portfolio_payload.append({
                "assetName": stock,
                "quantity": round(quantity, 2),
                "purchasePrice": round(float(init_price), 2),
                "currentPrice": round(float(curr_price), 2),  # YENİ: Güncel fiyat
                "purchaseDate": "2024-10-01"
            })

        print("Sending optimized portfolio data with current prices to Spring Boot...")
        try:
            response = requests.post(f"{self.base_url}/assets/batch", json=portfolio_payload)
            if response.status_code == 200:
                print("Portfolio successfully synced with Spring Boot!")
            else:
                print(f"Failed to sync. Status code: {response.status_code}, Response: {response.text}")
        except Exception as e:
            print(f"Connection error: {e}")

    def get_summary(self):
        print("\nFetching portfolio summary from backend...")
        try:
            response = requests.get(f"{self.base_url}/portfolio/summary")
            if response.status_code == 200:
                data = response.json()
                print("--- Portfolio Summary & Performance ---")
                print(f"Total Initial Cost: {data['totalPurchaseValue']:,.2f} TL")
                print(f"Total Current Value: {data['totalCurrentValue']:,.2f} TL")

                pl = data['totalProfitLoss']
                pl_pct = data['profitLossPercentage']
                print(f"Total Profit/Loss: {pl:+,.2f} TL (%{pl_pct:+.2f})")
                print(f"Total Asset Types: {data['totalAssetCount']}")
            else:
                print(f"Could not fetch summary. Status code: {response.status_code}")
        except Exception as e:
            print(f"Connection error: {e}")

if __name__ == "__main__":
    client = PortfolioClient()
    client.fetch()
    client.sync(total_capital=100000.0)
    client.get_summary()
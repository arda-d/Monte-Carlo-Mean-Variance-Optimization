import data_loader
import data_processor
import portfolio_optimizer
import analytics_report
import visualizer
from portfolio_client import PortfolioClient

if __name__ == "__main__":
  print("Running optimization and generating reports...")

  client = PortfolioClient()
  client.fetch()
  client.sync(total_capital=100000.0)
  client.get_summary()
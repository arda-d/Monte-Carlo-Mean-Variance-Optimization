import matplotlib.pyplot as plt
import portfolio_optimizer as mc
import data_processor as rc
import data_loader as sd
import numpy as np
plt.figure(figsize=(10, 8))

# Plot simulated portfolios mapped by Sharpe Ratio
plt.scatter(
    mc.portfolio_Risk,
    mc.portfolio_Return,
    c=mc.rate,
    cmap="viridis",
    marker="o",
    s=10,
    alpha=0.7,
)
plt.colorbar(label="Sharpe Ratio")

# Highlight Optimal Portfolio (Max Sharpe)
plt.scatter(
    mc.opt_risk,
    mc.opt_return,
    color="red",
    marker="v",
    s=200,
    edgecolors="black",
    label="Optimal Portfolio Value/Max Sharpe Ratio",
)
# Highlight Minimum Risk Portfolio
plt.scatter(
    mc.min_risk_val,
    mc.min_risk_return,
    color="lime",
    marker="^",
    s=175,
    edgecolors="black",
    label="Minimum Risk Portfolio",
)

# Plot BIST 100 Benchmark reference point
plt.scatter(
    rc.bist_risk,
    rc.bist_return,
    color="blue",
    marker="s",
    s=150,
    label="BIST 100 (Benchmark)",
)

# Plot individual assets for comparison
for i, stock in enumerate(sd.stocks):
  stock_risk = np.sqrt(rc.yearly_covariance.iloc[i, i])
  stock_income = rc.yearly_return.iloc[i]
  plt.scatter(stock_risk, stock_income, marker="o", s=35, edgecolors="black")
  plt.annotate(
      stock,
      (stock_risk, stock_income),
      textcoords="offset points",
      xytext=(0, 10),
      ha="center",
      fontsize=7,
      fontweight="bold",
  )


plt.title("Monte-Carlo Simulation Results with Benchmark", fontsize=12, fontweight="bold")
plt.xlabel("Yearly Risk", fontsize=10)
plt.ylabel("Expected Yearly Return", fontsize=10)
plt.legend(loc="upper left", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

plt.savefig("portfolio_report.png", dpi=300)
print("Portfolio visualization saved as 'portfolio_report.png'.")
plt.show()
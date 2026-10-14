import portfolio_optimizer as mc
import data_processor as rc
import data_loader as sd

print("\n" + "="*50)
print(f"{'Portfolio Optimization Report':^50}")
print("="*50)
print(
    f"BIST 100(BenchMark): Risk = %{rc.bist_risk * 100:.2f}   |"
    f"Return = %{rc.bist_return * 100:.2f}"
)
print(
    f"Minimum Risk Portfolio: Risk = %{mc.min_risk_val * 100:.2f} |"
    f"Return = %{mc.min_risk_return * 100:.2f}"
)

print(
    f"Optimal Portfolio: Risk = %{mc.opt_risk * 100:.2f}    |"
    f"Return = %{mc.opt_return * 100:.2f}"
)

print("\n" + "-"*50)
print("For Optimized Portfolio:")
for stock, weight in zip(sd.stocks, mc.opt_weights):
  print(f"    • {stock:<10} : %{weight*100:.2f}")
print("-" * 50 + "\n")
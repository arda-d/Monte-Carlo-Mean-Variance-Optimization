package com.financial.portfolio.dto;

public class PortfolioSummaryResponse {
    private int totalAssetCount;
    private double totalPurchaseValue;
    private double totalCurrentValue;
    private double totalProfitLoss;
    private double profitLossPercentage;

    public PortfolioSummaryResponse(int totalAssetCount, double totalPurchaseValue, double totalCurrentValue, double totalProfitLoss, double profitLossPercentage) {
        this.totalAssetCount = totalAssetCount;
        this.totalPurchaseValue = totalPurchaseValue;
        this.totalCurrentValue = totalCurrentValue;
        this.totalProfitLoss = totalProfitLoss;
        this.profitLossPercentage = profitLossPercentage;
    }

    // Getters
    public int getTotalAssetCount() { return totalAssetCount; }
    public double getTotalPurchaseValue() { return totalPurchaseValue; }
    public double getTotalCurrentValue() { return totalCurrentValue; }
    public double getTotalProfitLoss() { return totalProfitLoss; }
    public double getProfitLossPercentage() { return profitLossPercentage; }
}
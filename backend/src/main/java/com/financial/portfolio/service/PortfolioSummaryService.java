package com.financial.portfolio.service;

import com.financial.portfolio.dto.PortfolioSummaryResponse;
import com.financial.portfolio.model.Asset;
import com.financial.portfolio.repository.AssetRepository;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class PortfolioSummaryService {

    private final AssetRepository assetRepository;

    public PortfolioSummaryService(AssetRepository assetRepository) {
        this.assetRepository = assetRepository;
    }

    public PortfolioSummaryResponse getPortfolioSummary() {
        List<Asset> assets = assetRepository.findAll();

        double totalPurchaseValue = 0.0;
        double totalCurrentValue = 0.0;

        for (Asset asset : assets) {
            totalPurchaseValue += asset.getQuantity() * asset.getPurchasePrice();
            double currPrice = asset.getCurrentPrice() > 0 ? asset.getCurrentPrice() : asset.getPurchasePrice();
            totalCurrentValue += asset.getQuantity() * currPrice;
        }

        double totalProfitLoss = totalCurrentValue - totalPurchaseValue;
        double profitLossPercentage = totalPurchaseValue > 0 ? (totalProfitLoss / totalPurchaseValue) * 100 : 0.0;

        return new PortfolioSummaryResponse(
                assets.size(),
                totalPurchaseValue,
                totalCurrentValue,
                totalProfitLoss,
                profitLossPercentage
        );
    }
}
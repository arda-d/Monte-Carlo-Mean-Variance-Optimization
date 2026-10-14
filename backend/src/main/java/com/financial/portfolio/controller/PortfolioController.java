package com.financial.portfolio.controller;

import com.financial.portfolio.dto.PortfolioSummaryResponse;
import com.financial.portfolio.service.PortfolioSummaryService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/portfolio")
public class PortfolioController {

    private final PortfolioSummaryService portfolioSummaryService;

    public PortfolioController(PortfolioSummaryService portfolioSummaryService) {
        this.portfolioSummaryService = portfolioSummaryService;
    }

    @GetMapping("/summary")
    public PortfolioSummaryResponse getPortfolioSummary() {
        return portfolioSummaryService.getPortfolioSummary();
    }
}
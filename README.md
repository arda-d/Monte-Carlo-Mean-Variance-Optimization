# BIST 100 Portfolio Management System

A hybrid portfolio optimization and management system combining a quantitative Python analytics engine with a Java Spring Boot backend.

## Architecture

The project is structured as a monorepo consisting of two primary modules:

- backend: A Java Spring Boot REST API responsible for data persistence, asset management, and dynamic calculation of portfolio performance and Profit and Loss (PnL).
- portfolio: A Python analytics engine that fetches historical BIST 100 stock data, computes risk-return metrics, runs Monte Carlo simulations for portfolio optimization, and synchronizes data with the backend API.

## Core Features

- Automated historical data retrieval and processing for BIST 100 equities.
- Portfolio optimization utilizing Monte Carlo simulations to determine optimal asset allocation and risk-return balance.
- RESTful integration allowing the Python analytics pipeline to batch-update portfolio holdings in the database.
- Real-time backend calculation of total purchase value, current market value, total profit and loss, and percentage returns.

## Getting Started

### Backend (Spring Boot)
1. Navigate to the backend directory.
2. Open the project in an IDE such as IntelliJ IDEA.
3. Run the main application file (PortfolioApplication.java).

### Analytics Engine (Python)
1. Navigate to the portfolio directory.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

### Run the Pipeline Script
    python main.py# bist-portfolio-system

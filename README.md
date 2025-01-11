README: MLTrader Algorithmic Trading Strategy

Overview

This repository contains the implementation of MLTrader, a sentiment-driven algorithmic trading strategy. The strategy leverages Alpaca’s API for trading, FinBERT sentiment analysis for news interpretation, and LumiBot for algorithmic trading management. The goal is to dynamically adjust trading decisions based on market sentiment extracted from recent news headlines.

Features
	•	Dynamic Sentiment Analysis: Utilizes FinBERT to classify sentiment (positive/negative) from the latest financial news headlines.
	•	Automated Trading Decisions:
	•	Executes buy or sell orders based on sentiment.
	•	Employs position sizing calculated from available cash and risk parameters.
	•	Bracket orders are used for risk management with predefined take-profit and stop-loss levels.
	•	Backtesting Support: Backtests the strategy using historical market data from Yahoo Finance.

Prerequisites
	•	Python 3.8 or higher
	•	Required Python libraries:
	•	lumibot
	•	alpaca-trade-api
	•	timedelta
	•	finbert_utils
	•	Alpaca API keys (paper trading or live).

Getting Started

1. Clone the Repository

git clone <repository_url>
cd <repository_name>

2. Install Dependencies

Install the required libraries using pip:

pip install lumibot alpaca-trade-api pandas numpy

3. Configure Alpaca Credentials

Update the API_KEY, API_SECRET, and BASE_URL variables in the script with your Alpaca account details.

4. Run Backtesting

The script includes a backtesting setup to test the strategy’s performance on historical data:

strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters=paramerters
)

5. Execute Live Trading

To switch from backtesting to live trading, configure the broker with live API credentials and use:

trader = Trader(broker=broker, strategy=strategy)
trader.run()

Code Structure

Key Components
	1.	MLTrader Class:
	•	Implements the core logic of the strategy.
	•	Functions:
	•	initialize(): Sets up parameters like trading symbol and risk tolerance.
	•	position_sizing(): Calculates the trade size based on cash available and risk.
	•	get_sentiment(): Fetches news, applies sentiment analysis, and returns sentiment probabilities.
	•	on_trading_iteration(): Executes trades based on sentiment and predefined criteria.
	2.	Broker Setup:
	•	Uses Alpaca as the broker for both backtesting and live trading.
	3.	Backtesting:
	•	Simulates historical trades using Yahoo Finance data.

Customization
	•	Trading Symbol: Modify the symbol parameter in paramerters.
	•	Cash at Risk: Adjust the cash_at_risk parameter for risk tolerance.
	•	Sentiment Thresholds: Tune the probability threshold (.999) in on_trading_iteration() for sensitivity to sentiment analysis.

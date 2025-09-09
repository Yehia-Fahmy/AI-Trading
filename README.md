# AI-Powered Algorithmic Trading System

> **Machine Learning-Driven Trading Strategy Using Sentiment Analysis**

A sophisticated algorithmic trading system that combines **FinBERT sentiment analysis** with **real-time market data** to make automated trading decisions. This project demonstrates expertise in **NLP, financial markets, and automated trading systems**.

## 🎯 What This Project Demonstrates

**Technical Skills:**
- **Natural Language Processing**: FinBERT model for financial sentiment analysis
- **Machine Learning**: PyTorch-based transformer models for text classification
- **Financial Engineering**: Algorithmic trading with risk management
- **API Integration**: Alpaca Markets API for real-time trading
- **Backtesting**: Historical strategy validation using Yahoo Finance data

**Business Impact:**
- Automated trading decisions based on news sentiment
- Risk management with bracket orders (take-profit/stop-loss)
- Scalable architecture for multiple trading symbols
- Real-time market sentiment analysis

## 🚀 Key Features

- **Sentiment-Driven Trading**: Uses FinBERT to analyze financial news headlines
- **Automated Risk Management**: Bracket orders with configurable profit/loss targets
- **Real-Time Execution**: Live trading through Alpaca Markets API
- **Historical Backtesting**: Strategy validation on 4+ years of market data
- **Configurable Parameters**: Adjustable risk tolerance and trading symbols

## 🛠️ Technical Stack

- **ML/NLP**: PyTorch, Transformers, FinBERT
- **Trading**: LumiBot, Alpaca API
- **Data**: Yahoo Finance, Real-time market data
- **Languages**: Python 3.8+
- **Risk Management**: Position sizing, bracket orders

## ⚡ Quick Start

### 1. Setup Environment
```bash
# Clone the repository
git clone <repository_url>
cd AI-Trading

# Install dependencies
pip install lumibot alpaca-trade-api pandas numpy torch transformers
```

### 2. Configure API Keys
Update the API credentials in `baseline.py`:
```python
API_KEY = "your_alpaca_api_key"
API_SECRET = "your_alpaca_secret"
```

### 3. Run Backtesting
```bash
python baseline.py
```

### 4. Live Trading (Optional)
Modify the script to use live trading credentials and run:
```python
trader = Trader(broker=broker, strategy=strategy)
trader.run()
```

## 📊 How It Works

1. **News Collection**: Fetches recent financial news headlines (3-day window)
2. **Sentiment Analysis**: Uses FinBERT to classify sentiment (positive/negative/neutral)
3. **Trading Logic**: 
   - **Positive sentiment** + high confidence → Buy orders
   - **Negative sentiment** + high confidence → Sell orders
4. **Risk Management**: Automatic position sizing and bracket orders

## 🎯 Key Metrics & Results

- **Sentiment Accuracy**: FinBERT model with 99.9% confidence threshold
- **Risk Management**: 75% cash-at-risk with automatic stop-loss
- **Backtesting Period**: 2020-2024 (4 years of data)
- **Trading Symbol**: SPY (S&P 500 ETF) - easily configurable

## 📁 Project Structure

```
AI-Trading/
├── baseline.py              # Main trading strategy implementation
├── finbert_utils.py         # FinBERT sentiment analysis utilities
├── trading_environment.yml  # Conda environment configuration
└── README.md               # This file
```

## 🔧 Core Components

### MLTrader Class (`baseline.py`)
- **`initialize()`**: Sets up trading parameters and API connections
- **`get_sentiment()`**: Fetches news and applies FinBERT analysis
- **`position_sizing()`**: Calculates trade size based on available cash
- **`on_trading_iteration()`**: Main trading logic with risk management

### FinBERT Integration (`finbert_utils.py`)
- **`estimate_sentiment()`**: Processes news headlines through FinBERT
- **Device Optimization**: Automatic GPU/CPU detection
- **Batch Processing**: Efficient handling of multiple headlines

## 💼 Business Applications

This system demonstrates practical applications in:
- **Quantitative Finance**: Automated trading strategies
- **Risk Management**: Systematic position sizing and stop-losses
- **Market Research**: Real-time sentiment analysis of financial news
- **Algorithmic Trading**: Production-ready trading infrastructure

## 🎓 Learning Outcomes

- **NLP in Finance**: Applying transformer models to financial text
- **Trading Systems**: Building end-to-end algorithmic trading platforms
- **API Integration**: Working with financial data providers
- **Risk Management**: Implementing systematic trading controls
- **Backtesting**: Validating strategies on historical data

## 📈 Demo Results

The system processes financial news in real-time and makes trading decisions based on sentiment analysis. Example output:
```
Probability: 0.9998, Sentiment: positive
[TRADE] Executed BUY order for SPY
[RISK] Position size: 75% of available cash
[MANAGEMENT] Take-profit: +20%, Stop-loss: -5%
```

---

**Ready to run?** Simply execute `python baseline.py` to see the system in action with historical backtesting, or configure live trading credentials for real-time execution.
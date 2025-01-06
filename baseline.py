from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime 
from alpaca_trade_api import REST 
from timedelta import Timedelta 
from finbert_utils import estimate_sentiment

API_KEY = "PKAG3YLH2L6HBE3AM0Y0" 
API_SECRET = "urCNfnXihbE7dKOCDVvIMk6jRwOTAaUFX0lHPMcW" 
BASE_URL = "https://paper-api.alpaca.markets"

ALPACA_CREDS = {
    "API_KEY":API_KEY, 
    "API_SECRET": API_SECRET, 
    "PAPER": True
}

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 1, 1)
paramerters = {"symbol": "SPY", "cash_at_risk": 1}

class MLTrader(Strategy):
    def initialize(self, symbol:str="SPY", cash_at_risk:float=1):
        self.symbol = symbol
        self.sleeptime = "24H"
        self.last_trade = None
        self.cash_at_risk = cash_at_risk
        self.api = REST(base_url=BASE_URL, key_id=API_KEY, secret_key=API_SECRET)

    def position_sizing(self):
        cash = self.get_cash()
        last_price = self.get_last_price(self.symbol)
        quantity = round(cash * self.cash_at_risk / last_price, 0)
        return cash, last_price, quantity

    def get_dates(self):
        today = self.get_datetime()
        three_days_ago = today - Timedelta(days=3)
        return today.strftime("%Y-%m-%d"), three_days_ago.strftime("%Y-%m-%d")


    def get_news(self):
        today, three_days_ago = self.get_dates()
        news = self.api.get_news(symbol=self.symbol, start=three_days_ago, end=today)
        news = [ev.__dict__["_raw"]["headline"] for ev in news]
        # print("=====================================")
        # print(f"Returning news from {three_days_ago} to {today}")
        # print(news)
        return news
    
    def on_trading_iteration(self):
        cash, last_price, quantity = self.position_sizing()
        # news = self.get_news()

        if cash > quantity * last_price and quantity > 0:
            order = self.create_order(
                    self.symbol, 
                    quantity, 
                    "buy", 
                    type="bracket", 
                    take_profit_price=last_price*1.20, 
                    stop_loss_price=last_price*.95
                )
            self.submit_order(order)
            self.last_trade = "buy"

broker = Alpaca(ALPACA_CREDS)
strategy = MLTrader(name='mlstrat', broker=broker, parameters=paramerters)



strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters=paramerters
)
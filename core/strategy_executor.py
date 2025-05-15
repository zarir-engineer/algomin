from logzero import logger
# strategy_executor.py
class StrategyExecutor:
    def __init__(self, trading_client, strategies=None):
        self.strategies = strategies
        self.trading_client = trading_client

    def evaluate(self, tick_data):
        if not self.strategies:
            logger.error("Strategies can have some values")
            return
        for strategy in self.strategies:
            if strategy.get("symbol_token") in tick_data.get("token", ""):
                print("🧠 Strategy triggered for token:", strategy["symbol_token"])
                order_data = {
                    "variety": "NORMAL",
                    "tradingsymbol": strategy["tradingsymbol"],
                    "symboltoken": strategy["symbol_token"],
                    "transactiontype": strategy["order_type"],
                    "exchange": "NSE",
                    "ordertype": "LIMIT",
                    "producttype": "INTRADAY",
                    "duration": "DAY",
                    "price": strategy["target_price"],
                    "quantity": strategy["quantity"]
                }
                result = self.trading_client.place_order(order_data)
                print("✅ Order Placed:", result)

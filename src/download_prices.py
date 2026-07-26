import yfinance as yf

tickers = [ "SPY", "QQQ", "TLT", "GLD", "DBC", "VNQ"]

price_data = yf.download(tickers, start="2000-01-01", end="2025-01-01",
interval="1d", auto_adjust=True)

price_data.to_csv("raw_prices.csv")
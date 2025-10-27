import yfinance as yf
from datetime import datetime

def get_quote_data(tickers):
    results = {}
    for t in tickers:
        info = yf.Ticker(t).info

        # Convert last trade timestamp
        ts = info.get("regularMarketTime")
        trade_time = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S") if ts else None

        results[t] = {
            "last": info.get("regularMarketPrice"),
            "bid": info.get("bid"),
            "bidSize": info.get("bidSize"),     # may be None
            "ask": info.get("ask"),
            "askSize": info.get("askSize"),     # may be None
            "volume": info.get("regularMarketVolume"),
            "trade_time": trade_time,
            "shortName": info.get("shortName"),
            "longName": info.get("longName"),
        }
    return results


# Example usage
tickers = ["AAPL", "MSFT", "XOM"]
data = get_quote_data(tickers)

for t, q in data.items():
    print(f"{t}: {q}")

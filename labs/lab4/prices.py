'''
prices.py provides price lookup utilities for the portfolio system.

RETURN FORMAT
--------------
All functions return a dictionary:
    { symbol : price }

EXAMPLE:
    { "AAPL": 182.55, "MSFT": 411.34 }


MOCK PRICES vs REAL PRICES
--------------------------
If USE_MOCK_YFINANCE == True:
    - All price requests return sample prices from sample_prices.json
    - No network calls are made
    - 100% reliable in classroom environments

If USE_MOCK_YFINANCE == False:
    - Real prices are fetched using the yfinance package
    - Full fallback pipeline ensures price lookups never fail


PRICE LOOKUP FUNCTIONS
----------------------

get_last_close_map(symbols)
    Returns last night’s closing prices for the given symbols.
    Real Mode:
        1. Try yfinance.download() for multi-symbol close data
        2. If that fails, try Ticker(sym).history()
        3. If that fails, return sample prices
    Mock Mode:
        - Always returns sample prices

get_live_map(symbols)
    Returns real-time prices for the given symbols.
    Real Mode:
        1. Try Ticker(sym).fast_info.last_price
        2. If missing, fallback to last-night close via Ticker(sym).history()
        3. If that fails, return sample prices
    Mock Mode:
        - Always returns sample prices


MARKET HOURS
-------------
market_is_open()
    Returns True if the current local time is between 9:30am and 4:00pm
    Monday–Friday.

    This function is *optional* and can be used to improve the
    user experience in view_real_time(), e.g.:

        if not market_is_open():
            print("Market is closed — real-time prices will not change.")

    It does NOT affect the fallback logic for get_live_map(), which
    is already robust and will always return a usable price.

'''

import json, os, math, datetime

# optional imports
try:
    import yfinance as yf
except Exception:
    yf = None


# ---------------------------------------------------------
# Load data files
# ---------------------------------------------------------
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def _load_json(name):
    path = os.path.join(DATA_DIR, name)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

DOW30 = set(_load_json("dow30.json"))
SAMPLE_PRICES = _load_json("sample_prices.json")

# Students (or teacher) can flip this to False for live behavior if desired
USE_MOCK_YFINANCE = False


# ---------------------------------------------------------
# get_last_close_map
# ---------------------------------------------------------
def get_last_close_map(symbols): #note: sybols is a list 
    """
    Returns a dict: {sym: price}
    - Uses sample prices if USE_MOCK_YFINANCE = True
    - Uses yfinance last-close if available
    - Falls back to sample prices if yfinance fails
    """
    symbols = [s for s in symbols if s in DOW30]

    # Mock mode or no yfinance
    if USE_MOCK_YFINANCE or yf is None:
        return {s: float(SAMPLE_PRICES.get(s, math.nan)) for s in symbols}

    # Try multi-symbol download
    try:
        #data = yf.download(symbols, period="1d", threads=False)
        data = yf.download(symbols, period="1d", threads=False, auto_adjust=False, progress = False)

        if data is None or "Close" not in data:
            raise RuntimeError("No 'Close' data returned")

        closes = data["Close"]

        # Single-symbol case
        if getattr(closes, "ndim", 2) == 1:
            return {symbols[0]: float(closes.iloc[-1])}

        # Multi-symbol case
        row = closes.iloc[-1].to_dict()
        return {sym: float(row.get(sym, math.nan)) for sym in symbols}

    except Exception:
        # Per-symbol fallback
        out = {}
        for sym in symbols:
            try:
                h = yf.Ticker(sym).history(period="1d")
                out[sym] = float(h["Close"].iloc[-1])
            except Exception:
                out[sym] = float(SAMPLE_PRICES.get(sym, math.nan))
        return out


# ---------------------------------------------------------
# get_live_map
# ---------------------------------------------------------
def get_live_map(symbols): # note: symbols is a list
    """
    Returns real-time last traded price if possible.
    Fallback chain:
        real-time → last-close → sample prices
    """
    symbols = [s for s in symbols if s in DOW30]

    # mock mode → sample prices
    if USE_MOCK_YFINANCE or yf is None:
        return {s: float(SAMPLE_PRICES.get(s, math.nan)) for s in symbols}

    out = {}
    for sym in symbols:
        px = None

        # 1. Try fast_info (real-time)
        try:
            t = yf.Ticker(sym)
            px = getattr(getattr(t, "fast_info", object()), "last_price", None)
        except Exception:
            px = None

        # 2. Fallback: last-night close
        if px is None:
            try:
                h = yf.Ticker(sym).history(period="1d")
                px = float(h["Close"].iloc[-1])
            except Exception:
                px = None

        # 3. Final fallback: sample price
        if px is None:
            px = float(SAMPLE_PRICES.get(sym, math.nan))

        out[sym] = float(px)

    return out


# ---------------------------------------------------------
# Optional: Is market open?
# (Kept for completeness, not required in lab)
# ---------------------------------------------------------
def market_is_open():
    """
    Returns True if current time is within NYSE trading hours (Eastern time).
    Used optionally for real-time view loops.
    """
    now = datetime.datetime.now()  # we do not require pytz
    # Monday = 0, Sunday = 6
    if now.weekday() >= 5:
        return False

    open_time  = now.replace(hour=9,  minute=30, second=0, microsecond=0)
    close_time = now.replace(hour=16, minute=0,  second=0, microsecond=0)

    return open_time <= now <= close_time

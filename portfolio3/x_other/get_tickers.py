import csv
from pprint import pprint
def get_tickers():
    tickers = {}

    with open("portfolio/ticker.data", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:            
            ticker = row["Ticker"]
            tickers[ticker] = {
                "short_name": row["Short Name"],
                "full_name": row["Full Corporate Name"]
            }

    #pprint(tickers)
    #print(tickers['TSLA'])
    #print(tickers['TSLA']['short_name'])
    return tickers

#get_tickers()

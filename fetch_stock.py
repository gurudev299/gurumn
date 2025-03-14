import yfinance as yf


stock_symbol = "RELIANCE.NS"  # Change this to any stock you want
stock = yf.Ticker(stock_symbol)

# Get the latest closing price
price = stock.history(period="1d")["Close"].iloc[-1]

print(f"Latest stock price of {stock_symbol}: ₹{price}")

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the stock symbol
stock_symbol = "RELIANCE.NS"  # Change this to any stock

# Fetch historical stock data (last 6 months)
stock = yf.Ticker(stock_symbol)
data = stock.history(period="6mo")

# Calculate Moving Averages
data["SMA_50"] = data["Close"].rolling(window=50).mean()  # 50-day moving average
data["SMA_200"] = data["Close"].rolling(window=200).mean()  # 200-day moving average

# Generate Buy/Sell Signals
def generate_signals(data):
    signals = []
    for i in range(1, len(data)):
        if data["SMA_50"].iloc[i] > data["SMA_200"].iloc[i] and data["SMA_50"].iloc[i - 1] <= data["SMA_200"].iloc[i - 1]:
            signals.append("BUY")
        elif data["SMA_50"].iloc[i] < data["SMA_200"].iloc[i] and data["SMA_50"].iloc[i - 1] >= data["SMA_200"].iloc[i - 1]:
            signals.append("SELL")
        else:
            signals.append("")
    return [""] + signals  # First row has no signal

data["Signal"] = generate_signals(data)

# Plot the stock price and moving averages
plt.figure(figsize=(12,6))
plt.plot(data["Close"], label="Stock Price", color="blue")
plt.plot(data["SMA_50"], label="50-day SMA", color="green")
plt.plot(data["SMA_200"], label="200-day SMA", color="red")
plt.legend()
plt.title(f"{stock_symbol} Stock Price & Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.show()

# Check if there is a Buy/Sell signal
latest_signal = data["Signal"].dropna().iloc[-1] if not data["Signal"].dropna().empty else "No Signal"
print(f"Latest Trading Signal for {stock_symbol}: {latest_signal}")

# Print the last 5 rows to check signals
print(data[["Close", "SMA_50", "SMA_200", "Signal"]].tail(5))

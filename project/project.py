import sys
import csv
import math
import yfinance as yf

def main():
    print("Simple Moving Average Crossover Backtest")
    print("------------------------------------------")
    ticker = input("Ticker (e.g. AAPL): ").strip().upper()
    short_w = int(input("Short MA window (e.g. 20): ").strip())
    long_w = int(input("Long MA window (e.g. 50): ").strip())

    # Download prices, compute both MAs, then run backtest
    prices = load_prices(ticker, "2020-01-01", "2024-12-31")
    short_ma = moving_average(prices, short_w)
    long_ma = moving_average(prices, long_w)
    result = backtest(prices, short_ma, long_ma)

    print(f"\nTicker: {ticker}")
    print(f"Strategy Return: {result['strategy_return']:+.2f}%")
    print(f"Buy & Hold Return: {result['bh_return']:+.2f}%")
    print(f"Max Drawdown: {result['max_dd']:.2f}%")
    print(f"Sharpe Ratio: {result['sharpe']:.2f}")
    print(f"Total Trades: {result['trades']}")

# Download daily OHLCV data from Yahoo Finance for the given date range
def load_prices(ticker, start, end):
    data = yf.download(ticker, start=start, end=end, progress=False)
    if data.empty:
        raise ValueError(f"No data founded for {ticker}")
    # Extract closing prices, drop NaN values, return as plain Python list
    prices = data["Close"].squeeze().dropna().tolist()
    if len(prices) < 2:
        raise ValueError("Data not enough")
    return prices

def moving_average(prices, window):
    # Window must be a valid positive integer and not exceed data length
    if window < 1 or window > len(prices):
        raise ValueError(f"Invalid window: {window}")
    # For each position i, average the previous 'window' prices
    # Result is shorter than prices by (window - 1) elements
    return [
        sum(prices[i - window:i]) / window
        for i in range(window, len(prices) + 1)
    ]
    
def backtest(prices, short_ma, long_ma):
    # short_ma is longer than long_ma because it uses a smaller window
    # Trim short_ma so both series start at the same date
    offset = len(prices) - len(long_ma)
    short_ma = short_ma[len(short_ma) - len(long_ma):]

    # Initialize account: normalized starting capital of 1.0, no position
    position = 0 # 0 = out of market, 1 = holding shares
    cash = 1.0
    shares = 0.0
    trades = 0
    equity = [] # Daily portfolio value, used for drawdown and Sharpe

    for i in range(len(long_ma)):
        price = prices[offset + i] # Actual closing price for this day

        if i > 0:
            # Compare yesterday vs today to detect a crossover
            previous_short = short_ma[i - 1]
            previous_long = long_ma[i - 1]
            current_short = short_ma[i]
            current_long = long_ma[i]

        # Golden cross: short MA crosses above long MA → buy signal
            if previous_short <= previous_long and current_short > current_long and position == 0:
                shares = cash / price # Go all-in
                cash = 0
                position = 1
                trades += 1

            # Death cross: short MA crosses below long MA → sell signal
            elif previous_short >= previous_long and current_short < current_long and position == 1:
                cash = shares * price # Liquidate entire position
                shares = 0
                position = 0
                trades += 1
        
        # Record today's total portfolio value (cash + market value of shares)
        current_value = cash + shares * price
        equity.append(current_value)

    # If still holding at end of backtest, close position at last price
    if position == 1:
        cash = shares * prices[-1]

    # Compute performance metrics
    strategy_return = (cash - 1.0) * 100 # Total strategy return
    bh_return = (prices[-1] / prices[offset] - 1) * 100 # Buy & hold return
    max_dd = max_drawdown(equity) * 100 # Max drawdown in %
    sharpe = sharpe_ratio(equity) # Annualized Sharpe ratio

    return {
        "strategy_return": strategy_return,
        "bh_return": bh_return,
        "max_dd": max_dd,
        "sharpe": sharpe,
        "trades": trades
    }

def max_drawdown(equity):
    peak = equity[0] # Track the highest portfolio value seen so far
    max_dd = 0.0
    for val in equity:
        if val > peak:
            peak = val # Update peak
        dd = (peak - val) / peak # Current drawdown from peak
        if dd > max_dd:
            max_dd = dd # Keep track of the worst drawdown
    return -max_dd # Return as negative to indicate a loss

def sharpe_ratio(equity):
    if len(equity) < 2:
        return 0.0
    # Convert equity curve into a series of daily returns
    daily_returns = [
        (equity[i] - equity[i - 1]) / equity[i - 1]
        for i in range(1, len(equity))
    ]
    avg = sum(daily_returns) / len(daily_returns) # Mean daily return
    variance = sum((r - avg) ** 2 for r in daily_returns) / len(daily_returns)
    std = math.sqrt(variance) # Std dev of daily returns
    if std == 0:
        return 0.0
    # Annualized Sharpe = mean daily return / daily std dev * sqrt(252)
    return (avg / std) * math.sqrt(252)

if __name__ == "__main__":
    main()
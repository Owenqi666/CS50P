# Simple Moving Average Crossover Backtest

#### Description:

## Overview

This project is a simple quantitative trading backtester implemented in Python.
It simulates a classic Moving Average Crossover strategy on real historical stock
price data downloaded from Yahoo Finance, and evaluates its performance using
standard financial metrics: total return, buy-and-hold return, maximum drawdown,
and the Sharpe ratio.

---

## Financial and Mathematical Background

### Moving Average

A moving average (MA) smooths out price fluctuations by averaging closing prices
over a rolling window of $N$ days. Formally, the moving average at time $t$ with
window $N$ is:

$$\text{MA}(t) = \frac{1}{N} \sum_{i=0}^{N-1} P(t - i)$$

where $P(t)$ is the closing price on day $t$. A short-window MA (e.g. 20 days)
reacts quickly to recent price changes, while a long-window MA (e.g. 50 days)
reflects the broader trend more slowly.

### Moving Average Crossover Strategy

The crossover strategy generates trading signals by comparing a short-term MA
and a long-term MA:

- Golden Cross: when the short MA crosses above the long MA, it signals that
  recent momentum is stronger than the long-term trend. This is interpreted as
  a buy signal — the strategy goes fully long (buys all available shares).

- Death Cross: when the short MA crosses below the long MA, it signals weakening
  momentum relative to the longer trend. This is interpreted as a sell signal —
  the strategy liquidates the entire position.

This is a trend-following strategy: it profits when prices move in sustained
directional trends and tends to underperform in sideways or choppy markets.

### Strategy Return vs Buy and Hold Return

Strategy return measures the total percentage gain or loss from following the
crossover signals over the backtest period, starting with a normalised capital
of $C_0 = 1.0$:

$$R_{\text{strategy}} = \frac{C_{\text{final}} - C_0}{C_0} \times 100\%$$

Buy and hold return is the return from simply buying on the first day
of the backtest and selling on the last day, serving as a passive benchmark:

$$R_{\text{buy\&hold}} = \frac{P_{\text{last}} - P_{\text{first}}}{P_{\text{first}}} \times 100\%$$

Comparing these two reveals whether active signal-based trading adds value over
simply holding the asset.

### Maximum Drawdown

Maximum drawdown (MDD) measures the largest peak-to-trough decline in portfolio
value over the backtest period:

$$\text{MDD} = \frac{V_{\text{trough}} - V_{\text{peak}}}{V_{\text{peak}}}$$

It captures the worst-case loss an investor would have experienced if they had
bought at the highest point and sold at the lowest. A smaller (less negative)
MDD indicates a more stable and risk-controlled strategy.

### Sharpe Ratio

The Sharpe ratio measures risk-adjusted return — how much return is earned per
unit of risk (volatility) taken:

$$\text{Sharpe} = \frac{\bar{r}}{\sigma_r} \times \sqrt{252}$$

where $\bar{r}$ is the mean daily return and $\sigma_r$ is the standard deviation
of daily returns. The factor $\sqrt{252}$ annualises the ratio, since there are
approximately 252 trading days in a year. A Sharpe ratio above 1.0 is generally
considered acceptable, above 2.0 is considered good, and below 0 means the
strategy performs worse than a risk-free asset.

---

## Code Structure and Purpose

The project consists of two files: project.py and test_project.py.

### project.py

This is the main program file. It contains five functions:

**main()**
The entry point of the program. It prompts the user for a stock ticker symbol
and two window sizes (short and long), then calls the other functions in
sequence to download data, compute moving averages, run the backtest, and print
the results. All output formatting happens here, including displaying percentage
signs and sign indicators for returns.

**load_prices(ticker, start, end)**
Downloads historical daily closing prices from Yahoo Finance using the yfinance
library. It accepts a ticker symbol and a date range, extracts the Close column
from the returned DataFrame, removes any missing values, and returns a plain
Python list of floats. If no data is found or the ticker is invalid, it raises
a ValueError to prevent the rest of the program from running on bad data.

**moving_average(prices, window)**
Computes a simple moving average over a list of prices using a sliding window
of the specified size. It uses a list comprehension to iterate over all valid
positions and compute the mean of each window. The function validates that the
window is a positive integer no larger than the length of the price series,
raising a ValueError otherwise. The result is a list shorter than the input by
(window - 1) elements, since there is no valid average for the first incomplete
windows.

**backtest(prices, short_ma, long_ma)**
Implements the core simulation logic. It first aligns the two moving average
series to the same starting date by trimming the shorter-window series. It then
iterates day by day, maintaining an account with cash and share variables. On
each day it checks whether a crossover occurred between yesterday and today, and
executes a buy or sell accordingly. The daily portfolio value is recorded in an
equity list. After the loop, if the strategy is still invested, it closes the
position at the final price. It then calls max_drawdown and sharpe_ratio on the
equity curve and returns all metrics as a dictionary.

**max_drawdown(equity)**
Takes the equity curve and computes the maximum drawdown by tracking the running
peak and measuring how far each day's value falls below it. Returns a negative
float representing the worst percentage decline observed during the backtest.

**sharpe_ratio(equity)**
Converts the equity curve into a series of daily percentage returns, then
computes the mean and standard deviation of those returns. Applies the standard
annualization formula to produce an annualized Sharpe ratio. Returns 0.0 if the
standard deviation is zero to avoid division errors.

### test_project.py

Contains four pytest test functions that verify the correctness of the core
functions independently of live data or user input:

- test_moving_average: checks correct output values for known inputs, and
  verifies that ValueError is raised for invalid window sizes.
- test_max_drawdown: verifies that the drawdown calculation is mathematically
  correct against a hand-computed expected value.
- test_sharpe_ratio: checks that a monotonically increasing equity curve
  produces a positive Sharpe ratio.
- test_backtest_runs: constructs a synthetic price series and verifies that
  backtest returns a dictionary containing all expected keys.

### requirements.txt

Lists yfinance as the only external dependency. All other functionality uses
Python's standard library (math, csv, sys).

---

## Design Decisions

The decision to normalize starting capital to 1.0 rather than using an arbitrary
dollar amount makes the return calculation cleaner and more general — the result
directly represents a multiplier that is easy to convert to a percentage.

The decision to use only the standard library for calculations (rather than
numpy or pandas) was deliberate: it keeps the code accessible and demonstrates
that the core mathematical operations can be implemented from scratch in pure
Python, which is more in the spirit of this course.

The strategy intentionally uses full position sizing (all-in on buy, all-out on
sell) to keep the simulation logic simple and focused on the signal logic rather
than position management, which would add significant complexity.
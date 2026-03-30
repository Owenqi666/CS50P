import pytest
from project import load_prices, moving_average, backtest, max_drawdown, sharpe_ratio

def test_moving_average():
    prices = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert moving_average(prices, 3) == [2.0, 3.0, 4.0]
    assert moving_average(prices, 1) == [1.0, 2.0, 3.0, 4.0, 5.0]
    with pytest.raises(ValueError):
        moving_average(prices, 0)
    with pytest.raises(ValueError):
        moving_average(prices, 10)

def test_max_drawdown():
    equity = [100, 110, 90, 95, 105]
    result = max_drawdown(equity)
    assert round(result, 4) == round(-(110 - 90) / 110, 4)

def test_sharpe_ratio():
    equity = [100, 101, 102, 103, 104]
    result = sharpe_ratio(equity)
    assert result > 0

def test_backtest_runs():
    prices = [float(i) for i in range(10, 110)]
    short_ma = moving_average(prices, 5)
    long_ma = moving_average(prices, 20)
    result = backtest(prices, short_ma, long_ma)
    assert "strategy_return" in result
    assert "sharpe" in result
    assert "max_dd" in result
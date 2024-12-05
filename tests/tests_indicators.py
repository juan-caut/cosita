import pandas as pd
from bot.indicators import calculate_rsi

def test_calculate_rsi():
    data = pd.DataFrame({'close': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    rsi_data = calculate_rsi(data, period=2)
    assert 'rsi' in rsi_data.columns

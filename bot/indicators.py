import pandas as pd
import ta

def calculate_rsi(data, period):
    """
    Calcula el RSI basado en los datos de cierre.
    """
    data['rsi'] = ta.momentum.RSIIndicator(data['close'], window=period).rsi()
    return data

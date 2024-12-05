import ccxt
import pandas as pd
from bot.config import API_KEY, API_SECRET

# Inicialización del exchange
exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'options': {'adjustForTimeDifference': True}
})

def fetch_data(symbol, timeframe, limit=100):
    """
    Obtiene datos históricos de velas (OHLCV) desde el exchange.
    """
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def get_balance():
    """
    Obtiene el saldo actual en BTC y USDT.
    """
    try:
        balance = exchange.fetch_balance()
        btc_balance = balance['free']['BTC']  # Saldo disponible en BTC
        usdt_balance = balance['free']['USDT']  # Saldo disponible en USDT
        return btc_balance, usdt_balance
    except Exception as e:
        print(f"Error al obtener el saldo: {e}")
        return 0, 0

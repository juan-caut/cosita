from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde .env
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

# Otros parámetros de configuración
SYMBOL = 'BTC/USDT'
TIMEFRAME = '15m'
RSI_PERIOD = 10 #14 :defect
OVERBOUGHT = 70
OVERSOLD = 30
TRADE_AMOUNT = 0.0001

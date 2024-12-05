import time
from bot.config import SYMBOL, TIMEFRAME, RSI_PERIOD, OVERBOUGHT, OVERSOLD, TRADE_AMOUNT
from bot.data_fetcher import fetch_data,get_balance
from bot.indicators import calculate_rsi
from bot.trade_executor import place_order
from bot.utils import setup_logger

# Configuración del logger
logger = setup_logger("../logs/bot.log")

def run_bot():
    """
    Ejecuta el ciclo principal del bot.
    """
    print("-----------")
    logger.info("-----------")

    print("Iniciando bot...")
    logger.info("Bot iniciado")

    while True:
        try:
            print("-----------")
            logger.info("-----------")
            # Obtener saldo actual
            btc_balance, usdt_balance = get_balance()
            print(f"Saldo actual: BTC={btc_balance}, USDT={usdt_balance}")
            logger.info(f"Saldo actual: BTC={btc_balance}, USDT={usdt_balance}")

            # Obtener datos de mercado
            data = fetch_data(SYMBOL, TIMEFRAME)

            # Obtener el precio actual
            current_price = data['close'].iloc[-1]
            print(f"Precio actual: {current_price}")
            logger.info(f"Precio actual: {current_price}")

            # Calcular el RSI
            data = calculate_rsi(data, RSI_PERIOD)
            last_rsi = data['rsi'].iloc[-1]
            print(f"RSI actual: {last_rsi}")
            logger.info(f"RSI actual: {last_rsi}")

            # Verificar señales de compra/venta
            if last_rsi < OVERSOLD:
                print("Senial de COMPRA detectada.")
                logger.info("Senial de COMPRA detectada.")
                place_order('buy', TRADE_AMOUNT, SYMBOL)
            elif last_rsi > OVERBOUGHT:
                print("Senial de VENTA detectada.")
                logger.info("Senial de VENTA detectada.")
                place_order('sell', TRADE_AMOUNT, SYMBOL)

            # Esperar antes de la próxima iteración
            time.sleep(120)  # Esperar 1 minuto
        except Exception as e:
            print(f"Error en el bot: {e}")
            logger.error(f"Error en el bot: {e}")
            time.sleep(120)


if __name__ == "__main__":
    run_bot()

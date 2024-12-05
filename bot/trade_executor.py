from bot.data_fetcher import exchange

def place_order(side, amount, symbol):
    """
    Ejecuta una orden de mercado en el exchange.
    """
    try:
        order = exchange.create_order(symbol=symbol, type='market', side=side, amount=amount)
        print(f"Orden {side} ejecutada: {order}")
    except Exception as e:
        print(f"Error al ejecutar la orden: {e}")

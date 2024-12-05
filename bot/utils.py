import logging

def setup_logger(log_file):
    """
    Configura un archivo de log para el bot.
    """
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger()

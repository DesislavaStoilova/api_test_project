import logging


class Logger:
    def __init__(self, level=logging.INFO):
        # Create the logger
        self.logger = logging.getLogger("Logger")
        self.logger.setLevel(level)

        # Prevent log propagation to the root logger
        self.logger.propagate = False

        # Create a console handler explicitly
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        # Create a formatter and attach it to the handler
        formatter = logging.Formatter(f'%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        # Add the handler to the logger if it's not already added
        if not self.logger.hasHandlers():
            self.logger.addHandler(console_handler)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

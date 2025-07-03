import logging


class Logger:
    _logger_initialized = {}
    
    def __init__(self, level=logging.INFO):
        # Create the logger with a unique name to avoid conflicts
        logger_name = f"Logger_{id(self)}"
        self.logger = logging.getLogger(logger_name)
        
        # Only initialize if not already done for this specific logger
        if logger_name not in Logger._logger_initialized:
            self.logger.setLevel(level)

            # Prevent log propagation to the root logger
            self.logger.propagate = False

            # Create a console handler explicitly
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)

            # Create a formatter and attach it to the handler
            formatter = logging.Formatter(f'%(asctime)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)

            # Add the handler to the logger
            self.logger.addHandler(console_handler)
            Logger._logger_initialized[logger_name] = True

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

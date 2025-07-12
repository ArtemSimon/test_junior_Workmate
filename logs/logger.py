import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys


class Logger():

    """Класс для настройки и управления логгером"""
    def __init__(self, name: str = "csv_processor", log_file: str | None = None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)  # Минимальный уровень логирования

        # Формат сообщений
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        logs_dir = Path("logs")
        logs_dir.mkdir(exist_ok=True)

        # Вывод в консоль
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # Вывод в файл (если указан)
        file_handler = RotatingFileHandler(
        filename="logs/app.log",
        maxBytes=5*1024*1024,  # 5 MB
        backupCount=3,
        encoding="utf-8"
    )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger

# Глобальный логгер для всего проекта
logger = Logger().get_logger()

# logger.info('print lm')
import logging
import json
from datetime import datetime

# Создаем кастомный логгер
logger = logging.getLogger(__name__)

# Создаем кастомный форматтер
class JsonFormatter(logging.Formatter):
    def format(self, record):
        # Создаем словарь с информацией о логе
        log_data = {
            "time": datetime.now().strftime("%H:%M:%S"),
            "level": record.levelname,
            "message": record.msg
        }
        # Преобразуем словарь в JSON-строку
        return json.dumps(log_data)

# Создаем кастомный обработчик для записи логов в файл
file_handler = logging.FileHandler("skillbox_json_messages.log")
file_handler.setFormatter(JsonFormatter())

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)

# Устанавливаем уровень логирования на INFO
logger.setLevel(logging.INFO)

# Примеры лог-сообщений
logger.info("Это информационное сообщение")
logger.warning("Это предупреждение")
logger.error("Это сообщение об ошибке")
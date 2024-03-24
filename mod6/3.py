import logging
import json

class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        json_msg = json.dumps(msg, ensure_ascii=False)
        return json_msg, kwargs

logger = JsonAdapter(logging.getLogger(__name__))

logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('skillbox_json_messages.log')
formatter = logging.Formatter('{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}', datefmt='%H:%M:%S')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info("Сообщение 1")
logger.warning("Сообщение 2")
logger.error("Сообщение 3")

file_handler.close()

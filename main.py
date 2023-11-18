import os

from loguru import logger
from dotenv import load_dotenv
from os import environ, path

load_dotenv(path.abspath('.env'))

FORMAT_LOGGER = environ.get('FORMAT_LOGGER')
LEVEL_FILE_LOGGER = environ.get('LEVEL_FILE_LOGGER')
LEVEL_CONSOLE_LOGGER = environ.get('LEVEL_CONSOLE_LOGGER')
ROTATION_LOGGER = environ.get('ROTATION_LOGGER')
SERIALIZE_LOGGER = environ.get('SERIALIZE_LOGGER') == 'True'

logger.add(
    path.abspath(path.join('logs', '{time:YYYY-MM-DD  HH:mm:ss}.log')),  # Путь к файлу логов с динамическим именем
    rotation=ROTATION_LOGGER,  # Ротация логов каждый день
    compression="zip",  # Использование zip-архива
    level=LEVEL_FILE_LOGGER,  # Уровень логирования
    format=FORMAT_LOGGER,  # Формат вывода
    serialize=SERIALIZE_LOGGER,  # Сериализация в JSON
)

# # Вывод лога в консоль
# logger.add(
#     sink=print,
#     level=LEVEL_CONSOLE_LOGGER,
#     format=FORMAT_LOGGER,
# )


if __name__ == '__main__':
    pass

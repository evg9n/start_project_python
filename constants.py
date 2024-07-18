from os import path, listdir, getenv

from dotenv import load_dotenv


class Constants:

    def __init__(self):
        # определение пути к директории текущего файла
        current_dir = path.dirname(path.abspath(__file__))
        # определение пути к директории файлов переменных окруженний
        path_env = path.join(current_dir, 'env')

        # Обходим все файлы *.env и записываем переменные
        try:
            for env in listdir(path_env):
                if env.endswith('.env'):
                    load_dotenv(path.join(path_env, env))
        except FileNotFoundError:
            pass

        """
        Ниже добавляем нужные из переменные из текущей среды выполнения
        Добавляй или удаляй 
        """

        # логирование
        self.FORMAT_LOGGER = getenv('FORMAT_LOGGER',
                                    default='{time:YYYY-MM-DD HH:mm:ss} | {level} | {file} | {message}')
        self.LEVEL_FILE_LOGGER = getenv('LEVEL_FILE_LOGGER', default='DEBUG')
        self.LEVEL_CONSOLE_LOGGER = getenv('LEVEL_CONSOLE_LOGGER', default='INFO')
        self.ROTATION_LOGGER = getenv('ROTATION_LOGGER', default='1 day')
        self.SERIALIZE_LOGGER = getenv('SERIALIZE_LOGGER', default=None) == 'True'

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError('Constants are not changeable!')
        else:
            super().__setattr__(name, value)

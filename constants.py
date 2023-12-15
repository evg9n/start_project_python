from os import environ, path, listdir

from dotenv import load_dotenv


class Constants:

    def __init__(self):
        load_dotenv(path.abspath(path.join('env', '.env')))
        path_env = path.abspath('env')
        try:
            for env in listdir(path_env):
                if env.endswith('.env'):
                    load_dotenv(path.join(path_env, env))
        except FileNotFoundError:
            pass

        self.FORMAT_LOGGER = environ.get('FORMAT_LOGGER')
        self.LEVEL_FILE_LOGGER = environ.get('LEVEL_FILE_LOGGER')
        self.LEVEL_CONSOLE_LOGGER = environ.get('LEVEL_CONSOLE_LOGGER')
        self.ROTATION_LOGGER = environ.get('ROTATION_LOGGER')
        self.SERIALIZE_LOGGER = environ.get('SERIALIZE_LOGGER') == 'True'

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError('Constants are not changeable!')
        else:
            super().__setattr__(name, value)

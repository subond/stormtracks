import os
import sys
import logging

from stormtracks.load_settings import settings, pyro_settings


def setup_logging(name, filename=None, level_str='DEBUG', console_level_str='WARNING'):
    if not os.path.exists(settings.LOGGING_DIR):
        os.makedirs(settings.LOGGING_DIR)

    level = getattr(logging, level_str)

    # N.B. .log gets added on automatically.
    logging_filename = os.path.join(settings.LOGGING_DIR, '{0}'.format(filename))

    logging.basicConfig(filename=logging_filename,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        level=level)

    return get_logger(name, console_level_str)


def get_logger(name, console_level_str='WARNING'):
    console_level = getattr(logging, console_level_str)

    logger = logging.getLogger(name)

    console_print = logging.StreamHandler(sys.stdout)
    console_print.setLevel(console_level)
    formatter = logging.Formatter('%(message)s')
    console_print.setFormatter(formatter)

    logger.addHandler(console_print)
    return logger


# TODO: Delete this class.
class Logger(object):
    def __init__(self, name, filename=None, level_str='DEBUG', console_level_str='WARNING'):
        if not os.path.exists(settings.LOGGING_DIR):
            os.makedirs(settings.LOGGING_DIR)

        level = getattr(logging, level_str)
        console_level = getattr(logging, console_level_str)

        if filename:
            # N.B. .log gets added on automatically.
            logging_filename = os.path.join(settings.LOGGING_DIR, '{0}'.format(filename))

            logging.basicConfig(filename=logging_filename,
                                format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                                datefmt='%m-%d %H:%M',
                                level=level)
        else:
            logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                                datefmt='%m-%d %H:%M',
                                level=level)

        self.__logger = logging.getLogger(name)

        console_print = logging.StreamHandler(sys.stdout)
        console_print.setLevel(console_level)
        formatter = logging.Formatter('%(message)s')
        console_print.setFormatter(formatter)
        self.__logger.addHandler(console_print)

    def get(self):
        return self.__logger

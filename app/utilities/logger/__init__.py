import json
import logging
import logging.config
from pathlib import Path
from pydantic import validate_call


class Logger:
    @staticmethod
    @validate_call
    def setup_logging(is_verbose: bool):
        config_file = Path(__file__).with_name("logging.conf.json")
        with open(config_file) as f_in:
            config = json.load(f_in)

        logging.config.dictConfig(config)
        logger = Logger.get_instance()
        logger.setLevel(logging.DEBUG if is_verbose else logging.INFO)

        if is_verbose:
            current_level = logging.getLevelName(logger.level)
            logger.debug(f"Verbose mode enabled. Log level set to {current_level}")

    @staticmethod
    def get_instance():
        return logging.getLogger("app")

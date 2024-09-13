import logging

from labs.app import create_app
from labs.db import migrate, drop


logger = logging.getLogger(__name__)
logging.basicConfig(filename="runner.log", filemode="w", encoding="utf-8", level=logging.NOTSET)


def main():
    app = create_app()
    logger.info("Start")
    app.run()
    # drop()
    # migrate(0)


if __name__ == "__main__":
    main()

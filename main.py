#!/usr/bin/env python
# main function to add swagger endpoints

import connexion

from structlog import get_logger

LOGGER = get_logger()

# main function
def main():
    app = connexion.FlaskApp(__name__)
    LOGGER.info("Add swagger documentation")
    app.add_api('swagger.yaml')
    app.run(port=8090)

if __name__ == '__main__':
    main()

try:

    from src.settings import (
        initialize_logging,
        check_directories,
        check_packages,
        required_directories,
        required_packages
    )
    import logging

    logging.getLogger(initialize_logging())
    check_directories(required_directories)
    check_packages(required_packages)

except ImportError as e:
    print(f"Error: {e}")
    exit(1)

from web_interface.app import app

if __name__ == '__main__':

    try:
        logging.info("Starting web interface")
        app.run(
            host='0.0.0.0',
            port=5000,
        )
        logging.info("Web interface started successfully")
    except Exception as e:
        logging.error(f"Error: {e}")
        exit(1)

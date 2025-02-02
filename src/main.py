from modules import execute_bot
from settings import (
    input_csv,
    output_csv,
    initialize_logging
)
import logging

logging.getLogger(initialize_logging())

logging.info("Starting - search for phone number in Google Aplication")
execute_bot(input_csv, output_csv)
logging.info("Finished - search for phone number in Google Aplication")

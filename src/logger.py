import os
import logging

LOG_FILE_PATH = 'logs/app.log'

# Create the directory if it does not exist
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

try:
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        level=logging.INFO,
        format='%(asctime)s:%(levelname)s:%(message)s'
    )
except Exception as e:
    print(f"Error setting up logging: {e}")

if __name__ == '__main__':
    logging.info('Logging has started')
    
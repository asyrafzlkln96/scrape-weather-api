import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
	"status.log",
	maxBytes= 1024 * 1024,
	backupCount = 1,
	encoding="utf8",
	)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")


if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    r = requests.get('https://weather.talkpython.fm/api/weather/?city=Berlin&country=DE')
    if r.status_code == 200:
    	try:
	        data = r.json()
	        temperature = data["forecast"]["temp"]
	        pressure = data["forecast"]["pressure"]
	        humid = data["forecast"]["humidity"]
	        logger.info(f'Weather in Berlin: {temperature}')
	        logger.info(f'Pressure in Berlin: {pressure}')
	        logger.info(f'Humidity in Berlin: {humid}')
    	except Exception as e:
    		logger.exception(str(e))
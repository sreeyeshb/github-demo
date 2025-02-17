import logging

logging.basicConfig(filename='good.log', filemode='w', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


logger.info("Starting the programm")

sreeyesh = {"name": "Sreeyesh",
            "age": 36,
            "height": "5'11",
            "weight": 76.5}

for i, j in sreeyesh.items():
    print(f"{i} : {j}")

logger.info("created the dictionary")

logger.error("there is no problem")

logger.critical("chumma demo")

logger.info("Ending the programm")



import os
import logging
import sys

logging_str="[%(asctime)s: %(module)s: %(levelname)s:-  %(message)s ]"

log_dir="logs"
log_file="logging.log"

log_path=os.path.join(log_dir,log_file)

os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("D A T A S C I E N C E L O G G E R")
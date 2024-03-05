import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"

log_file_path = os.path.join(log_dir, "running_log.log")

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_file_path), ## FileHandler is useful in storing log on the file.
        logging.StreamHandler(sys.stdout) ## StreamHandler is useful in printing log on the terminal itself.
    ]
)

logger = logging.getLogger("PredictiveMaintenanceLogger")
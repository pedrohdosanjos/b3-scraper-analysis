from scraper import run_scraper
from utils.logging_service import setup_logger

logger = setup_logger("scraper", "scraper.log")

if __name__ == "__main__":
    run_scraper(logger)

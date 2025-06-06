from analysis import run_analysis
from interface import run_interface
from scraper import run_scraper
from utils.logging_service import setup_logger

logger = setup_logger("scraper", "scraper.log")


def main():
    run_interface(logger)
    return


if __name__ == "__main__":
    main()

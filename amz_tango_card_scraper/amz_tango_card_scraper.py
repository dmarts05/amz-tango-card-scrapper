"""Module containing the main function of the program."""

import os

from browser import get_chrome_browser
from config_handler import get_config
from gmail_scraper import scrape_tango_cards
from tango_scraper import scrap_amazon_gift_cards


def main() -> None:
    # Get program configuration
    print("[INFO] Reading configuration file...")
    # Get path of config file in the parent directory
    config_file_path = os.path.join(__file__, "..", "config.yml")
    config = get_config(config_file_path)
    print("[INFO] Configuration file read successfully")

    # Scrape Tango Cards from Gmail
    print("[INFO] Scraping Tango Cards from Gmail...")
    tango_cards = scrape_tango_cards(
        config.gmail.get("email", ""),
        config.gmail.get("app_password", ""),
        config.from_list,
        config.script.get("trash", False),
    )
    print("[INFO] Tango Cards scraped successfully")

    # Get Selenium browser
    browser = get_chrome_browser(
        config.script.get("headless", True),
        config.script.get("no_images", True),
        config.script.get("no_webdriver_manager", False),
    )

    # Scrape Amazon gift card codes from Tango Cards
    print("[INFO] Scraping Amazon gift card codes from Tango Cards...")
    amazon_cards = scrap_amazon_gift_cards(browser, tango_cards)
    print("[INFO] Amazon gift card codes scraped successfully")

    # Print Amazon gift card codes
    amazon_cards_str = "\n".join([str(card) for card in amazon_cards])
    print(amazon_cards_str)

    # Close Selenium browser
    browser.quit()


if __name__ == "__main__":
    main()

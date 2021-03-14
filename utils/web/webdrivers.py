from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def get_chrome_capability():
    """https://sites.google.com/a/chromium.org/chromedriver/capabilities"""
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--remote-debugging-port=9222")  # Необходимо из-за бага в хромдрайвере
    # prefs = {}
    # chrome_options.add_experimental_option('prefs', prefs)
    return chrome_options.to_capabilities()


def driver():
    capabilities = {}
    capabilities.update(get_chrome_capability())
    return webdriver.Chrome(desired_capabilities=capabilities)

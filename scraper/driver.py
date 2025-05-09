from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from typing import Literal
BrowserType = Literal['chrome', 'edge']


def browser_driver(user_agent: str = None, browser: BrowserType = 'chrome' ):
    options = ChromeOptions() if browser == 'chrome' else EdgeOptions()
    
    if user_agent:
        options.add_argument(f"user-agent={user_agent}")
    
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
     
    match browser:
        case 'chrome':
            driver = webdriver.Chrome(options=options)
        case 'edge':
            driver = webdriver.Edge(options=options)
        case _:
            raise ValueError(f'Unsupported browser: {browser}')
            
    driver.set_window_size(1200, 800)
    return driver


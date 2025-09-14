from selenium import webdriver
import time

TIMEOUT = 7

def get_page(url: str, domain: str = "localhost"):
    """get www page 

    Args:
        url (str): muss defined url adresse from out func
        domain (str, optional): "localhost" or www or container

    Returns:
        _type_: _description_
    """
    print("1 in get_page")
    driver_url = f"http://{domain}:4444/wd/hub"
    print("2 in get_page -driver_url",driver_url)
    #driver_url = f"http://selenium/standalone-chrome:4444/wd/hub"   


    options = webdriver.ChromeOptions()    

    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    print("3 in get_page- options",options)

    driver = webdriver.Remote(command_executor=driver_url, options=options)
    time.sleep(TIMEOUT)
    # example how to use (url must be defined)
    driver.get(url)
    time.sleep(TIMEOUT)
    return driver.page_source

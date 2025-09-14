import time
from  selenium import webdriver
from tqdm import tqdm
TIMEOUT = 7

def get_chrom_web_page(url: str):
    """CONNECT via Driver Chrom to WebPage 
        ohne Docker via local LIB
        url: str
    """
    objResult = None
    objBrowser= webdriver.Chrome()
    time.sleep(TIMEOUT)   

    try:
        objBrowser.get(url=url)
        time.sleep(TIMEOUT)
        objResult = objBrowser.page_source        

    except Exception as err:
        print(err)
    finally:
        objBrowser.stop_client() 
        objBrowser.close()
        objBrowser.quit()    
        objBrowser = None
        
    print(objResult)
    return objResult

def get_screen_schot(obj:object):    
    return obj.save_screenshot

def get_down_load_file(obj:object):             
    return obj.get_downloadable_files()

def get_element_web_page(obj:object):    
    return obj.find_element('data-title')
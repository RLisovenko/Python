#from xxx_test_var import html_doc_Example
#import test_01_var

import argparse
import time
import requests
from bs4 import BeautifulSoup
from drv_browser import get_chrom_web_page
from drv_docker import get_page

URL_BASE = "https://leetcode.com/{USER}/"

class LeetCodeParser:
    """ Class parser leetCode 
        und print List Task
        Leetcode - https://leetcode.com/<USERID>

    """
    
    def __init__(self, sProFileName="RL_ukr"):                
        sProFileName = sProFileName    

    def get_soup_data(self, objFile: object, sFilePath="", params=None):
        """get Soup container

        Args:
            objFile (object): _description_
            sFilePath (str, optional): _description_. Defaults to "".
            params (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: objSoup
        """
        objResult = None
        if sFilePath == "":
            objResult = BeautifulSoup(objFile, "html.parser")
        else:
            with open(sFilePath, encoding="utf-8") as html_doc_file:
                objResult = BeautifulSoup(html_doc_file, "html.parser")
        return objResult
 

    def get_web_page(self, sURL_Page: str, USER_NAME="RL_ukr"):
        """get web Page Content

        Args:
            sURL_Page (str): url web Page
            USER_NAME (str, optional): user name for test

        Returns:
            _type_: html_content
        """

        objResponseWebPage = None
        url = sURL_Page + USER_NAME        
        objResponseWebPage = requests.get(url)
        html_content = None
        if objResponseWebPage.status_code == requests.codes.not_found:  # error 404
            print(f"WebPage:{url} -> Not Found.")
        else:                                                           # request 200
            print(f"WebPage:{url} -> Found.")
            html_content = objResponseWebPage.content

        return html_content

    # -----------------------------------------------------
    def get_text_in_sub_teg(self, sNameAufGabe: str, sSubTegName="data-title", params=None):                
        return sNameAufGabe.get(sSubTegName)

    def get_list_task(self, url: str,sProFileName="RL_ukr", sTegName="div", subTeg="data-title", domain: str = "localhost") -> list:
        """function get list task

        Args:
            url(str): https://leetcode.com . Defaults https://leetcode.com/RL_ukr/
            sProFileName (str, optional): Test login for check . Defaults to "RL_ukr".
            sTegName (str, optional): main Teg Name for search Defaults to "div".
            subTeg (str, optional): sub Teg. Defaults to "data-title".
            domain (str, optional): where search . Defaults to "localhost".

        Returns:
            list: list task
        """

        soup_container = None
        lResNameAufGabe = []
        start_time = time.time()
        
        sWebPage = "browser_provider"  
        if domain.lower() == "selenium":
            sWebPage = "docker_provider"

        match sWebPage:
            case "browser_provider":                            # bekomt WebPage via selenium
                html_text = get_chrom_web_page(url=url)      
                soup_container = self.get_soup_data(html_text)  
            case "docker_provider":                             # bekomt WebPage via selenium + Docker
                html_text = get_page(url=url, domain=domain)  
                soup_container = self.get_soup_data(html_text)  
            case "www":
                html_text = self.get_web_page("https://leetcode.com/", sProFileName)
            case "local":
                soup_container = self.get_soup_data(None, "test_example/RL_ukr - LeetCode Profile.html")
            case "else_html_text_beispiel":
                html_text = test_01_var.html_doc_Example
                soup_container = self.get_soup_data(html_text) 
        
        print(f"\n duration reading {url}:", time.time() - start_time)
        
        start_time = time.time()
        print("Login: ", soup_container.title.string)        
        sListAufGabe = soup_container.find_all(name=sTegName)        
        iCountTask = 1
        iCountRow = 1
        for sNameAufGabe in sListAufGabe:            
            sResNameAufGabe = str(self.get_text_in_sub_teg(sNameAufGabe, subTeg))
            if sResNameAufGabe != "None":
                print(f"Aufgabe {iCountTask} und hat in Row {iCountRow} gefunden: ", sResNameAufGabe)
                lResNameAufGabe.append(sResNameAufGabe)
                iCountTask += 1
            iCountRow += 1

        print("\n Duration reading List Task:", time.time() - start_time)
        return lResNameAufGabe

# -----------------------------------------------------
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", action="store", default="localhost", help="domain name to access")
    parser.add_argument("-u", "--user", action="store", default="RL_ukr", help="Leetcode user")
    args = parser.parse_args()

    print(f"Using the following domain for selenium: {args.domain}")
    
    url = URL_BASE.format(USER=args.user)
    CheckLogin = args.user
    print (f"Checking url: {url}"," USER: ",CheckLogin)    

    obj = LeetCodeParser(sProFileName = url)
    result = obj.get_list_task(url=url,sProFileName=CheckLogin, domain=args.domain)
    print(77 * "*")
    print(f"List Task {len(result)}:\n", "absent Task!" if len(result) == 0 else result)
    print(77 * "*" + "end*")

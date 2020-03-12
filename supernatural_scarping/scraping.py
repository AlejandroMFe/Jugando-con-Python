from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from bs4 import BeautifulSoup
from time import sleep

download_dir = ""
url_sp = "http://www.argenteam.net/episode/11644/Supernatural.%282005%29.S01E01-Pilot"
url_sp_base = "http://www.argenteam.net"

def enable_download_in_headless_chrome(browser):
    # Esta funcion permite que el chrome descargue un archivo
    # de manera automatica sin pregutnar si lo desea descargar
    # add missing support for chrome "send_command"  to selenium webdriver
    # by https://bugs.chromium.org/p/chromium/issues/detail?id=696481#c86
    browser.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior', 'params': {
        'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)


def set_options_webdriver():
    browser_options = Options()
    # browser_options.add_argument("--headless")
    prefs = {"download.default_directory": download_dir,
             "download.prompt_for_download": False,
             "download.directory_upgrade": True,
             "safebrowsing.enable": True,
             'safebrowsing.disable_download_protection': True
             }
    browser_options.add_experimental_option("prefs", prefs)
    return browser_options


try:
    browser = webdriver.Chrome()
    browser.get(url_sp)
    #driver.find_element(By.XPATH, '//button[text()="Some text"]')

    sleep(2)
    browser.find_element_by_xpath("//button[text()='Aceptar']").click()
    
    soup = BeautifulSoup(browser.page_source, "lxml")
    sleep(3)

    season_list = soup.find("div", class_="season-list")
    # links_list = season_list.find_all("a", href=True)
    # print(links_list)
    # for link in links_list:
    #     print("texto: "+link.text)
    #     print("value: "+str(link["href"]))

    links_list = [a["href"] for a in season_list.find_all("a", href=True)]

    [print(f"{url_sp_base}{str(a)}") for a in links_list]
    

finally:
    browser.quit()
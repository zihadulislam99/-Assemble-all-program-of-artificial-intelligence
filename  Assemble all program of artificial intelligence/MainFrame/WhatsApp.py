from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium import webdriver
import pathlib

scriptDirectory = pathlib.Path().absolute()

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
PathofDriver = "DataBase\\chromedriver.exe"
driver = webdriver.Chrome(PathofDriver, options=options)
driver.maximize_window()




Message = "Hello ghjkjhjkjhjkjk"
Number = "+8801922405991"
LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
driver.get(LinkWeb)
sleep(5)
try:
    sleep(15)
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()

except:
    print("Invalid Number")


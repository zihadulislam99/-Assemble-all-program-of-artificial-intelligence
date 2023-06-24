# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from time import sleep
#
# chrome_options = Options()
# chrome_options.add_argument('--log-level=3')
# chrome_options.headless = True
# Path = "DataBase\\chromedriver.exe"
# driver = webdriver.Chrome(Path,options=chrome_options)
# driver.maximize_window()
#
# website = r"https://ttsmp3.com/text-to-speech/British%20English/"
# driver.get(website)
# ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
# ButtonSelection.select_by_visible_text('British English / Brian')
#
# def Speak(Text):
#     lengthoftext = len(str(Text))
#
#     if lengthoftext==0:
#         pass
#
#     else:
#         print(f"AI : {Text}.")
#         Data = str(Text)
#         xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
#         driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
#         driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
#         driver.find_element(By.XPATH,value="/html/body/div[4]/div[2]/form/textarea").clear()



# import instaloader
# import re
#
# bot = instaloader.Instaloader()
# profile = instaloader.Profile.from_username(bot.context, 'zihadultalukder9900')
# # print(profile)
# emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
#
# print("Username:", profile.username)
# # print("Name: ", profile.name)
# print("User ID:", profile.userid)
# print("Number of Posts:", profile.mediacount)
# print("Followers Count:", profile.followers)
# print("Following Count:", profile.followees)
# print("Bio:", profile.biography)
# print("External URL:", profile.external_url)
# print("Emails:", emails)




# import requests
# from bs4 import BeautifulSoup
# url = 'https://www.bbc.com/news'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# headlines = soup.find('body').find_all('h3')
# unwanted = ['BBC World News TV', 'BBC World Service Radio', 'News daily newsletter', 'Mobile app', 'Get in touch']
# for x in list(dict.fromkeys(headlines)):
# 	if x.text.strip() not in unwanted:
# 		print(x.text.strip())
import cv2

image = cv2.imread('path_to_image.jpg')

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

invert = cv2.bitwise_not(gray_img)

blur = cv2.GaussianBlur(invert, (21, 21), 0)

inverted_blur = cv2.bitwise_not(blur)

sketch = cv2 . divide(gray_img, inverted_blur, scale=256.0)

cv2 . imwrite('path_to_output_sketch.jpg', sketch)



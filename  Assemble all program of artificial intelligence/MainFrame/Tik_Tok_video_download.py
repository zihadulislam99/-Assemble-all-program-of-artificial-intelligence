import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen


def downloadVideo(link, id, Tiktok_Username):
    cookies = {
        '__gads': 'ID=b6feb575e5563738-22036864e3db003d:T=1678082417:RT=1678082417:S=ALNI_MZZPSzTvn6P9SA-1IleVKTty5o6aw',
        'ab.storage.deviceId.a9882122-ac6c-486a-bc3b-fab39ef624c5': '%7B%22g%22%3A%227db69a3e-b0a4-1530-a546-d4d0f4407fc3%22%2C%22c%22%3A1682100628254%2C%22l%22%3A1682100628254%7D',
        '_gid': 'GA1.2.1621283113.1684825659',
        '__gpi': 'UID=00000bd2e5abb57f:T=1678082417:RT=1684825660:S=ALNI_MbUNgW0LX2BPOv6ULSmCuMDr2g-cw',
        '__cflb': '02DiuEcwseaiqqyPC5qrDCss6XuWcthYNfytbgqkBAXRM',
        '_gat_UA-3524196-6': '1',
        '_ga': 'GA1.2.2085980683.1678082417',
        '_ga_ZSF3D6YSLC': 'GS1.1.1684825658.1.1.1684825892.0.0.0',
    }

    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '__gads=ID=b6feb575e5563738-22036864e3db003d:T=1678082417:RT=1678082417:S=ALNI_MZZPSzTvn6P9SA-1IleVKTty5o6aw; ab.storage.deviceId.a9882122-ac6c-486a-bc3b-fab39ef624c5=%7B%22g%22%3A%227db69a3e-b0a4-1530-a546-d4d0f4407fc3%22%2C%22c%22%3A1682100628254%2C%22l%22%3A1682100628254%7D; _gid=GA1.2.1621283113.1684825659; __gpi=UID=00000bd2e5abb57f:T=1678082417:RT=1684825660:S=ALNI_MbUNgW0LX2BPOv6ULSmCuMDr2g-cw; __cflb=02DiuEcwseaiqqyPC5qrDCss6XuWcthYNfytbgqkBAXRM; _gat_UA-3524196-6=1; _ga=GA1.2.2085980683.1678082417; _ga_ZSF3D6YSLC=GS1.1.1684825658.1.1.1684825892.0.0.0',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'WjNoRzhh',
    }

    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, "html.parser")
    downloadLink = downloadSoup.a["href"]
    mp4File = urlopen(downloadLink)
    id = id + 1
    with open(f"Tiktok/Download/{Tiktok_Username}/{id}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break

def TiktokVideoDownload(Tiktok_Username):

    try:
        os.mkdir(f"Tiktok/Download/{Tiktok_Username}")
    except:
        pass


    driver = webdriver.Chrome()
    driver.get(f"https://www.tiktok.com/{Tiktok_Username}")
    time.sleep(20)
    scroll_pause_time = 1
    screen_height = driver.execute_script("return window.screen.height;")
    i = 1
    while True:
        time.sleep(20)
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        i += 1
        time.sleep(scroll_pause_time)
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        if (screen_height) * i > scroll_height:
            break
    soup = BeautifulSoup(driver.page_source, "html.parser")
    videos = soup.find_all("div", {"class": "tiktok-yz6ijl-DivWrapper"})
    lenth = (len(videos))
    print(f"({Tiktok_Username}) Tiktok account has {lenth} videos")

    for index, video in enumerate(videos):
        indexnum = index + 1
        try:
            downloadVideo(video.a["href"], index, Tiktok_Username)
            print(f"[{indexnum}] Download successful ✅")
        except:
            print(f"[{indexnum}] Download fail ❌")
        time.sleep(10)

    print("fenesh")

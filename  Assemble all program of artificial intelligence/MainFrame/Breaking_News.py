from GoogleNews import GoogleNews

try:
    News = GoogleNews(lang='en', period='1d', encode='utf-8')
    # News = GoogleNews()
    News.search("cricket")
    Results = News.result(sort=True)
    # print(Results)
    for Result in Results:
        print("\nTitle: ", Result["title"])
        print("Media: ", Result["media"])
        print("Link: ", Result["link"])
        print("Image: ", Result["img"])

except:
    pass
import webbrowser
from Body.Speak import Say

def OpenWebs(command):
    webs = [["spotify my favourite song", "https://open.spotify.com/collection/tracks"],
            ["youtube", "https://www.youtube.com/"],
            ["facebook", "https://www.facebook.com/"],
            ["twitter", "https://twitter.com/"],
            ["instagram", "https://www.instagram.com/"],
            ["linkedin", "https://www.linkedin.com/"],
            ["whatsapp", "https://web.whatsapp.com/"],
            ["reddit", "https://www.reddit.com/"],
            ["telegram", "https://web.telegram.org/"],
            ["discord", "https://discord.com/channels/@me"],
            ["github", "https://github.com/zihadulislam99"],
            ["wikipedia", "https://www.wikipedia.org/"],
            ["mlw bd", "https://mlwbd.global/"],
            ["chat gpt", "https://chat.openai.com/"],
            ["google bird", "https://bard.google.com/"],
            ["router admin panel", "http://192.168.0.1/"],
            ["spotify home", "https://spotify.com/"]
        ]
    for web in webs:
        if f"open {web[0]}" in command:
            Say(f"Opening {web[0]}")
            webbrowser.open(web[1])
import wikipedia

def wikipedia_data(query):
    try:
        info = wikipedia.summary(query)
        return info
    except:
        return ("I don't understand your prompt")


input_box = "Artificial Intelligence"
print(wikipedia_data(input_box))
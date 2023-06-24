import openai

def ReplyBrain(question,chat_log = None):
    # fileopen = open("Data\\Api.txt", "r")
    # API = fileopen.read()
    # fileopen.close()

    openai.api_key = "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"
    completion = openai.Completion()

    FileLog = open("../DataBase/chat_log.txt", "r")
    chat_log_template = FileLog.read()
    FileLog.close()
    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}H : {question}\nA : '
    response = completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0.7,
        engine="davinci-codex",  # Use "davinci-codex" for the GPT-3.5 Turbo model
        # language="en",  # Set the English language
        language="bn",  # Set the Bangla language
        completions=None,
        logprobs=None,
        messages=None,
        context=None,
        length=None,
        stream=None,
        stop=None,
        echo=True,
        n=1
    )
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nH : {question} \nA : {answer}"
    FileLog = open("../DataBase/chat_log.txt", "w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer

inpute_boxe = "Hello!"
ppp = ReplyBrain(inpute_boxe)
print(ppp)
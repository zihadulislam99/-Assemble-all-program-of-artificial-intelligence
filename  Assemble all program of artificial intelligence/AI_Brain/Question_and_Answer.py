import cohere
from Body.Listening import TakeCommand
from Body.Speak import Say

def AI_Chat_Log(question,chat_log = None):
    API = cohere.Client('JrqPuFZsVIM1cHdn8HYx9ulNjSgD3S1ylPeUtPw0')
    FileLogs = open("../DataBase/prompt.txt", "r")
    chat_log_templates = FileLogs.read()
    FileLogs.close()
    if chat_log is None:
        chat_log = chat_log_templates
    prompt = f'{chat_log}H : {question}\nA : '


    response = API.generate(
        model='command-light',
        prompt=prompt,
        max_tokens=300,
        temperature=0.9,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE')
    answer = ('{}'.format(response.generations[0].text))
    answer = answer.replace("\n", "")


    FileLog = open("AI_Chat\\Chat_Log_2.txt", "r")
    chat_log_template = FileLog.read()
    chat_log_template_update = chat_log_template + f"\nH: {question}\nA : {answer}"
    FileLog = open("AI_Chat\\Chat_Log_2.txt", "w")
    FileLog.write(chat_log_template_update)
    FileLog.close()

    return answer

while True:
    print("Listening...")
    Listening = TakeCommand()
    say = AI_Chat_Log(Listening)
    Say(say)

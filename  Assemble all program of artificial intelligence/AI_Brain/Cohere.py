import cohere
from Body.Speak import Say
from Body.Listening import TakeCommand


def ReplyBrain(question,chat_log = None):
  API = cohere.Client('JrqPuFZsVIM1cHdn8HYx9ulNjSgD3S1ylPeUtPw0')
  FileLog = open("../DataBase/chat_log.txt", "r")
  chat_log_template = FileLog.read()
  FileLog.close()
  if chat_log is None:
    chat_log = chat_log_template
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


  chat_log_template_update = chat_log_template + f"\nH : {question} \nA : {answer}"
  FileLog = open("../DataBase/chat_log.txt", "w")
  FileLog.write(chat_log_template_update)
  FileLog.close()
  return answer


while True:
  inpute_boxe = TakeCommand()
  ppp = ReplyBrain(inpute_boxe)
  Say(ppp)

# https://www.youtube.com/watch?v=TjxgmLQrDJA
# https://dashboard.cohere.ai/
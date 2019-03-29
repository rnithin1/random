import requests, time
import sikhgenerator
request = {'token' : '[redacted]'}

while True:
  response = requests.get('https://api.groupme.com/v3/groups/27409006/messages', params=request)
  if(response.status_code == 200):
    messages = response.json()['response']['messages']
    for m in messages:
      if(m['text'] == 'Generate sikh'):
        post = {'bot_id' : 'afb038714798f3441bbd41f2ea', 'text': sikhgenerator.make_name()}
        requests.post('https://api.groupme.com/v3/bots/post', params=post)
        request['since_id'] = m['id']
        break
time.sleep(4)

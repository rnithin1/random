import requests, time
import sikhgenerator
request = {'token' : '8dvD3RsRjQBYzYEMC9GveMg0MnQq0R5a7M4HMzAI'}

while True:
  response = requests.get('https://api.groupme.com/v3/groups/27409006/messages', params=request)
  if(response.status_code == 200):
    messages = response.json()['response']['messages']
    for m in messages:
      if(m['text']):
        m['text'] = m['text'].lower()
      if(m['text'] == 'Generate sikh'):
        post = {'bot_id' : 'afb038714798f3441bbd41f2ea', 'text': sikhgenerator.make_name()}
        requests.post('https://api.groupme.com/v3/bots/post', params=post)
        request['since_id'] = m['id']
        break
  time.sleep(4)

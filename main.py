import asyncio
import os
import sys
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())



env_vars = {}
if os.path.isfile('.device'):
    with open('.device') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            key, value = line.strip().split('=', 1)
            env_vars[key] = value.replace("\"", "")
else:
  print("error device in the file")
  sys.exit()

os.system('pip install -U XBXBOT')
os.system('clear')

import XBXBOT


try:
  client = XBXBOT.XBXBOT(
    device_id=env_vars['DEVICE_ID'],
    account_id=env_vars['ACCOUNT_ID'],
    secret=env_vars['SECRET']
)

except:

  client = XBXBOT.PartyBot(
    device_id=os.getenv('DEVICE_ID'),
    account_id=os.getenv('ACCOUNT_ID'),
    secret=os.getenv('SECRET')
)
  
try:
    client.run()
except Exception as e:
    print(e)
    print("Can't login because your device auths is probably wrong.")
    print("are you sure you have put yourr IDs in secrets env or in .device  file ?")


from colorama import Fore
import os,sys
import requests




os.system('cls||clear')

print(Fore.RED+' __      __.__              _____               _____.___.           _________')
print(Fore.RED+'/  \    /  \  |__   ____   /  _  \_______   ____\__  |   | ____  __ _\_____   |')
print(Fore.RED+'\   \/\/   /  |  \ /  _ \ /  /_\  \_  __ \_/ __ \/   |   |/  _ \|  |  \ /   __/')
print(Fore.RED+' \        /|   Y  (  <_> )    |    \  | \/\  ___/\____   (  <_> )  |  /|   |  ')
print(Fore.RED+'  \__/\  / |___|  /\____/\____|__  /__|    \___  > ______|\____/|____/ |   |  ')
print(Fore.RED+'       \/       \/               \/            \/\/                    <___>  ')


### USER DATA ###
country = input(" \033[1;37mCOUNTRY\033[0m (without +)\033[1;37m ═>\033[1;36m ")
phone = input(" \033[1;37mNUMBER ═>\033[1;36m ")
victim_phone = '+' + country + phone
message = input(" \033[1;37mMESSAGE ═>\033[1;36m ")

### API ### 
resp = requests.post('https://textbelt.com/text', {
  'phone': victim_phone,
  'message': message,
  'key': 'textbelt',
})
print(resp.json())

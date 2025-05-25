import requests
import time
import random
from fake_useragent import UserAgent

ua = UserAgent()

mainvanity = ''
serverid = ''
token = ''
 
base_url = 'https://discord.com/api/v9'
invite_url = f'{base_url}/invites/{mainvanity}'
settings_url = f'{base_url}/guilds/{serverid}/vanity-url'                                                                                                                                                                                                                                                         
audit_log_url = f'{base_url}/guilds/{serverid}/audit-logs'                                                                                                                                                                                                                                                          
guild_url = f'{base_url}/guilds/{serverid}'
dm_url = f'{base_url}/users/@me/channels'                                                                                                                                                                                                                                                          
user_url = f'{base_url}/users/'
headers = {
    'Authorization': f'{token}',
    'Content-Type': 'application/json',
    'User-Agent': ua.random                                                                                                                                                                                                                                                        
}

def print_success(message):
    print(f'\033[92m[+] {message}\033[0m')

def print_error(message):
    print(f'\033[91m[-] {message}\033[0m')

def vanitycodecd():
    response = requests.get(settings_url, headers=headers)
    if response.status_code == 200:
        return response.json().get('code')                                                                                                                                                                                                                                                          
    else:                                                                                                                                                                                                                                                          
        print_error(f'Failed to get current vanity URL: {response.text}')
        return None
    




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
    
def setvanity():
    start_time = time.time()
    patch_response = requests.patch(
        settings_url,
        headers=headers,
        json={'code': mainvanity}
    )
    end_time = time.time()

    if patch_response.status_code == 200:
        duration = end_time - start_time
        print_success(f'Vanity URL "{mainvanity}" has been set for the server [in {duration:.2f} seconds].')                                                                                                                                                                                                                                                          
    else:
        print_error(f'Failed to set vanity URL: {patch_response.text}')

def kick_user(user_id):
    kick_url = f'{base_url}/guilds/{serverid}/members/{user_id}'
    response = requests.delete(kick_url, headers=headers)
    if response.status_code == 204:
        print_success(f'User {user_id} has been kicked from the server.')
    else:
        print_error(f'Unable to kick user {user_id} due to {response.text}')

def lastlogaudit():
    response = requests.get(audit_log_url, headers=headers, params={'limit': 1, "action_type": 60})
    if response.status_code == 200:
        logs = response.json().get('audit_log_entries')
        if logs:
            return logs[0]
        else:
            print_error(f"Failed to get audit logs: No entries found.")
        return None

def get_user_info(user_id):
    response = requests.get(f'{user_url}{user_id}', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print_error(f'Failed to get user info for {user_id}: {response.text}')
        return None
    
def send_dm(user_id, message):
    payload = {'recipient_id': user_id}
    response = requests.post(dm_url, headers=headers, json=payload)
    if response.status_code == 200:
        dm_channel_id = response.json().get('id')
        message_url = f'{base_url}/channels/{dm_channel_id}/messages'
        message_payload = {'content': message}
        response = requests.post(message_url, headers=headers, json=message_payload)                                                                                                                                                                                                                                                          
        if response.status_code != 200:
            print_error(f'Failed to send DM: {response.text}')
    else:
        print_error(f'Failed to create DM channel: {response.text}')

def owneridfetch():
    response = requests.get(guild_url, headers=headers)
    if response.status_code == 200:
        return response.json().get('owner_id')
    else:
        print_error(f'Failed to get owner ID: {response.text}')
        return None

owner_id = owneridfetch()     

while True:                                                                                                                                                                                                                                                         
    try:
        current_code = vanitycodecd()
        if current_code != mainvanity:
            start_time = time.time()
            print_error(f'Unauthorized vanity URL change detected: {current_code}')
            
            
            setvanity()

            last_log_entry = lastlogaudit()
            if last_log_entry:
                user_id = last_log_entry.get('user_id')
                user_info = get_user_info(user_id)
                if user_info:
                    username = user_info.get('username')
                    discriminator = user_info.get('discriminator')
                    print_error(f'Unauthorized vanity URL change by {username}#{discriminator} detected: {current_code}.')                                                                                                                                                                                                                                                          

                    message = f'Unauthorized vanity URL change by {username}#{discriminator} detected. Vanity URL reset to "{mainvanity}".'                                                                                                                                                                                                                                                         
                    if owner_id:
                        send_dm(owner_id, message)

                    kick_user(user_id)

            end_time = time.time()                                                                                                                                                                                                                                                          
            duration = end_time - start_time                                                                                                                                                                                                                                                          
            print_success(f'Action completed in {duration:.2f} seconds.')                                                                                                                                                                                                                                                          

        time.sleep(10)                                                                                                                                                                                                                                                          

    except requests.RequestException as e:
        print_error(f'Error occurred: {e}')                                                                                                                                                                                                                                                          
        time.sleep(60)                                                                                                                                                                                                                                                          


            






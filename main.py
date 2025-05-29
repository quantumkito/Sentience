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
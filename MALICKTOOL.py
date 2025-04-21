# Logo
logo = """


  __  __          _      _____ _____ _  __
 |  \/  |   /\   | |    |_   _/ ____| |/ /
 | \  / |  /  \  | |      | || |    | ' / 
 | |\/| | / /\ \ | |      | || |    |  <  
 | |  | |/ ____ \| |____ _| || |____| . \ 
 |_|  |_/_/    \_\______|_____\_____|_|\_\
                                          
                                          
                                             
\033[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[37m[*] 𝐎𝐖𝐍𝐄𝐑      : \033[36m𝐌𝐀𝐋𝐈𝐂𝐊
\033[37m[*] 𝐆𝐈𝐓𝐇𝐔𝐁     : \033[33m𝐋𝐄𝐆𝐄𝐍𝐃 𝐌𝐀𝐋𝐈𝐂𝐊
\033[37m[*] 𝐒𝐓𝐀𝐓𝐔𝐒     : \033[32m𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐏𝐀𝐈𝐃 𝐓𝐎𝐎𝐋
\033[37m[*] 𝐓𝐄𝐀𝐌       : \033[35m𝐎𝐍𝐄 𝐌𝐀𝐍 𝐀𝐑𝐌𝐘
\033[37m[*] 𝐓𝐎𝐎𝐋       : \033[34m𝐄𝐍𝐃 𝐓𝐎 𝐄𝐍𝐃 𝐄𝐍𝐂𝐑𝐘𝐏𝐓𝐈𝐎𝐍 
\033[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
print(logo)

import os
import random
import time
import requests

# Facebook Graph API endpoint
thread_id = input("\033[1;32mEnter thread ID: ")

url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'

# Token file paths
token_file_paths = input("\033[33mEnter token file paths (separated by comma): ").split(',')

# Message file path
message_file_path = input("\033[34mEnter message file path: ")

# Haters name
haters_name = input("\033[35mEnter haters name: ")

# Delay between messages
delay_between_messages = int(input("\033[36mEnter delay between messages: "))

# Read tokens from files
access_tokens = []
token_names = []
for token_file_path in token_file_paths:
    with open(token_file_path.strip(), "r") as token_file:
        for i, token in enumerate(token_file.readlines()):
            access_tokens.append(token.strip())
            token_names.append(f"Token {i+1}")

# Read messages from file
messages = []
with open(message_file_path, "r") as message_file:
    messages = message_file.readlines()

def get_account_name(token):
    try:
        response = requests.get(f'https://graph.facebook.com/v15.0/me?access_token={token}')
        data = response.json()
        return data['name']
    except Exception as e:
        return "Unknown"

def send_message(token, message, thread_id, haters_name):
    try:
        message_url = f"{url}"
        message_params = {
            "access_token": token,
            "message": f"{haters_name} {message}"
        }
        message_response = requests.post(message_url, params=message_params)
        if message_response.status_code == 200:
            current_time = time.strftime("%H:%M:%S")
            print(f"""
 \033[34m 
✪✭═══════•『 𝐓𝐇𝐄 𝐋𝐄𝐆𝐄𝐍𝐃 𝐌𝐀𝐋𝐈𝐂𝐊 𝐎𝐍𝐅𝐈𝐑𝐄』•═══════✭✪
""")
            account_name = get_account_name(token)           
            print(f"\033[38;5;25m[+] 𝐀𝐀𝐏𝐊𝐀 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐌𝐀𝐋𝐈𝐂𝐊 𝐒𝐈𝐑 𝐊𝐈 𝐓𝐀𝐑𝐀𝐅 𝐒𝐄 𝐂𝐇𝐀𝐋𝐀 𝐆𝐀𝐘𝐀  => Thread ID: {thread_id} => Token: {token_names[access_tokens.index(token)]} => Account Name: {account_name} => Haters Name: {haters_name} => Message: {message} => Time: {current_time}\033[0m")
        else:
            current_time = time.strftime("%H:%M:%S")
            print(f"""
 \033[31;5;196m 
✪✭═══════•『𝐓𝐇𝐄 𝐋𝐄𝐆𝐄𝐍𝐃 𝐌𝐀𝐋𝐈𝐂𝐊 𝐎𝐍𝐅𝐈𝐑𝐄』•═══════✭✪
""")
            print(f"\033[38;5;196m𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐅𝐀𝐈𝐋𝐄𝐃 𝐇𝐎𝐆𝐀𝐘𝐀 𝐇𝐀𝐈=> Thread ID: {thread_id} =>Token: {token_names[access_tokens.index(token)]} => Haters Name: {haters_name} => Message: {message} => Time: {current_time}\033[0m")
    except Exception as e:
        print(str(e))

def process_messages_thread():
    try:
        while True:
            random_token = random.choice(access_tokens)
            random_message = random.choice(messages).strip()
            send_message(random_token, random_message, thread_id, haters_name)
            time.sleep(delay_between_messages)
    except Exception as e:
        print(str(e))

process_messages_thread()

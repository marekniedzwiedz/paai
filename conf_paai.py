MODELS = {
    'gpt35': {
        'model': 'gpt-3.5-turbo',
        'api_key': open('.secret_api_key.txt').read().strip(),
    }
}

MODEL = MODELS['gpt35']

COLORS = {
    'CRED': '\033[91m',
    'CEND': '\033[0m'    
}

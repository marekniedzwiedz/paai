MODELS = {
    'gpt35': {
        'model': 'gpt-3.5-turbo',
        'api_key': open('.secret_api_key.txt').read().strip(),
    }
}

MODEL = MODELS['gpt35']

STYLES = {
    'ITALICS': "\x1B[3m",
    'SEND': '\x1B[0m',
}

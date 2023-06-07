import openai

from conf_paai import MODEL, COLORS
from prompts import PROMPTS


openai.api_key  = MODEL['api_key']


def get_completion_from_messages(messages, model=MODEL['model'], temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


def set_prompt():
    print('Reply with number of prompt you would like to use')
    for count, value in enumerate(PROMPTS):
        print (count, '-', value[0]['content'])
    return PROMPTS[int(input(">> "))]


def show_prompts(conversation):
    print('Starting prompts:')
    for entry in conversation:
        if entry['role'] == 'user':
            print ('>>', entry['content'])
        else:
            print ('<<', entry['content'])


conversation = set_prompt()
show_prompts(conversation)

# Main interaction loop
while True:
    user_input = []
    MULTILIE = False
    while True:
        if len(user_input) == 0:
            user_input.append(input(">> "))
            if user_input[0].startswith('"""'):
                MULTILIE = True
        else:
            user_input.append(input())
        if not MULTILIE or user_input[-1].endswith('"""'):
            break

    ENTRY = "\n".join(user_input)
    if ENTRY.lower() == 'exit()':
        break
    if ENTRY.lower() == 'prompt()':
        conversation = set_prompt()
        show_prompts(conversation)
    else:
        conversation.append({'role': 'user', 'content': ENTRY})
        response = get_completion_from_messages(conversation)
        conversation.append({'role': 'system', 'content': response})
        print(COLORS['CRED'], "<< ", response, COLORS['CEND'])

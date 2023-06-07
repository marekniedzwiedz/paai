PAAI was created to make it easier to use chatgpt type of tool.

Today it supports only chatgpt from Openai.
To use it, you have to: 
1. generate API key - https://platform.openai.com/account/api-keys.
2. create a file '.secret_api_key.txt' and put there your API key.
3. you can extend and modify prompts.py to include your often-used prompts.
4. commands
    - prompt() - select new prompt;
    - exit() - exit;
    - use """ to start multiline input; you have to finish it as well with """.
5. if you want to add private prompts just create a file 'private_prompts.py' with variable inside of it PRIVATE_PROMPTS
    - e.g PRIVATE_PROMPTS = [
        [ {'role':'user', 'content':'I want to chat with you.'} ],
        ]


I've been using it for a few weeks and find it helpful. I hope you will find it useful as well.
Do share with me your prompts and ideas!

I apologize for the code quality - first time doing that after years without coding.

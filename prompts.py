import os

PROMPTS = [
    [ {'role':'user', 'content':'I want to chat with you.'} ],
    [ {'role':'user', 'content':'I will ask you a question about the subject that I want to learn about. Identify and share the most important 20% of learnings from this topic that will help me understand 80% of it.'} ],
    [ {'role':'user', 'content':'I will ask you to analyze the top performers in specific field. Give me a list of the most important lessons I can learn from these top performers to boost my productivity.'} ],
    [ {'role':'user', 'content':'I will tell you about what I am learning about. Ask me a series of questions that will test my knowledge. Identify knowledge gaps in my answers and give me better answers to fill those gaps.'} ],
    [ {'role':'user', 'content':'I will ask you to help me create a report on the specific subject or topic. Research and create an in-depth report with a step-by-step guide that will help readers understand it.'} ],
    [ {'role':'user', 'content':'I will ask you about the skill i want to learn. Generate a 30 day plan that will help a beginner like me learn the skill from scratch.'} ],
]

FILENAME_PRIVATE_PROMOTS = 'private_prompts.py'
if os.path.isfile(FILENAME_PRIVATE_PROMOTS):
    from private_prompts import PRIVATE_PROMPTS
    PROMPTS += PRIVATE_PROMPTS

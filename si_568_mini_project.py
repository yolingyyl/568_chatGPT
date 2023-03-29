# -*- coding: utf-8 -*-
"""SI 568 mini project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T1nqgGEU4J5h8c-j-c_QIM9vcEEYQSoK
"""

!pip install openai

# sample from playground: https://platform.openai.com/playground/p/default-vr-fitness?mode=complete&model=text-curie-001

import os
import openai
yoling_key = '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'
openai.api_key = yoling_key

def behavioral_questions(num = 5):
  jd = input('please enter the job description: ')
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Help me generate {num} behavioral questions based on the job description. \njob description: {jd}",
    temperature=0.94,
    max_tokens=2878,
    top_p=1,
    frequency_penalty=1,
    presence_penalty=1
  )

  response = response.choices[0]['text'][2:]
  return response, jd

def random_questions(num = 5):
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Help me generate {num} behavioral questions for the interview.",
  temperature=0.94,
  max_tokens=2878,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)

  response = response.choices[0]['text'][2:]
  return response

def sample_answer(question = '', resume = ''):
  if question == "":
    pass
  else:
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Help me generate the answer of the behavioral question based on my resume. \nbehavioral question: {question}\nresume: {resume}",
      temperature=0.94,
      max_tokens=2878,
      top_p=1,
      frequency_penalty=1,
      presence_penalty=1
    )
    response_raw = response
    response_trim = response.choices[0]['text'][2:]
    return response_raw, response_trim

def new_random_questions(ori, num = 5):
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Help me generate {num} new behavioral questions for the interview. I don't want these questions: {ori}",
  temperature=0.94,
  max_tokens=2878,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)

  response = response.choices[0]['text'][2:]
  return response

def new_behavioral_questions(ori, jd, num = 5):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Help me generate {num} behavioral questions based on the job description, and I don't want these questions: {ori} \njob description: {jd}",
    temperature=0.94,
    max_tokens=2878,
    top_p=1,
    frequency_penalty=1,
    presence_penalty=1
  )

  response = response.choices[0]['text'][2:]
  return response, jd

# scenario
print('''Hello, welcome to our behavioral question practice tool. 
We are here to help you prepare your customized answers for the behavioral questions. ''')

# collect resume 
resume = ''
while True: 
  if resume == '':
    resume = input('Please enter your resume in plain text: ')
    print('receiving ...')
  else: 
    print('We received your resume')
    break

question_type = input('''Please enter \'job description\' if you want us to generate possible behavioral questions based on the job description, 
or enter \'random\' for random selected questions: ''').lower()

# generate behavioral questions
question_lst = []
if question_type == 'job description':
  chat = behavioral_questions()
  q = chat[0]
  jd = chat[1]
  print(q)
  for a in q.split('\n'):
    question_lst.append(a)
elif question_type == 'random':
  q = random_questions()
  print(q)
  for a in q.split('\n'):
    question_lst.append(a)
else:
  while True: 
    question_type = input('''Please enter \'job description\' if you want us to generate possible behavioral questions based on the job description, 
or enter \'random\' for random selected questions: ''').lower()
    if question_type == 'job descripton' or question_type == 'random':
      break

# generate new questions or create sample answers

regenerate = input('Please enter \'next\' if you found these questions ok, or \'refresh\' if you want to regenerate the questions: ').lower()

if regenerate == 'refresh':
  if question_type == 'random':
      q = new_random_questions(ori = q)
      print(q)
      question_lst = []
      for a in q.split('\n'):
        question_lst.append(a)

  elif question_type == 'job description':
    chat = new_behavioral_questions(ori = q, jd = jd)
    q = chat[0]
    jd = chat[1]
    print(q)
    question_lst = []
    for a in q.split('\n'):
      question_lst.append(a)
elif regenerate == 'next':
  pass

ans = input('Do you want us to generate sample answers based on the behavioral questions above? Enter \'yes\' if you want or \'no\' if you\'re good.').lower()
if ans == 'yes':
  for a in question_lst:
    print(f'Question: {a} \n\nAnwser: {sample_answer(question = a, resume = resume)[1]}')
else:
  print('You are all set. Good luck with your interview')

q

q

q[1:]

chat


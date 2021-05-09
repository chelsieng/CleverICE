import os, json
import openai
from .config import Config

class openAI:
    prefix = 'Here is a claim letter from a customer to an insurance company.\
            Read the letter, then answer the following questions\n\n\
            """\n'
    answer_prefix = 'Answer:\nAnswer-1.'
    keywords = ['Name', 'Phone number', 'Insurance policy number', 'Email', 'Incident', 'Location of the incident', 'Requested money', 'Summary']

    def __init__(self):
       openai.api_key = Config.OPENAI_API_KEY
 
    def make_request(self, prompt, engine="davinci", stop=['/n/n'], max_tokens = 64, temperature = 0.5, echo = False, frequency_penalty = 0.2):
        """
        More info about the parameters: https://beta.openai.com/docs/api-reference/completions/create
        """
        response = openai.Completion.create(prompt=prompt, engine=engine, stop=stop, max_tokens=max_tokens, temperature=temperature, echo=echo, frequency_penalty = frequency_penalty)
        return response


    def scan(self, prompt):
        """
        Extract the general information from the claim letter.
        """
        prefix = 'Here is a claim letter from a customer to an insurance company.\
             Read the letter, then answer the following questions\n'
        suffix = 'Questions:\n\
            1. Customer\'s name?\
            \n2. Phone number of the customer?\
            \n3. Insurance policy number?\
            \n4. Email address of the customer?\
            \n5. What happened to the customer?\
            \n6. What is the location of the incident?\
            \n7. How much money does the customer ask for?\
            \n8. A short summary of the claim letter\n'

        # Append prefix and suffix to create meaningful query.
        prompt = self.prefix + prompt + '\n"""\n' + suffix + self.answer_prefix
        response = self.clean(self.make_request(prompt, temperature=0.6, max_tokens=250, frequency_penalty=0.2)).split('Answer-')
        print(self.extract(response))
        return response

    def extract(self, response):
        return json.dumps({self.keywords[i]: response[i][:-1] for i in range(len(self.keywords))}, indent=4)

    def clean(self, response):
        return response.choices[0].text

    def ask(self, content, question):
        """
        User asks a question about the content of the letter.
        """
        suffix = 'Question: \n' + question + '\nAnswer:'
        query = self.prefix + content + suffix
        response = self.clean(self.make_request(question, temperature=0.5, max_tokens=250))
        return response



"""
# Test

test_letter = 'Dear Sir/Madam, \
\
This letter is to formally request reimbursement for medical expenses for policy 135-8452-1268. I was visiting Niagara Fall last Sunday (May 2nd, 2021) where I fell and broke my wrist.\
\
I was treated at Toronto General Hospital, and because I was from out-of-state, I needed to pay the bill in full. The amount was $3500 for x-rays, a bone specialist and one night in the hospital.\
\
According to the terms of my policy, I contacted my primary healthcare physician within 24 hours of the accident. I have enclosed all the documents related to my treatment. I understand that I have a $500 deductible on my policy. I am requesting you to reimburse me $3000 in keeping with my health care coverage.\
\
I can be reached at 538-753-3578 or at christyang@gmail.com if you have any questions. Thank you for your quick attention to this.\
\
Sincerely,\
\
Christ'

model = openAI()
response = model.scan(test_letter)
"""

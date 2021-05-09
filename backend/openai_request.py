import os
import openai
from .config import Config

class openAI:
    prefix = 'Here is a claim letter from a customer to an insurance company.\
            Read the letter, then answer the following questions\n\n\
            """\n'
    answer_prefix = 'Answer:\n1.'

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
        print(prompt)
        response = self.clean(self.make_request(prompt, temperature=0.3, max_tokens=250, frequency_penalty=0.16))
        print(response)
        return response

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

    
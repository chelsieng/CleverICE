# :ice_cube: CleverICE	
A tool that helps automate the insurance claim process

## :bulb: Inspiration
Having an accident is already a bad thing, having to wait for the insurance claim to process is even worse. Sometimes, the customer could already have written an accident claim report prior to applying with the Insurance company. With the hope of improving customers' satisfaction, the claim letter can go reused and can help insurance companies speed up their processing time. Their customers now can rest assured that they will receive their claim faster than before.

## :thinking: What it does
CleverICE (or Clever Insurance Claim Extract) allows insurance companies to upload claim letters from their customers and get insights quickly. We leverage OCR Detection so users can upload their claim as a PDF file. With Generative Pre-trained Transformer 3 (GPT-3) from OpenAI, we are to automatically extract relevant information by summarizing it in the form of Q&A.

## :hammer_and_wrench: How we built it
We start by storing PDF files that users upload in Google Cloud Storage.
Then we convert documents from PDF to text using the Google Cloud Vision.
We store the extracted text in another bucket on Google Cloud Storage.
The paths to text and PDF files along with users' information are stored on CockroachDB.
Then we extract information and answer related questions using GPT-3 OpenAI.
We host the web on Heroku.
Front-end: Angular.
Back-end: Python with Flask to serve endpoints to the front-end. Connect to CockroachDB using SqlAchemy.

## :muscle: Challenges we ran into
405 error due to CORS policy that prevents us to send POST requests to the back-end
Team members are not familiar with the new API, take time to get the hang of it.
It's hard to calibrate the parameters of OpenAI to produce accurate results.
Accomplishments that we're proud of
We're proud to have been able to create a prototype in 24 hours! The back-end works well and endpoints work correctly as expected.

## :books: What we learned
We learn how to connect remotely to the SQL database
Learn how to leverage NLP with Open AI.

## :clapper: Demo


## How to run Backend
```
	$ pipenv shell
	$ pipenv install
	$ pip install -r requirements.txt
	$ python run.py
```
## How to run Frontend

```
	$ npm install
	$ npm run start
```

Angular app will be listening on http://localhost:4200/ 


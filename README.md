<p align="center">
	<img src = 'assets/logo.png'>
</p>

[A submission to ToHacks 2021](https://devpost.com/software/intact-insurance-challenge)


A tool that helps automate the insurance claim process

## :bulb: Inspiration
Having an accident is already a bad thing, having to wait for the insurance claim to process is even worse. Sometimes, the customer could already have written an accident claim report prior to applying with the Insurance company. With the hope of improving customers' satisfaction, the claim letter can go reused and can help insurance companies speed up their processing time. Their customers now can rest assured that they will receive their claim faster than before.

## :thinking: What it does
CleverICE (or Clever Insurance Claim Extract) allows insurance companies to upload claim letters from their customers and get insights quickly. We leverage OCR Detection so users can upload their claims as a PDF file. With Generative Pre-trained Transformer 3 (GPT-3) from OpenAI, we are to automatically extract relevant information by summarizing it in the form of Q&A.

## :hammer_and_wrench: How we built it
* We start by storing PDF files that users upload in Google Cloud Storage.
* Then we convert documents from PDF to text using the Google Cloud Vision.
* We store the extracted text in another bucket on Google Cloud Storage.
* The paths to text and PDF files along with users' information are stored on CockroachDB.
* Then we extract information and answer related questions using GPT-3 OpenAI.

#### Frontend: Angular

#### Backend: Python with Flask. CockroachDB using SqlAchemy as Database.

## :muscle: Challenges we ran into
* 405 error due to CORS policy that prevents us to send POST requests to the back-end
* It's hard to calibrate the parameters of OpenAI to produce accurate results.
* Heroku hosting errors

## :star: Accomplishments that we're proud of
We're proud to have been able to create a prototype in 24 hours! The back-end works well and endpoints work correctly as expected.

## :books: What we learned
* We learn how to connect remotely to the CockroachDB SQL database
* Learn how to leverage NLP with Open AI.
* OpenAI is awesome!

## :clapper: Demo

#### 1. Upload Doc
![upload-form](https://user-images.githubusercontent.com/60008262/117580252-232b0580-b0c5-11eb-9a74-50034803df75.png)


#### 2. After Submission
![uploaded](https://user-images.githubusercontent.com/60008262/117580269-35a53f00-b0c5-11eb-85e4-29edf50e3933.png)


#### 3. Claim information extracted
![info-extracted](https://user-images.githubusercontent.com/60008262/117580282-3dfd7a00-b0c5-11eb-9b7c-34fe843b54fd.png)

## :electric_plug: How to run Backend
```
	$ pipenv install
	$ pipenv shell
	$ pip install -r requirements.txt
	$ python run.py
```
## 💻 How to run Frontend

```
	$ npm install
	$ npm run start
```
CleverICE will be listening on http://localhost:4200/ 


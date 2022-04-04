# Author: Mettu Deepika
## Project1: The Redactor

This project will help us in detecting and redacting "sensitive" items such as names, dates, phone numbers, genders, addresses, and concepts. 

**The command used for running the project:**
pipenv run python main.py --input '*.txt' --names  --dates --address --genders --phones --concept 'kid' --output 'files' --stats stderr

**The command used for running the test scripts:**
pipenv run pytest test_main.py

**The modules used for the project:**
glob, os, re
nltk : pipenv install nltk
spacy : pipenv install spacy and !pipenv run python -m spacy download en_core_web_sm

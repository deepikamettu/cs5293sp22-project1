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

Running the project with the above command line argument will read all the .txt files in the current folder given by glob. All these files will be redated by the program. The program consists of two .py files namely redactor.py and main.py. Main.py parses the command line argument and each function is called to redaction process. 

The redactor.py contains the following functions:  

***inputData(files):***  
This function uses an --input flag argument for reading all the files in the current folder and appending the data(present in all the files) as a string to a list. This list is returned to the main function.  

***nameRedaction(data):***  
This function (uses --names flag argument) takes the list of data returned from the inputData(files) and searches for the entities that are labeled as ‘PERSON’  and ‘ORG’ in it. These texts are further redacted with Unicode █ (U+2588).  After redaction, the redacted data is appended to a list and sent to the main function for further redaction.  

***dateRedaction(data):***  
This function (uses --dates flag) now contains a list of data where the names are redacted. Entities with the label ‘DATE’ are searched in this list and redacted with Unicode █ (U+2588). This list is further passed to main function.  

***addressRedaction(data):***  
This function(uses --address flag) takes the list of data returned from dateRedaction(data) function and searches the entities with labels ‘LOC’ ‘FAC’  and ‘GPE’ and redacts those texts with Unicode █ (U+2588). This redacted list is returned to main function.  

***phoneRedaction(data):***  
This function(uses --phones flag) takes the list returned from the previous function and searches for phone numbers in the list using regular expressions. If there is a match, then the phone number is redacted with Unicode █ (U+2588).  

***genderRedaction(data):***  
This  function(uses --gender flag) takes the list of data and searches for gender related words like he|He|she|She|Him|him|her|Her|girl|Girl|boy|Boy|male|Male|female|Female|males|females|Males|Females|Women|Men|Woman|Man|women|men|woman|man and redacts with Unicode █ (U+2588).  

***conceptRedaction(data,concept):***  
This function(uses --concept flag along with concept) takes one word or phrase that represents a concept. A concept is either an idea or theme. Any word of the input files that refer to this concept word will be redacted with Unicode █ (U+2588).  

***statistics(li):***  
In nameRedaction() dateRedaction() addressRedaction() phoneRedaction() genderRedaction() and conceptRedaction() functions, statistical data regarding the frequency is calculated like:  
The number of “items” that are redacted : count(items)  
Where items = names, dates, address, phone numbers, gender, concepts and count(items) is calculated in it’s respective functions.  
The above information is appended to a list in each function and this list is passed as a parameter to statistics(). This function opens up the specified path('./stderr/stderr.txt')  and writes the statistical data into the stderr.txt file. If this file does not exist, then a file stderr.txt is created and data is written into it.  

***output(data):***  
This function is used to write the redacted data to a .redacted file. Meaning each redacted file will be transformed into new files of the same name with the .redacted extension and written to the files folder.  

**Assumptions:**  
1.	Phone numbers either be in ‘123 456 7890’ or ‘123-456-7890’ or ‘123.456.7890’ or '1234567890' format and will not be repeated more than once in the text file.  
2.	Dates will be in the format : ‘19 Jan 2001', '2005', 'Sunday', 'January'  
3.	Gender words that will be present in the text files will be among   he|He|she|She|Him|him|her|Her|girl|Girl|boy|Boy|male|Male|female|Female|males|females|Males|Females|Women|Men|Woman|Man|women|men|woman|man  
4.	Only .txt files are given as input arguments.  

**Test Cases:**  
Test cases are written in tests/test_main.py.  
1.	***test_inputData()***: This method is used to test inputData(files) function defined in redactor.py file and it asserts True if the inputData(files) function produces a list.  
2.	***test_nameRedaction()***: This method is used to test nameRedaction(data)  function defined in redactor.py file. In this method a sample list(names) is passed a parameter to nameRedaction(data) and the result is stored in a list variable called nameRedaction. This method asserts True iff the sample list and nameRedaction list have same length and nameRedaction list contains Unicode █(U+2588). Else asserts False.  
3.	***test_dateRedaction()***: This method is used to test  dateRedaction(data) function defined in redactor.py file. In this method a sample list(date) is passed a parameter to dateRedaction(data) and the result is stored in a list variable called dateRedaction. This method asserts True iff the sample list and dateRedaction have same length and dateRedaction contains Unicode █(U+2588). Else asserts False.  
4.	***test_addressRedaction()***: This method is used to test  addressRedaction(data) function defined in redactor.py file. In this method a sample list(address) is passed a parameter to addressRedaction(data) and the result is stored in a list variable called addressRedaction. This method asserts True iff the sample list and addressRedaction have same length and addressRedaction contains Unicode █(U+2588). Else asserts False.  
5.	***test_phoneRedaction()***: This method is used to test  phoneRedaction(data) function defined in redactor.py file. In this method a sample list(phoneNumber) is passed a parameter to phoneRedaction(data) and the result is stored in a list variable called phoneRedaction. This method asserts True iff the sample list and phoneRedaction have same length and phoneRedaction contains Unicode █(U+2588). Else asserts False.  
6.	***test_genderRedaction()***: This method is used to test genderRedaction(data)  function defined in redactor.py file.  In this method a sample list(gender) is passed a parameter to genderRedaction(data) and the result is stored in a list variable called genderRedaction. This method asserts True iff the sample list and genderRedaction have same length and genderRedaction contains Unicode █(U+2588). Else asserts False.  
7.	***test_conceptRedaction()***: This method is used to test conceptRedaction(data,concept)  function defined in redactor.py file.  In this method conceptRedaction(data,concept) is called and the result is stored in a list variable called conceptRedaction. This method asserts True iff the input data list and the redacted list have same length and the redacted list contains Unicode █(U+2588). Else asserts False.  
8.	***test_statistics()***: This method is used to test statistics(li) function defined in redactor.py file. This method asserts True if there exists a file named stderr.txt in project1/stderr/stderr.txt path else asserts False.  
9.	***test_output()***: This method is used to test output(data) function defined in redactor.py file. This method asserts True is there exists files with ‘.redacted’ extension in files folder else asserts False.  

**Bugs:**  
1.	Spacy detection is not accurate. Sometimes few entities are not recognized correctly.  
2.	In conceptRedaction(data) function, only the word that refers to the concept word is redacted instead of redacting the whole sentences.  

**References:**  
https://stackoverflow.com/questions/210518/regex-multi-word-search - used in genderRedaction()  
https://www.geeksforgeeks.org/get-synonymsantonyms-nltk-wordnet-python/ - used in conceptRedaction()  
https://stackoverflow.com/questions/35345761/python-re-split-vs-nltk-word-tokenize-and-sent-tokenize - used in conceptRedaction()  
https://stackoverflow.com/questions/51166970/how-can-i-check-if-only-txt-file-exists-in-a-directory-with-python - used in test_output()  
https://itsmycode.com/python-write-text-file/ and https://www.codegrepper.com/code-examples/python/python+create+text+file+in+specific+directory -	used in output(data)  
https://jcharistech.wordpress.com/2019/02/18/document-redaction-sanitization-using-spacys-named-entity-recognition/ and https://python.hotexamples.com/examples/spacy.tokens/Doc/retokenize/python-doc-retokenize-method-examples.html - used for name, address, date redaction


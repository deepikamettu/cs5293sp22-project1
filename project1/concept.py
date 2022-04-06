import nltk
import re
import os
import glob
import spacy
import sys
nltk.download('punkt')
nltk.download('words')
nltk.download('wordnet')
from nltk.corpus import wordnet
from os import path

nlp=spacy.load('en_core_web_sm')

def inputData(files):
    original = []
    [original.append(open(j,"r").read()) for i in  nltk.flatten(files) for j in glob.glob(i)]
    #print(original)
    return original

statsList = []

def nameRedaction(data):
    li =[]
    names = []
    originalData = data
    for d in originalData:
        docx = nlp(d)
        with docx.retokenize() as retokenizer:
            for ent in docx.ents:
                #print(ent.text,ent.label_)
                retokenizer.merge(ent)
                if ent.label_ == 'PERSON' or ent.label_ == 'ORG':
                    names.append(ent.text)
            #for token in docx:
                #print(token)
                #if token.ent_type_ == 'PERSON' or token.ent_type_ == 'ORG':
                    #names.append(token)
            #print("*****************NAMES****************")
            #print(names)
            for i in names:
                d=d.replace(str(i),"\u2588"*len(i))
            #print(i)
            #if i in names:
                #d.replace(i,"\u2588"*len(i))
        #data1 = " ".join(redacted_sentences)
        #print(data1)
        #li = list(data1.strip(" ").split("\n"))
        li.append(d)
    #print("***********************NAME**************")
    #print(li)
    nameRedactionCount = str(len(names))
    part ="Number of names that are redacted: "
    finalStat = part + nameRedactionCount
    #print(finalStat)
    statsList.append(finalStat)
    return li


def dateRedaction(data):
    li =[]
    dates = []
    address = []
    combine = []
    originalData = data
    for d in originalData:
        docx = nlp(d)  
        #print(docx)
        with docx.retokenize() as retokenizer:
            for ent in docx.ents:
                #print(ent.text,ent.label_)
                retokenizer.merge(ent)
                if ent.label_ == 'DATE':
                    dates.append(ent.text)
            #print("*********************DATES*************")
            #print(dates)
            for i in dates:
                d=d.replace(i,"\u2588"*len(i))
        li.append(d)
    dateReadctionCount = str(len(dates))
    part ="Number of dates that are redacted: "
    finalStat = part + dateReadctionCount
    statsList.append(finalStat)
    #print("*****************dates************")
    #print(li)
    return li

def addressRedaction(data):
    li = []
    address = []
    originalData = data
    for d in originalData:
        docx = nlp(d)
        with docx.retokenize() as retokenizer:
            for ent in docx.ents:
                retokenizer.merge(ent)
                if ent.label_ == 'LOC' or ent.label_ == 'GPE' or ent.label_ == 'FAC':
                    address.append(ent.text)
            #print(address)
            for i in address:
                #print("**************")
                #print(i)
                d = d.replace(i,"\u2588"*len(i))
        li.append(d)
        #print(li)
    addressRedactionCount = str(len(address))
    part = "Number of address that are redacted: "
    finalStat = part + addressRedactionCount
    statsList.append(finalStat)
    #print(li)
    return li


def phoneRedaction(data):
    mainData = []
    temp = []
    phoneNumbersList = []
    originalData = data
    for i in originalData:
        #phoneNumbersList = re.findall(r' \(?\+?[0-9][0-9]?[-\.\s]?\(?\d{3}\)?[-\.\s]?\(?\d{3}\)?[-\.\s]?\(?\d{4}\)?',i)
        #phoneNumbersList = re.findall(r'(i\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}',i)
        #print(phoneNumbersList)
        #if phoneNumbersList!=0:
            #print(phoneNumbersList)
        phoneNumbersList = re.findall(r' ([+]?\d{0,2}[ .-]?\(?\d{3,4}\)?[ .-]\d{3,4}[ .-]\d{4}|\d{10})',i)
        #phoneNumbersList = re.findall(r' ^\(?([0-9]{3})\)?[-.● '']?([0-9]{3})[-.● '']?([0-9]{4})$',i)
        print(len(phoneNumbersList))
        for j in phoneNumbersList:
            #print("**********************NUMBERS****")
            #print(j)
            #getting each length for replacing
            jLength = len(j)
            i = i.replace(str(j),u"\u2588" * jLength)
        mainData.append(i)
    phoneRedactionLength = str(len(phoneNumbersList))
    part = "Number of phone numbers that are redacted: "
    finalStat = part + phoneRedactionLength
    statsList.append(finalStat)    
    print("****************phone numbers***********************")
    #print(mainData)
    print(phoneRedactionLength)
    return mainData

def genderRedaction(data):
    mainList = []
    genderList = []
    count = 0
    #print(data)
    #data1 = nltk.word_tokenize(str(nlp(str(data))))
    #print(data1)
    #find = r'(he|He|she|She|Him|him|her|Her|girl|Girl|boy|Boy|male|Male|female|Female|males|females|Males|Females|Women|Men|Woman|Man|women|men|woman|man)'
    #find = r'(she|boy|her|him|Male|man|Women)'
    find = r'(\b he\b|\bHe\b|\bshe\b|\bShe\b|\bHim\b|\bhim\b|\bher\b|\bHer\b|\bgirl\b|\bGirl\b|\bboy\b|\bBoy\b|\bmale\b|\bMale\b|\bfemale\b|\bFemale\b|\bmales\b|\bfemale\b|\bMales\b|\bFemales\b|\bWomen\b|\bMen\b|\bWoman\b|\bMan\b|\bwomen\b|\bmen\b|\bwoman\b|\bman\b)'
    for i in data:
        #print(i)
        genderList = re.findall(find,i)
        #print(genderList)
        for j in genderList:
            #print(j)
            jLength = len(j)
            #print(len(j))
            #count = count + 1
            i = i.replace(j,"\u2588"*jLength)
        mainList.append(i)
    #print(genderList)
    '''for i in genderList:
        count = count + 1'''
    #print(count)
    #print(len(genderList))
    genderRedactionLength = str(len(genderList))
    part = "Number of genders that are redacted: "
    finalStat = part + genderRedactionLength
    statsList.append(finalStat)    
    #print(mainList)
    return mainList


def conceptRedaction(data,concept):
    synonyms= []
    redact = []
    dup = []
    li = []
    [redact.append(l.name()) for k in concept for syn in wordnet.synsets(k) for l in syn.lemmas()]
    data1 = nltk.word_tokenize(str(nlp(str(data))))
    [dup.append(i) for i in data1 if i in redact]
    for q in data:
        data2 = q.splitlines()
        #print(data1)
    for s in data2:
        for t in redact:
            if t in s:
                contains = s
                #print(i)
                li.append(contains)
                #print(li)
                #i = i.replace(str(l),"\u2588"*len(l))
        #synonyms.append(i)
    #print(li)
    #print(data2)
    for x in data2:
        #print(x)
        for y in li:
            if y in x:
                x = x.replace(str(y),"\u2588"*len(y))
        synonyms.append(x)
    conceptListLength = str(len(dup))
    #print(conceptListLength)
    part = "Number of concepts that are redacted: "
    finalStat = part + conceptListLength
    statsList.append(finalStat)
    #print("********************")
    #print(synonyms)
    #print(statsList)
    return synonyms


def statistics(filepath):
    #print(filepath)
    if filepath == 'stderr':
        file = open('./stderr/stderr.txt', "w", encoding="utf-8")
    else:
        file = open('./stdout/stdout.txt', "w", encoding="utf-8")
    li = statsList
    lengthFinalList = len(li)
    lengthFinalList = range(lengthFinalList)
    for i in lengthFinalList:
        each = li[i]
        print(each)
        file.write(each)
        file.write("\n")
    file.close()

def output(data):
    os.getcwd()
    filenames = []
    res = []
    [filenames.append(file) for file in glob.glob("*.txt")]
    for i in range(len(filenames)):
         res = [i.replace('.txt', '.redacted') for i in filenames]
    for k in range(len(filenames)):
        tempname = os.path.join('files/',res[k])
        with open(tempname,'w',encoding = 'utf-8') as tempfile:
            tempfile.write(data[k])
            tempfile.close()

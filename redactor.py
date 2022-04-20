import nltk
import re
import os
import glob
import spacy
import sys
import argparse
nltk.download('punkt')
nltk.download('words')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet
from os import path

nlp=spacy.load('en_core_web_md')

def inputData(files):
    original = []
    for x in files:
        [original.append(open(j,"r").read()) for i in  nltk.flatten(x) for j in glob.glob(i)]
    #print(original)
    return original

statsList = []

def nameRedaction(data):
    li =[]
    count = 0
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
            #count = count + len(names)
            #print(names)
            for i in names:
                d = d.replace(str(i),"\u2588"*len(i))
        li.append(d)
    #print(count)
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
    count = 0
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
            #count = count + len(dates)
            for i in dates:
                d=d.replace(i,"\u2588"*len(i))
        li.append(d)
    dateReadctionCount = str(len(dates))
    part ="Number of dates that are redacted: "
    finalStat = part + dateReadctionCount
    statsList.append(finalStat)
    return li

def addressRedaction(data):
    li = []
    count = 0
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
            count = count + len(address)
            #print(count)
            for i in address:
                #print("**************")
                #print(i)
                d = d.replace(i,"\u2588"*len(i))
        li.append(d)
        #print(li)
    #print(count)
    addressRedactionCount = str(len(address))
    part = "Number of address that are redacted: "
    finalStat = part + addressRedactionCount
    statsList.append(finalStat)
    #print(li)
    return li


def phoneRedaction(data):
    mainData = []
    temp = []
    count = 0
    phoneNumbersList = []
    originalData = data
    for i in originalData:
        phoneNumbersList = re.findall(r' ([+]?\d{0,2}[ .-]?\(?\d{3,4}\)?[ .-]\d{3,4}[ .-]\d{4}|\d{10})',i)
        count = count + len(phoneNumbersList)
        #print(count)
        for j in phoneNumbersList:
            jLength = len(j)
            i = i.replace(str(j),u"\u2588" * jLength)
        mainData.append(i)
    #print(count)
    #phoneRedactionLength = str(len(phoneNumbersList))
    part = "Number of phone numbers that are redacted: "
    finalStat = part + str(count)
    statsList.append(finalStat)    
    return mainData

def genderRedaction(data):
    mainList = []
    genderList = []
    count = 0
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
    data2 = []
    [redact.append(l.name()) for k in concept for syn in wordnet.synsets(k) for l in syn.lemmas()]
    data1 = nltk.word_tokenize(str(nlp(str(data))))
    [dup.append(i) for i in data1 if i in redact]
    for q in data:
        data2 = q.splitlines()
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
    part = "Number of concepts that are redacted: "
    finalStat = part + conceptListLength
    statsList.append(finalStat)
    #print("********************")
    #print(synonyms)
    #print(statsList)
    return synonyms


def statistics(filename):
    #print(filename)
    for i in range(len(filename)):
        if filename == ['stdout']:
            for i in statsList:
                sys.stdout.write(i + '\n')
        elif filename == ['stderr']:
            for k in statsList:
                sys.stderr.write(k + '\n')
        else:
            for i in range(len(filename)):
                    #print(filename[i])
                    file = open(filename[i],"w",encoding="utf-8")
                    for j in statsList:
                        #print(j)
                        file.write(j + '\n')
                    file.close()

def output(filelist,data):
    os.getcwd()
    filenames = []
    res = []
    for i in filelist:
        [filenames.append(file) for file in glob.glob(i)]
    #print(filenames)
    for i in range(len(filenames)):
         res = [i + '.redacted' for i in filenames]
    #print(res)
    #print(data)
    for k in range(len(filenames)):
        tempname = os.path.join('files/',res[k])
        with open(tempname,'w',encoding = 'utf-8') as tempfile:
            for sent in data:
                sent = sent +'\n'
                tempfile.write(sent)
        tempfile.close()



if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True, action='append', type=str)
    parser.add_argument("--names", action='store_true')
    parser.add_argument("--genders", action='store_true')
    parser.add_argument("--dates", action='store_true')
    parser.add_argument("--phones", action='store_true')
    parser.add_argument("--address", action='store_true')
    parser.add_argument("--concept", action='append', type=str)
    parser.add_argument("--stats", type=str,required=True,action ='append')
    parser.add_argument("--output",type=str,required=True)

    args = parser.parse_args()

    data = inputData(args.input)

    if (args.names):
        data = nameRedaction(data)
    if (args.genders):
        data = genderRedaction(data)
    if (args.dates):
        data = dateRedaction(data)
    if (args.concept):
        data = conceptRedaction(data, args.concept)
    if (args.phones):
        data = phoneRedaction(data)
    if (args.address):
        data = addressRedaction(data)
    if (args.output):
        output(args.input,data)
    if (args.stats):
        statistics(args.stats)

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
                retokenizer.merge(ent)
                if ent.label_ == 'PERSON' or ent.label_ == 'ORG':
                    names.append(ent.text)
            for i in names:
                d = d.replace(str(i),"\u2588"*len(i))
        li.append(d)
    nameRedactionCount = str(len(names))
    part ="Number of names that are redacted: "
    finalStat = part + nameRedactionCount
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
        with docx.retokenize() as retokenizer:
            for ent in docx.ents:
                retokenizer.merge(ent)
                if ent.label_ == 'DATE':
                    dates.append(ent.text)
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
            count = count + len(address)
            for i in address:
                d = d.replace(i,"\u2588"*len(i))
        li.append(d)
    addressRedactionCount = str(len(address))
    part = "Number of address that are redacted: "
    finalStat = part + addressRedactionCount
    statsList.append(finalStat)
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
        for j in phoneNumbersList:
            jLength = len(j)
            i = i.replace(str(j),u"\u2588" * jLength)
        mainData.append(i)
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
        genderList = re.findall(find,i)
        count = count + len(genderList)
        for j in genderList:
            jLength = len(j)
            i = i.replace(j,"\u2588"*jLength)
        mainList.append(i)
    part = "Number of genders that are redacted: "
    finalStat = part + str(count)
    statsList.append(finalStat) 
    return mainList


def conceptRedaction(data,concept):
    synonyms= []
    redact = []
    dup = []
    data2 = []
    [redact.append(l.name()) for k in concept for syn in wordnet.synsets(k) for l in syn.lemmas()] # redact list contains all the syns
    [data2.append(nlp(str(i))) for i in data]
    for q in data2:
        bol = True
        strings = str(q)
        sent_token_data = strings.splitlines(bol)
        for s in sent_token_data:
            for t in redact:
                if t in s:
                    s = s.replace(str(s),"\u2588"*len(s))
            synonyms.append(s)
            syn = ' '.join(synonyms)
        dup.append(syn)
        synonyms = []
    conceptListLength = str(len(dup))
    part = "Number of concepts that are redacted: "
    finalStat = part + conceptListLength
    statsList.append(finalStat)
    return dup


def statistics(filename):
    for i in range(len(filename)):
        if filename == ['stdout']:
            for i in statsList:
                sys.stdout.write(i + '\n')
        elif filename == ['stderr']:
            for k in statsList:
                sys.stderr.write(k + '\n')
        else:
            file = open(filename[i],"w",encoding="utf-8")
            for j in statsList:
                file.write(j + '\n')
            file.close()

def output(filelist,data,loc):
    os.getcwd()
    filenames = []
    res = []
    for i in filelist:
        [filenames.append(file) for file in glob.glob(i)]
    for i in range(len(filenames)):
         res = [i + '.redacted' for i in filenames]
    check = loc.endswith('/')
    if check == False:
        loc = loc + '/'
    exist = os.path.exists(loc)
    if exist == False:
        os.makedirs(loc)
    for k in range(len(res)):
        tempname = os.path.join(loc,res[k])
        with open(tempname,'w',encoding = 'utf-8') as tempfile:
            tempfile.write(data[k])
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
        output(args.input,data,args.output)
    if (args.stats):
        statistics(args.stats)

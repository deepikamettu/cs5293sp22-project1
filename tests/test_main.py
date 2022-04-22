import sys
sys.path.append('..')
import pytest
import redactor
import os

file_list = ['*.txt']
concept = ['kid']

def test_inputData():
    inputData = redactor.inputData(file_list)
    if(type(inputData)==list):
        assert True
    else:
        assert False

def test_nameRedaction():
    name = ['My name is Mettu Deepika']
    nameRedaction = redactor.nameRedaction(name)
    if len(nameRedaction) == len(name):
        if '\u2588' in nameRedaction:
            assert True
    else:
        assert False

def test_dateRedaction():
    date = ['20 March 2022 is a holiday']
    dateRedaction = redactor.dateRedaction(date)
    if len(dateRedaction) == len(date):
        if '\u2588' in dateRedaction:
            assert True
    else:
        assert False

def test_addressRedaction():
    address = ['I live at 1800 Beaumont Drive']
    addressRedaction = redactor.addressRedaction(address)
    if len(addressRedaction) == len(address):
        if '\u2588' in addressRedaction:
            assert True
    else:
        assert False

def test_phoneReadction():
    phoneNumber = ['My Phone Numbers are 123-456-7890 and 129 374 7390']
    phoneRedaction = redactor.phoneRedaction(phoneNumber)
    if len(phoneRedaction) == len(phoneNumber):
        if '\u2588' in phoneRedaction:
            assert True
    else:
        assert False

def test_genderRedaction():
    gender = ['All men and women are equal']
    genderRedaction = redactor.genderRedaction(gender)
    if len(genderRedaction) == len(gender):
        if '\u2588' in genderRedaction:
            assert True
    else:
        assert False

def test_concept():
    conceptList = ['All kids are not allowed to eat in class']
    conceptRedaction = redactor.conceptRedaction(conceptList,concept)
    if len(conceptRedaction) == len(conceptList):
        if '\u2588' in conceptRedaction:
            assert True
    else:
        assert False

def test_statistics():
    filename = ['xyz']
    res = redactor.statistics(filename)
    res1 = os.path.exists(filename[0])
    if res1 == True:
        assert True
    else:
        assert False


def test_output():
    data = ['This is first file','This is second file']
    loc = 'files/'
    file_list = ['1.txt','2.txt']
    redactor.output(file_list,data,loc)
    os.chdir(loc)
    li = os.listdir()
    for i in li:
        if i.endswith('.redacted'):
            assert True
        else:
            assert False



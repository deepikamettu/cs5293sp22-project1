import sys
sys.path.append('..')
import pytest
from project1 import redactor
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
    inputData = redactor.inputData(file_list)
    conceptRedaction = redactor.conceptRedaction(inputData,concept)
    if len(conceptRedaction) == len(inputData):
        if '\u2588' in conceptRedaction:
            assert True
    else:
        assert False

def test_statistics():
    filename = 'xyz'
    os.chdir('../')
    os.chdir('project1/')
    res = redactor.statistics(filename)
    res1 = os.path.exists(filename)
    if res1 == True:
        assert True
    else:
        assert False


def test_output():
    data = ['This is a file']
    os.chdir('../')
    os.chdir('project1/')
    redactor.output(data,file_list)
    os.chdir('files/')
    li = os.listdir()
    for i in li:
        if i.endswith('.redacted'):
            assert True
        else:
            assert False



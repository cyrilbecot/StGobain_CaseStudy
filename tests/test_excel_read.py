import pytest
from data_reader.data_reader import DataReader

@pytest.fixture
def read_test_excel_1():
    path="tests/test_data/TestExcelFile.xlsx"
    data=DataReader(path=path,sheet_name='Sheet1')

    tmp=data.content()
    yield tmp

@pytest.fixture
def read_test_excel_2():
    path="tests/test_data/TestExcelFile.xlsx"
    data=DataReader(path=path,sheet_name='Sheet2',skiprows=1)

    tmp=data.content()
    yield tmp

def test_content_1(read_test_excel_1):
    x=read_test_excel_1
    assert ((x.loc[1,'A']==6) and (x.loc[2,'B']==8))

def test_content_2(read_test_excel_2):
    x=read_test_excel_2
    assert ((x.loc[0,'D']=="Retest") and (x.loc[1,'F']=="Retest3"))


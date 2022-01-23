import pytest
from data_reader.data_reader import DataReader
from data_reader.helpers import DataTypes

@pytest.fixture
def read_test_csv():
    path="tests/test_data/test_simple_csv.csv"
    data=DataReader(path=path, dt=DataTypes.Excel)

    tmp=data.content()
    yield tmp

def test_content(read_test_csv):
    x=read_test_csv
    assert ((x.loc[1,'A']==2) and (x.loc[2,'B']==6))

def test_length(read_test_csv):
    assert (len(read_test_csv) == 3)

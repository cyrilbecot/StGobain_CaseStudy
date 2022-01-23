import pytest
from data_reader.data_reader import DataReader
from data_reader.helpers import DataTypes

@pytest.fixture
def read_test_csv():
    path="tests/test_data/test_simple_csv.csv"
    data=DataReader(path=path, dt=DataTypes.CSV)

    tmp=data.content()
    yield tmp

@pytest.fixture
def open_real_file():
    path="input_data/Referendum.csv"
    data=DataReader(path=path)
    yield data.content()



def test_other_read(read_test_csv):
    path="tests/test_data/test_simple_csv.csv"
    data=DataReader(path=path)

    # One all to go from full table to feature (check series), 2nd for equality
    assert (data.content()==read_test_csv).all().all()

def test_content(read_test_csv):
    x=read_test_csv
    assert ((x.loc[1,'A']==2) and (x.loc[2,'B']==6))

def test_length(read_test_csv):
    assert (len(read_test_csv) == 3)

def test_real_length(open_real_file):
    assert(len(open_real_file) == 36791)

def test_real_index(open_real_file):
    assert(len(open_real_file.columns) == 9)

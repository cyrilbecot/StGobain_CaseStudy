import pytest
import pandas
from data_reader.data_reader import DataReader

@pytest.fixture
def read_test_geo_2column():
    path="tests/test_data/test_csv_geocode_builder_1.csv"
    data=DataReader(path=path,insee_code=('code_part1','code_part2'))

    tmp=data.content()
    yield tmp



def test_geo1(read_test_geo_2column):
    res_series=pandas.Series(['01038','22134','97025'])
    print(read_test_geo_2column['insee'])

    assert (read_test_geo_2column.insee==res_series).all()

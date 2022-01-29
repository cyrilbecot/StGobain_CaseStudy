import pytest
import pandas
from data_reader.data_reader import DataReader

@pytest.fixture
def read_test_geo_2column():
    path="tests/test_data/test_csv_geocode_builder_1.csv"
    data=DataReader(path=path,insee_code=('code_part1','code_part2'))

    tmp=data.content()
    yield tmp

@pytest.fixture
def read_test_geo_2column_noDomTom():
    path="tests/test_data/test_csv_geocode_builder_1.csv"
    data=DataReader(path=path,insee_code=('code_part1','code_part2'),drop_domtom=True)

    tmp=data.content()
    yield tmp



def test_geo_all(read_test_geo_2column):
    res_series=pandas.Series(['01038','22134','97025'])

    assert (read_test_geo_2column.insee==res_series).all()



def test_geo_drop_domtom(read_test_geo_2column_noDomTom):
    res_series=pandas.Series(['01038','22134'])

    assert (read_test_geo_2column_noDomTom.insee==res_series).all()

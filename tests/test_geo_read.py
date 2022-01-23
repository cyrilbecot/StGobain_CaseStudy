import pytest
from data_reader.data_reader import DataReader
import geopandas as gpd

@pytest.fixture
def read_earth_lowres():
    p=gpd.datasets.get_path("naturalearth_lowres")
    d=gpd.read_file(p)
    yield d

def test_len_earth_lowres(read_earth_lowres):
    assert (len(read_earth_lowres) == 177)

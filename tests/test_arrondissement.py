import pytest
import pandas as pd
from data_reader.data_reader import DataReader

@pytest.fixture
def read_del_arrond():
    path="tests/test_data/test_csv_arrondissements.csv"
    data=DataReader(path=path,insee_code=('code_part1','code_part2'),arrondissement_handling="Delete")
    yield data.content()


def test_del_length(read_del_arrond):
    assert (len(read_del_arrond)==1)


def test_del_content(read_del_arrond):
    assert (read_del_arrond.Ville.reset_index(drop=True)==pd.Series(['Tripouillis'])).all()

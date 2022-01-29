import pytest
import pandas as pd
from data_reader.data_reader import DataReader

@pytest.fixture
def read_del_arrond():
    path="tests/test_data/test_csv_arrondissements.csv"
    data=DataReader(path=path,insee_code=('code_part1','code_part2'),arrondissement_handling="Delete")
    yield data.content()

@pytest.fixture
def read_merge_arrond():
    path="tests/test_data/test_csv_arrondissements.csv"
    data=DataReader(path=path,insee_code=('code_part1','code_part2'),arrondissement_handling="Merge")
    yield data.content()


def test_del_length(read_del_arrond):
    assert (len(read_del_arrond)==1)

def test_del_content(read_del_arrond):
    assert (read_del_arrond.libgeo.reset_index(drop=True)==pd.Series(['Tripouillis'])).all()

def test_merge_content_1(read_merge_arrond):
    assert (read_merge_arrond.libgeo.reset_index(drop=True)==pd.Series(['Tripouillis','Paris'])).all()

def test_merge_content_2(read_merge_arrond):
    assert (read_merge_arrond.loc['75056','B']==15)

def test_merge_length(read_merge_arrond):
    assert (len(read_merge_arrond)==2)

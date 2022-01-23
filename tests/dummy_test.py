import pytest
import pandas as pd

@pytest.fixture
def dummy_data():
    dummy={
        'A': [1,2,3],
        'B': [4,5,6]
    }
    yield pd.DataFrame(dummy)


def test_length(dummy_data):
    assert len(dummy_data)==3

def test_value(dummy_data):
    assert ((dummy_data.loc[1,'B']==5) and (dummy_data.loc[1,'A']==2))

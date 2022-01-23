import pandas, geopandas
from enum import Enum

class DataTypes(Enum):
    Void=0
    GeoShape=1
    Excel=2
    CSV=3

def get_read_fcn(dt: DataTypes):
    if dt == DataTypes.Excel:
        return pandas.read_csv

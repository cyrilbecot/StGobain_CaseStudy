import pandas, geopandas
from enum import Enum

class DataTypes(Enum):
    Void=0
    GeoShape=1
    Excel=2
    CSV=3

def get_read_fcn(dt: DataTypes):
    if dt == DataTypes.CSV:
        return pandas.read_csv

def locations(which):
    res={
            'referundum':'/input_data/Referundum.csv',
            'geodata':'/input_data/GeoShapeCommunes/communes-20220101.shp',
            'recensement':'/input_data/base-cc-evol-struct-pop-2013/base-cc-evol-struct-pop-2013.xls',
            'revenus':'/input_data/filo-revenu-pauvrete-menage-2013/filo-revenu-pauvrete-menage-2013.xls',
            'diplomes':'/input_data/pop-16ans-dipl6817/pop-16ans-dipl6817.xlsx'
        }
    return res[which]

import pandas, geopandas
from enum import Enum

class DataTypes(Enum):
    Void=0
    GeoShape=1
    Excel=2
    CSV=3

def locations(which):
    """Helper function to locate the different databases I'll look at"""
    res={
            'referendum':'/input_data/Referendum.csv',
            'geodata':'/input_data/GeoShapeCommunes/communes-20220101.shp',
            'recensement':'/input_data/base-cc-evol-struct-pop-2013/base-cc-evol-struct-pop-2013.xls',
            'revenus':'/input_data/filo-revenu-pauvrete-menage-2013/filo-revenu-pauvrete-menage-2013.xls',
            'diplomes':'/input_data/pop-16ans-dipl6817/pop-16ans-dipl6817.xlsx'
        }
    return res[which]

def age_class():
    res = {
        '0014': (0,14),
        '1529': (15,29),
        '3044': (29,44),
        '4559': (45,59),
        '6074': (60,74),
        '7589': (75,89),
        '90P': (90,90)
          }
    return res

def mean_age(x,suffix='P13_POP'):
    tot_pop=0.
    tot_age=0.

    for idx,val in age_class().items():
        current_pop = x[suffix+idx]
        age=(val[0]+val[1])/2.
        tot_age += current_pop*age
        tot_pop += current_pop

    return tot_age/tot_pop

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
            'diplomes':'/input_data/pop-16ans-dipl6817/pop-16ans-dipl6817.xlsx',
            'diploma_helper':'/input_data/HelperDataframeDiploma.csv'
        }
    return res[which]



def diploma_class():
    """Converts diploma numbers into the equivalent age at which someone who doesn't double would finish
    Put 6 for people without diplomas"""
    res = {
        0: 6, #No diploma
        1: 11, #CEP
        2: 14, #BEPC
        3: 16, #Bac
        4: 18,
        5: 21,
        6: 24
    }
    return res

def mean_diploma(x,helper_df):
    tot_pop=0.
    tot_diploma=0.

    diplomas = helper_df.columns
    for col in diplomas:
        current_diploma=diploma_class()[helper_df[col]["DIPLÔME"]]
        current_pop=x[col]
        tot_pop += current_pop
        tot_diploma += current_pop*current_diploma

    return tot_diploma/tot_pop


def socio_pro_class():
    res = {
        'C13_POP15P_CS1': 'Agriculteurs',
        'C13_POP15P_CS2': 'Artisans/commercants',
        'C13_POP15P_CS3': 'Cadres',
        'C13_POP15P_CS4': 'Profs',
        'C13_POP15P_CS5': 'Employés',
        'C13_POP15P_CS6': 'Ouvriers',
        'C13_POP15P_CS7': 'Retraites',
        'C13_POP15P_CS8': 'Autres'
    }
    return res


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

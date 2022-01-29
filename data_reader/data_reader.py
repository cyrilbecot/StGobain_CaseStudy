from dataclasses import dataclass
import pandas as pd
import geopandas as gpd

from data_reader.helpers import DataTypes


@dataclass
class DataReader():
    """
    Class that will be used to read all the
    datasets for this project, whatever there
    format is : geodata is shapefile, XLS, or XSV
    """

    path: str #Place at which the data is stored
    sheet_name: str="" #For excel files with >1sheet : which one to use
    dt: DataTypes=DataTypes.Void
    dc: pd.DataFrame=pd.DataFrame() # Will contain the actual data
    encoding: str='utf-8'
    sep: str=';'
    skiprows: int=-1
    rm_nan: bool=False
    insee_code: tuple=()


    def __post_init__(self):
        """This will read in the data, using the proper datatype,
            potentially detecting it if it wasn't filled"""

        if self.dt == DataTypes.Void:
            self.determine_type()

        self.read()

        if self.rm_nan:
            self.dropna(inplace=True)

        self.insee_code_builder(self.insee_code)


    def insee_code_builder(self,incode):
        """Will either take two columns to build the INSEE code out of it,
                or will rename the column that already contains it"""
        if len(incode)==2:
            dept,city=incode

            self.dc[dept] = self.dc[dept].map(lambda x: str(x).rjust(2,'0'))
            self.dc[city] = self.dc[city].map(lambda x: str(x).rjust(3,'0'))

            fnc=lambda x: x[dept]+x[city]
            self.dc=self.dc.assign(insee=fnc)


    def determine_type(self):
        """Determine the file type to chose the reader"""
        support_types = {
                "csv": DataTypes.CSV,
                "xls": DataTypes.Excel,
                "shp": DataTypes.GeoShape
            }
        for t in support_types:
            if t in self.path.lower():
                self.dt = support_types[t]
                break
        else:
            exit("DataTypes cannot be detected")


    def dropna(self, **kwargs):
        """Drop NaNs from the inner dataframe"""
        tmp=self.dc.dropna(kwargs)
        if not inplace:
            return tmp


    def read(self):
        """Actually read data"""
        if self.dt == DataTypes.CSV:
            self.dc = pd.read_csv(self.path, encoding=self.encoding, sep=self.sep)
        elif self.dt == DataTypes.Excel:
            self.dc = pd.read_excel(self.path,sheet_name=self.sheet_name,skiprows=self.skiprows)
        elif self.dt == DataTypes.GeoShape:
            self.dc = gpd.read_file(self.path)
        else:
            exit("DataTypes isn't recognized")


    def content(self):
        return self.dc

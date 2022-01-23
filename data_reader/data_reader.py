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

    def __post_init__(self):
        """This will read in the data, using the proper datatype,
            potentially detecting it if it wasn't filled"""

        if self.dt == DataTypes.Void:
            self.determine_type()

        self.read()

    def determine_type(self):
        support_types = {
                "csv": DataTypes.CSV,
                "xls": DataTypes.Excel
            }
        for t in support_types:
            if t in self.path.lower():
                self.dt = support_types[t]
                break
        else:
            exit("DataTypes cannot be detected")

    def read(self):
        if self.dt == DataTypes.CSV:
            self.dc = pd.read_csv(self.path, encoding=self.encoding, sep=self.sep)
        elif self.dt == DataTypes.Excel:
            self.dc = pd.read_excel(self.path,sheet_name=self.sheet_name,skiprows=self.skiprows)

    def content(self):
        return self.dc

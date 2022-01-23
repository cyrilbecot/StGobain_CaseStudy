from dataclasses import dataclass
import pandas, geopandas

from data_reader.helpers import DataTypes, get_read_fcn


@dataclass
class DataReader():
    """
    Class that will be used to read all the
    datasets for this project, whatever there
    format is : geodata is shapefile, XLS, or XSV
    """

    path: str #Place at which the data is stored
    sheet_id: str="" #For excel files with >1sheet : which one to use
    dt: DataTypes=DataTypes.Void
    dc=None # Will contain the actual data

    def __post_init__(self):
        if not self.dt == DataTypes.Void:
            self.dc = get_read_fcn(self.dt)(self.path)
        else:
            exit("Problem : DataType is Void")

    def content(self):
        return self.dc

FROM nvidia/cuda:11.4.1-devel-ubuntu20.04

RUN apt-get update
RUN apt-get install -y pip wget unzip

RUN pip install notebook pandas geopandas seaborn

RUN mkdir /input_data
COPY input_data/Referendum.csv /input_data
COPY input_data/data_downloader.sh /input_data
RUN chmod +x /input_data/data_downloader.sh ; cd /input_data ; ./data_downloader.sh

RUN mkdir /Work

RUN pip install openpyxl xlrd

COPY input_data/HelperDataframeDiploma.csv /input_data
RUN pip install jupyterlab statsmodels

WORKDIR /Work
CMD jupyter lab --ip 0.0.0.0 --allow-root --NotebookApp.iopub_data_rate_limit=1.0e10
# TaxiDataPipeLine
Project to create a simple data pipeline using Yellow Taxis trip data

## Content

* [src](src/) - Python source code
* [test](test/) - Unit test
* [docs](docs/) - Project documentation


## Getting Started

Follow these instructions to get the source code and run it on your local machine.

### Prerequisites

You need `Python 3.7.3` ([Official download link](https://www.python.org/downloads/release/python-373/)) to run this project.
Additionally, it has been developed on a Windows 10 PC, so the command written below are specific to Windows environment.

### Clone repository
```sh
git clone https://github.com/write2sushma/TaxiDataPipeLine.git
```

### Set-up development environment

* Navigate to TaxiDataPipeLine folder
```sh
cd TaxiDataPipeLine
```

* Create a virtual environment and activate it
```sh    
python -m venv env
env\Scripts\activate
```  

* Install project dependencies 
Project dependencies are listed in `requirements.txt` file
```sh    
pip install -r requirements.txt
```    
To install `dask` using `pip`, use the below command in command prompt/terminal window:
```sh
pip install “dask[complete]”

pip install dask distributed
```

### How to run

Navigate to `TaxiDataPipeLine\src` folder and run `data_processor.py`

```sh
python data_processor.py
```

### How to Unit Test

Unit tests are written using Python's UnitTest library. Tests can be run using below command:
```sh
python -m unittest test/test_data_processor.py
```


## Data Source
Here is the list of data source urls used for creating data Pipe Line -

    https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-01.csv
    https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-02.csv
    https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-03.csv
    https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-04.csv
    https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-05.csv
    https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-06.csv
    
## Future Enhancement Plan:    
    • Create a Python setup/installer for distribution 	
    • Optimize performance using asyncio and dask scheduler
    • Scale pipeline to a multiple of the data size that does not fit any more to one machine using multinode clusters in cloud (e.g. AWS)
    • Setup automated build
    

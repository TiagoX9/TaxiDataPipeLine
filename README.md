# TaxiDataPipeLine
Project to create a simple data pipeline using Yellow Taxis trip data

## Content

* [docs](docs/) - Project documentation
* [src](src/) - Python source code
* [test](test/) - Unit test


## Getting Started

Follow these instructions to get the source code and run it on your local machine.

### Prerequisites

  You need `Python 3.7.3` ([Official download link](https://www.python.org/downloads/release/python-373/)) to run this project.

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

  In Linux OS
  ```sh    
  python3 -m venv env
  source env\bin\activate
  ```  

  In Windows OS
  ```sh    
  python -m venv env
  env\Scripts\activate
  ```  

* Install project dependencies 

  Project dependencies are listed in `requirements.txt` file. Use below command to install them -
  ```sh    
  pip3 install -r requirements.txt
  ```    
  
  If there is any issue in installing dask using `requirements.txt` file, use the below commands in command prompt/terminal window:
  ```sh
  pip3 install “dask[complete]”

  pip3 install dask distributed
  ```

### How to run

  Navigate to `TaxiDataPipeLine\src` folder and run `data_processor.py`

  ```sh
  python data_processor.py
  ```

### How to Unit Test

  Unit tests are written using Python's UnitTest library. Tests can be run using below command:
  ```sh
  cd test
  pytest test_data_processor.py
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
    • Current implementation runs in a single process using single thread. Use ProcessPoolExecutor/asyncio for faster parallel/concurrent executaion.
    • Create a Python setup/installer for distribution 	
    • Optimize performance using asyncio and dask scheduler
    • Scale pipeline to a multiple of the data size that does not fit any more to one machine using multinode clusters in cloud (e.g. AWS)
    • Setup automated build
    • Setup performance monitoring (e.g. using New Relic)
    

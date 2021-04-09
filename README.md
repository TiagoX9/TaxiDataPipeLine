<!-- TOC -->
- [Description](#description)
- [Build Status](#build-status)
- [Content](#content)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Clone repository](#clone-repository)
- [Set-up development environment](#set-up-development-environment)
  - [Navigate to source folder](#navigate-to-source-folder)
  - [Create a virtual environment](#create-a-virtual-environment)
  - [Install project dependencies](#install-project-dependencies)
- [How to run](#how-to-run)
- [How to Unit Test](#how-to-unit-test)
- [How to check coverage](#how-to-check-coverage)
- [Data Source](#data-source)
- [Automated build setup](#automated-build-setup)
- [Future Enhancement Plan:](#future-enhancement-plan)
<!-- /TOC -->

# Description
TaxiDataPipeLine is an application to demonstrate creation of a simple data pipeline using Yellow Taxis trip data.

## Build Status

|   | Build & Test |
|---|:-----:|
|**Windows x64**|![Build & Test][win-x64-build-badge]
|**Linux x64**|![Build & Test][linux-x64-build-badge]

[win-x64-build-badge]: https://mseng.visualstudio.com/pipelinetools/_apis/build/status/VSTS.Agent/azure-pipelines-agent.ci?branchName=master&jobname=Windows%20Agent%20(x64)
[linux-x64-build-badge]: https://mseng.visualstudio.com/pipelinetools/_apis/build/status/VSTS.Agent/azure-pipelines-agent.ci?branchName=master&jobname=Linux%20Agent%20(x64)

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

#### Navigate to source folder
  ```sh
  cd TaxiDataPipeLine
  ```

#### Create a virtual environment

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

#### Install project dependencies 

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

  Navigate to `TaxiDataPipeLine\taxidata` folder and run `data_processor.py`

  ```sh
  python data_processor.py
  ```

### How to Unit Test

  Unit tests are written using Python's UnitTest library. Tests can be run using below command:
  ```sh
  pytest
  
  or 
  
  python -m unittest test\test_data_processor.py
  ```

### How to check coverage

  Run below command to check code coverage:
  ```sh
  python -m coverage run test\test_data_processor.py
  ```
  And, then we can see coverage and can generate coverage report in html format
  ```sh
  coverage report
  coverage html
  ```

## Data Source
  Here is the list of data source urls used for creating data Pipe Line -

    https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-01.csv
    https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-02.csv
    https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-03.csv
    https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-04.csv
    https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-05.csv
    https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-06.csv
    
## Automated build setup
Azure DevOp Pipeline is used to set and configure [Automated build pipeline](https://sushmag.visualstudio.com/TaxiDataPipeLine)
    
## Future Enhancement Plan:    
    • Optimize performance using dask scheduler to enable faster parallel processing.
        - This is already implemented in 'enhancements' feature branch.
    • Scale pipeline to a multiple of the data size that does not fit any more to one machine using multinode clusters in cloud (e.g. AWS)
    • Setup performance monitoring 
    • Automate deployment using Azure DevOp Pipeline 
    

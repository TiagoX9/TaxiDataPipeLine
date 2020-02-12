"""
This module provides analysis of NYC Yellow Taxi data
"""

import argparse
import logging

import dask.dataframe as dd
import pandas as pd
from dask.diagnostics import ProgressBar

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def initialize():
    fileHandler = logging.FileHandler('pipeline.log')
    fileHandler.setLevel(logging.INFO)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)

    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)


def clean_data(df, index):
    """
    Cleans up data so that only relevant data is processed during calculations.
    :param df: Data Frame to analyse
    :param index: Month of trip data
    :return: Cleaned up data frame
    """
    logger.info("Cleaning up csv data")
    df = df[(df['passenger_count'] > 0) &
            (df['trip_distance'] > 0) &
            (df['tpep_pickup_datetime'] < df['tpep_dropoff_datetime']) &
            (df['tpep_pickup_datetime'].dt.month == index + 1) &
            (df['tpep_dropoff_datetime'].dt.month == index + 1) &
            (df['tpep_pickup_datetime'].dt.year == 2019) &
            (df['tpep_dropoff_datetime'].dt.year == 2019)
            ]
    # Drop the rest
    df = df.dropna()

    return df


def read_trip_data(url):
    """
    Loads CSV file in chunks of 100 MB and return dataframe
    :param url: url for loading csv data
    :return: dataframe
    """
    if len(url) == 0:
        logger.warning("Please provide a non empty url.")
        return

    try:
        logger.info(f"Reading csv file: {url}")
        df = dd.read_csv(url, blocksize=100e6, parse_dates=['tpep_pickup_datetime', 'tpep_dropoff_datetime'])
    except Exception as ex:
        logger.error(f"Reading file from {url} failed with error : {ex}")

    logger.debug(f'Reading completed for url {url}')
    return df


def calculate_monthly_average(df):
    """
    Calculates average trip length per month
    :param df: dataframe
    :return: Average trip length per month
    """
    logger.info("Calculating trip length average")

    with ProgressBar():
        df['month'] = df['tpep_pickup_datetime'].dt.strftime("%B")
        try:
            monthly_average = df.groupby(df['month'])['trip_distance'].mean().compute()
        except Exception as ex:
            logger.error(f"Monthly Average calculation failed with error : {ex}")


    logger.debug("Calculation of monthly trip length average completed")
    return monthly_average


def rolling_average(df):
    """
    This function calculates rolling average per month.
    :param df: dataframe
    :return: Rolling average per month
    """
    logger.info("Calculating rolling trip length average")

    with ProgressBar():
        # Convert to pandas dataframe
        dfp = df.compute()
        dfp['month'] = pd.to_datetime(dfp['tpep_pickup_datetime']).dt.strftime("%B")
        try:
            r_average = dfp.groupby(dfp['month'])['trip_distance'].rolling(45).mean().reset_index(name='Rolling Average')
        except Exception as ex:
            logger.error(f"Rolling Average calculation failed with error : {ex}")

    logger.debug("Calculation of rolling monthly trip length average is completed")
    return r_average


def main():
    """
    Processes data source files (in CSV format) in a loop.
    :return:
    """
    initialize()

    logger.info('*** Application started ***')
    index = 0
    while index < 6:
        url = 'https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-0' + str(index + 1) + '.csv'
        df = read_trip_data(url)

        df = clean_data(df, index)

        # Calculate monthly average
        avg_trip_length = calculate_monthly_average(df)
        print(avg_trip_length)

        # Calculate Rolling average
        rolling_trip_length = rolling_average(df)
        print(rolling_trip_length)

        index += 1


if __name__ == '__main__':
    main()

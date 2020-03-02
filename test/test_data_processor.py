import os
import unittest
from pathlib import Path

import dask.dataframe as dd
from taxidata import data_processor


class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        current_dir = Path(__file__).parent
        print(current_dir)
        data_file = os.path.join(current_dir, 'data/testdata.csv')
        self.df = data_processor.read_trip_data(data_file)

    def tearDown(self):
        """ Executed after every test case """
        print("\ntearDown executing after the test case.")

    def test_read_trip_data(self):
        self.assertEqual(len(self.df.columns), 18)
        self.assertEqual(len(self.df), 11)

    def test_invalid_csv(self):
        invalid_file = "404.csv"

        with self.assertRaises(FileNotFoundError):
            df = dd.read_csv(invalid_file)

    def test_clean_data(self):
        df = data_processor.clean_data(self.df, 0)
        self.assertEqual(len(self.df), 11)

    def test_calculate_monthly_average(self):
        avg_value = data_processor.calculate_monthly_average(self.df)
        self.assertGreaterEqual(avg_value.January, 2.3)

    def test_rolling_average(self):
        rolling_avg = data_processor.rolling_average(self.df)
        self.assertEqual(rolling_avg.size, 33)


if __name__ == '__main__':
    unittest.main()

import unittest
import pandas as pd

class TestBrentOilDataAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load the dataset for testing
        cls.df = pd.read_csv('../data/brentOilPrices.csv')
    
    def test_data_loading(self):
        """ Test if the data is loaded correctly """
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertFalse(self.df.empty)
        
    def test_column_names(self):
        """ Test if the DataFrame has the correct columns """
        expected_columns = ['Date', 'Price']
        self.assertTrue(all(col in self.df.columns for col in expected_columns))

    def test_price_value(self):
        """ Test if price values are greater than zero """
        self.assertTrue((self.df['Price'] > 0).all())

    def test_average_price(self):
        """ Test to calculate the average price """
        average_price = self.df['Price'].mean()
        self.assertGreater(average_price, 0)

    def test_filter_high_prices(self):
        """ Test filtering prices greater than a certain value """
        high_prices = self.df[self.df['Price'] > 100]
        self.assertTrue((high_prices['Price'] > 100).all())

if __name__ == '__main__':
    unittest.main()
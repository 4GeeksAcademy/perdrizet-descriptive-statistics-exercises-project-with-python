"""
Unit tests for the functions module.

This module contains unit tests for the add_title_length_features function
and other utility functions used in the descriptive statistics exercises.
"""

import unittest
import pandas as pd
import numpy as np
from functions import add_title_length_features


class TestAddTitleLengthFeatures(unittest.TestCase):
    """Test cases for the add_title_length_features function."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create a sample dataframe for testing
        self.sample_data = {
            'title': ['A', 'AB', 'ABC', 'ABCD', 'ABCDE'],
            'year': [2020, 2021, 2022, 2023, 2024],
            'rating': [7.5, 8.0, 6.5, 9.0, 7.8]
        }
        self.df = pd.DataFrame(self.sample_data)
        
        # Expected title lengths for the sample data
        self.expected_lengths = [1, 2, 3, 4, 5]
    
    def test_basic_functionality(self):
        """Test basic functionality with default parameters."""
        result = add_title_length_features(self.df)
        
        # Check that the function returns a DataFrame
        self.assertIsInstance(result, pd.DataFrame)
        
        # Check that the title_length column was added
        self.assertIn('title_length', result.columns)
        
        # Check that the lengths are calculated correctly
        self.assertEqual(list(result['title_length']), self.expected_lengths)
        
        # Check that original data is preserved
        pd.testing.assert_frame_equal(result[['title', 'year', 'rating']], 
                                    self.df[['title', 'year', 'rating']])
    
    def test_custom_column_names(self):
        """Test functionality with custom column names."""
        # Create a dataframe with different column names
        custom_df = pd.DataFrame({
            'movie_name': ['Short', 'Medium Title', 'Very Long Movie Title'],
            'genre': ['Action', 'Comedy', 'Drama']
        })
        
        result = add_title_length_features(
            custom_df, 
            title_column='movie_name', 
            length_column='name_length'
        )
        
        # Check that the custom column was created
        self.assertIn('name_length', result.columns)
        
        # Check the calculated lengths
        expected_custom_lengths = [5, 12, 21]  # len of each movie_name
        self.assertEqual(list(result['name_length']), expected_custom_lengths)
    
    def test_original_dataframe_not_modified(self):
        """Test that the original dataframe is not modified."""
        original_columns = list(self.df.columns)
        original_shape = self.df.shape
        
        # Call the function
        result = add_title_length_features(self.df)
        
        # Check that original dataframe wasn't modified
        self.assertEqual(list(self.df.columns), original_columns)
        self.assertEqual(self.df.shape, original_shape)
        self.assertNotIn('title_length', self.df.columns)
        
        # But result should have the new column
        self.assertIn('title_length', result.columns)
    
    def test_empty_dataframe(self):
        """Test handling of empty dataframe."""
        empty_df = pd.DataFrame(columns=['title', 'year'])
        result = add_title_length_features(empty_df)
        
        # Should return empty dataframe with title_length column
        self.assertEqual(len(result), 0)
        self.assertIn('title_length', result.columns)
    
    def test_dataframe_with_nan_values(self):
        """Test handling of NaN values in title column."""
        nan_df = pd.DataFrame({
            'title': ['Valid Title', np.nan, 'Another Title', None],
            'year': [2020, 2021, 2022, 2023]
        })
        
        result = add_title_length_features(nan_df)
        
        # Check that valid titles have correct lengths
        self.assertEqual(result.iloc[0]['title_length'], 11)  # 'Valid Title'
        self.assertEqual(result.iloc[2]['title_length'], 13)  # 'Another Title'
        
        # Check that NaN values result in NaN lengths
        self.assertTrue(pd.isna(result.iloc[1]['title_length']))
        self.assertTrue(pd.isna(result.iloc[3]['title_length']))
    
    def test_invalid_dataframe_type(self):
        """Test error handling for invalid input type."""
        with self.assertRaises(TypeError):
            add_title_length_features("not a dataframe")
        
        with self.assertRaises(TypeError):
            add_title_length_features([1, 2, 3])
        
        with self.assertRaises(TypeError):
            add_title_length_features(None)
    
    def test_missing_title_column(self):
        """Test error handling when title column doesn't exist."""
        df_no_title = pd.DataFrame({
            'movie_name': ['Title 1', 'Title 2'],
            'year': [2020, 2021]
        })
        
        # Should raise ValueError when title column doesn't exist
        with self.assertRaises(ValueError):
            add_title_length_features(df_no_title)
        
        # Should include the column name in the error message
        with self.assertRaisesRegex(ValueError, "Column 'title' not found"):
            add_title_length_features(df_no_title)
    
    def test_special_characters_and_spaces(self):
        """Test handling of titles with special characters and spaces."""
        special_df = pd.DataFrame({
            'title': [
                'Title with spaces',
                'Title-with-dashes',
                'Title.with.dots',
                'Title (with parentheses)',
                'Title & symbols!',
                ''  # Empty string
            ]
        })
        
        result = add_title_length_features(special_df)
        
        expected_lengths = [17, 17, 15, 24, 16, 0]
        self.assertEqual(list(result['title_length']), expected_lengths)
    
    def test_unicode_characters(self):
        """Test handling of unicode characters in titles."""
        unicode_df = pd.DataFrame({
            'title': [
                'Café',
                'Naïve',
                '电影',  # Chinese characters
                'Москва',  # Cyrillic characters
                '🎬📽️'  # Emoji
            ]
        })
        
        result = add_title_length_features(unicode_df)
        
        # Check that unicode characters are counted correctly
        self.assertGreater(result.iloc[0]['title_length'], 0)  # Café
        self.assertGreater(result.iloc[1]['title_length'], 0)  # Naïve
        self.assertGreater(result.iloc[2]['title_length'], 0)  # Chinese
        self.assertGreater(result.iloc[3]['title_length'], 0)  # Cyrillic
        self.assertGreater(result.iloc[4]['title_length'], 0)  # Emoji


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)

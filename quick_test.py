import pandas as pd
from functions import add_title_length_features

# Create a test dataframe
test_df = pd.DataFrame({'title': ['Test', 'Another Test', 'A Much Longer Title']})
result = add_title_length_features(test_df)
print('Test successful!')
print(result)

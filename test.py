from ETL.Transform import clean_date
import pandas as pd
test_date_frame = pd.DataFrame({
    'date_column': ['12/31/2020', '01-15-2021', '2021.02.28', 'March 3, 2021', 'Feb-2023', 'invalid_date']
})

transformed_df = clean_date(test_date_frame, 'date_column')
print(transformed_df)



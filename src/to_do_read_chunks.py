# =============================================================================
# To Be Used Elsewhere
# =============================================================================
# =============================================================================
# Working with large CSV files in Python
# =============================================================================
# =============================================================================
# http://pythondata.com/working-large-csv-files-python/
# =============================================================================
import pandas as pd

# =============================================================================
# columns we wish to keep/filter on
# =============================================================================
cols_to_keep = ['id', 'member_id', 'loan_amnt', 'funded_amnt']
# =============================================================================
# setup dataframe iterator, the 'usecols' parameter filters the columns in the csv
# =============================================================================

kwargs = {
    'filepath_or_buffer': r'/tmp/z_data/LoanStats_2016Q1.csv.zip',
    'skiprows': 1,
    'compression': 'zip',
    'chunksize': 20000,
    'usecols': cols_to_keep
}
df_iter = pd.read_csv(**kwargs)
# =============================================================================
# this list will store the filtered dataframes for concatenation
# =============================================================================
dfs = []
for df in df_iter:
    temp_df = (df.rename(columns={
        col: col.lower() for col in df.columns
    })
        # =============================================================================
        # filter
        # =============================================================================
        .pipe(lambda x: x[x.funded_amnt > 10000]))
    dfs += [temp_df.copy()]
    # =============================================================================
    # combine filtered dfs into large output df
    # =============================================================================
    concat_df = pd.concat(dfs)

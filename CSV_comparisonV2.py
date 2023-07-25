import pandas as pd

def find_unique_terms(csv_file1, csv_file2, output_csv):
    # Read the CSV files into pandas DataFrames
    df1 = pd.read_csv(csv_file1)
    df2 = pd.read_csv(csv_file2)

    # Merge the two DataFrames on the 'term' column using an outer join
    merged_df = pd.merge(df1, df2, on='term', how='outer', suffixes=('_file1', '_file2'))

    # Filter the merged DataFrame to get rows where 'Id' from one file is null (indicating a unique term)
    unique_terms_df = merged_df[merged_df['Id_file1'].isnull() | merged_df['Id_file2'].isnull()]

    # Select only the 'term' and 'Id' columns
    unique_terms_df = unique_terms_df[['term', 'Id_file1', 'Id_file2']]

    # Rename the columns for clarity
    unique_terms_df.columns = ['term', 'Id_in_file1', 'Id_in_file2']

    # Write the result to a new CSV file
    unique_terms_df.to_csv(output_csv, index=False)
    
#add relevant file names and file locations here.     
if __name__ == "__main__":
   csv_file1 = r'C:\Users\lmust\Documents\ST3 year (ACF BHF 1)\targeted screening\CODELISTS\HYPERTENSION_Gold\18072023_1.csv'
   csv_file2 = r'C:\Users\lmust\Documents\ST3 year (ACF BHF 1)\targeted screening\CODELISTS\HYPERTENSION_Gold\COMPARATOR_NHSD_opensafely-hypertension-2020-04-28.csv'
   output_csv = r'C:\Users\lmust\Documents\ST3 year (ACF BHF 1)\targeted screening\CODELISTS\HYPERTENSION_Gold\output.csv'

   find_unique_terms(csv_file1, csv_file2, output_csv)

